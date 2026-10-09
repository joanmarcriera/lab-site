---
title: "Visual Basic script to pack, zip and send a full report."
date: 2014-08-19
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/19/visual-basic-script-to-pack-zip-and-send-a-full-report/
summary: "A VBScript for Windows that zips a folder with built-in shell objects, logs progress and emails the archive as a monthly report."
draft: false
---

Each first Monday of each month I needed to prepare and send a report to some customers. Everything was on windows, so Visual Basic was the one to be used. Nowadays I would ask to reinstall the machine to be able to use Powershellv3 or so, but at that point this is what I got.


```vb
'compress folder and send a zip file
'TODO : 


Option Explicit

Dim outputFileZip, outputErrFile, mailTextFile, reportFolder, emailFrom, emailTo, dateStamp, emailSubject
outputFileZip = "D:\Reports\ReportLastMonth.zip"
mailTextFile = "D:\Reports\report_scripts\file1.txt"
outputErrFile = "D:\Reports\report_scripts\file2.txt"
reportFolder = "D:\Reports\LastMonth"
emailFrom = "sender@example.com"
emailTo = "user1@example.com;user2@example.com;user3@example.com"
emailSubject = "Summary report "
dateStamp = Date()

' -=-=-=-=-=-=-=-=-=-
''''''''''''''' Prepare log file
dim loggit_logfilename, loggit_fso, loggit_silent, tempFile

loggit_logfilename = outputErrFile
loggit_silent = true   ' log file only or with MsgBox/Echo
set loggit_fso = CreateObject("Scripting.FileSystemObject")
set tempFile = loggit_fso.OpenTextFile(loggit_logfilename, 2, True)
tempFile.Write ""
tempFile.Close 

' -=-=-=-=-=-=-=-=-=-
sub loggit (msg)
	Dim stream
    set stream = loggit_fso.OpenTextFile(loggit_logfilename, 8, True)
    stream.writeline date & " " & time & ": " & msg
    stream.close
    if not loggit_silent then
       WScript.echo msg 
    end if   
end sub
' -=-=-=-=-=-=-=-=-=-

'''''''''''''''''''' Log file ready. :)
loggit "Started..."

' -=-=-=-=-=-=-=-=-=-
' Funtion used on date string
' -=-=-=-=-=-=-=-=-=-

Dim objFSO,strDate

Function padDate(intNumber)
	if intNumber <= 9 Then
		padDate = "0" & CStr(intNumber)
	Else
		padDate = CStr(intNumber)
	End If
End Function

' -=-=-=-=-=-=-=-=-=-


'''''''''''''''beggin
Dim arrResult
'''ZipFolder funcion is at the end of this file. 
loggit "Launch ziping function."
arrResult = ZipFolder( reportFolder, outputFileZip )
loggit "Finish ziping function. "

If arrResult(0) = 0 Then
    If arrResult(1) = 1 Then
       'WScript.Echo "Done; 1 empty subfolder was skipped."
	   loggit "Done; 1 empty subfolder was skipped."
    Else
       'WScript.Echo "Done; " & arrResult(1) & " empty subfolders were skipped."
	   loggit "Done; " & arrResult(1) & " empty subfolders were skipped."
    End If
Else
    'WScript.Echo "ERROR ziping the lastMonth folder. Call the sysadmin ASAP" & Join( arrResult, vbCrLf )
	loggit "ERROR ziping the lastMonth folder. We are going to look at this and report back to you as soon as possible. :: " & Join( arrResult, vbCrLf )
End If

'''' Writing Done before the file gets into the may body text.
loggit "Done."
''''
'prepare mail content
Dim objEmail
Set objEmail = CreateObject("CDO.Message")
Const ForReading = 1, ForWriting = 2, ForAppending = 8
Dim fso, f, f2
Set fso = CreateObject("Scripting.FileSystemObject")
'Open the file for reading
Set f = fso.OpenTextFile(mailTextFile, ForReading)
Set f2 = fso.OpenTextFile(outputErrFile, ForReading)
'The ReadAll method reads the entire file into the variable BodyText
Dim BodyText
BodyText = f.ReadAll&f2.ReadAll
'Close the file
f.Close
f2.Close
Set f = Nothing
Set f2 = Nothing


'send mail
objEmail.From = emailFrom
objEmail.To = emailTo
objEmail.Subject = emailSubject & " --- " & dateStamp
objEmail.TextBody = BodyText
objEmail.AddAttachment outputFileZip
objEmail.Configuration.Fields.Item _
    ("http://schemas.microsoft.com/cdo/configuration/sendusing") = 2
objEmail.Configuration.Fields.Item _
    ("http://schemas.microsoft.com/cdo/configuration/smtpserver") = _
        "192.0.2.25"
objEmail.Configuration.Fields.Item _
    ("http://schemas.microsoft.com/cdo/configuration/smtpserverport") = 25
objEmail.Configuration.Fields.Update
objEmail.Send

loggit "File has been send"

Set objFSO = CreateObject("Scripting.FileSystemObject")
'MsgBox	Year(Date) & "-" & padDate(Month(Date)) & "-" & padDate(Day(Date))
strDate = Year(Date) & "-" & padDate(Month(Date)) & "-" & padDate(Day(Date))

loggit "Moving zip file to zip file with date"
If (objFSO.FileExists(outputFileZip)) Then
	objFSO.MoveFile outputFileZip , outputFileZip & "-" & strdate & ".zip"
End If
loggit "Moved."
loggit "Done. :) "

'''
Function ZipFolder( myFolder, myZipFile )
' This function recursively ZIPs an entire folder into a single ZIP file,
' using only Windows' built-in ("native") objects and methods.
'
' Last Modified:
' March 8, 2012
'
' Arguments:
' myFolder   [string]  the fully qualified path of the folder to be ZIPped
' myZipFile  [string]  the fully qualified path of the target ZIP file
'
' Return Code:
' An array with the error number at index 0, the source at index 1, and
' the description at index 2. If the error number equals 0, all went well
' and at index 1 the number of skipped empty subfolders can be found.
'
' Notes:
' [1] If the specified ZIP file exists, it will be overwritten
'     (NOT APPENDED) without notice!
' [2] Empty subfolders in the specified source folder will be skipped
'     without notice; lower level subfolders WILL be added, wether
'     empty or not.
'
' Based on a VBA script (http://www.rondebruin.nl/windowsxpzip.htm)
' by Ron de Bruin, http://www.rondebruin.nl
'
' (Re)written by Rob van der Woude
' http://www.robvanderwoude.com
' (Re) Joan Marc Riera - added outfile for errors/log

    ' Standard housekeeping
    Dim intSkipped, intSrcItems
    Dim objApp, objFolder, objFSO, objItem, objTxt, objErrFSO, objErrTxt
    Dim strSkipped

    Const ForWriting = 2

    intSkipped = 0
	
    ' Make sure the path ends with a backslash
    If Right( myFolder, 1 ) <> "\" Then
        myFolder = myFolder & "\"
	Else
		loggit "	- The path does  not end with backslash " & "\" 
    End If

    ' Use custom error handling
    On Error Resume Next

    ' Create an empty ZIP file
    Set objFSO = CreateObject( "Scripting.FileSystemObject" )
    Set objTxt = objFSO.OpenTextFile( myZipFile, ForWriting, True )
    objTxt.Write "PK" & Chr(5) & Chr(6) & String( 18, Chr(0) )
    objTxt.Close
    Set objTxt = Nothing

    ' Abort on errors
    If Err Then
        ZipFolder = Array( Err.Number, Err.Source, Err.Description )
		loggit "	- ERROR !!!! - " & Err.Number & " " & Err.Source & " " & Err.Description & "------" 
        Err.Clear
        On Error Goto 0
        Exit Function
    End If
    
    ' Create a Shell object
    Set objApp = CreateObject( "Shell.Application" )
	
	loggit "	- copy files to compressed folder . started. "
    ' Copy the files to the compressed folder
    For Each objItem in objApp.NameSpace( myFolder ).Items
        If objItem.IsFolder Then
            ' Check if the subfolder is empty, and if
            ' so, skip it to prevent an error message
            Set objFolder = objFSO.GetFolder( objItem.Path )
            If objFolder.Files.Count + objFolder.SubFolders.Count = 0 Then
                intSkipped = intSkipped + 1
            Else
                objApp.NameSpace( myZipFile ).CopyHere objItem
            End If
        Else
            objApp.NameSpace( myZipFile ).CopyHere objItem
        End If
    Next
	loggit "	- copy files to compressed folder . finished ."
	
    Set objFolder = Nothing
    Set objFSO    = Nothing

    ' Abort on errors
    If Err Then
        ZipFolder = Array( Err.Number, Err.Source, Err.Description )
		loggit "	- ERROR !!!! - " & Err.Number & " " & Err.Source & " " & Err.Description & "------" 
        Set objApp = Nothing
        Err.Clear
        On Error Goto 0
        Exit Function
    End If
	loggit "	- Compression started.  "
    ' Keep script waiting until compression is done
    intSrcItems = objApp.NameSpace( myFolder  ).Items.Count
    Do Until objApp.NameSpace( myZipFile ).Items.Count + intSkipped = intSrcItems
        WScript.Sleep 2000
    Loop
    Set objApp = Nothing
	loggit "	- Compression finished.  "
	
    ' Abort on errors
    If Err Then
        ZipFolder = Array( Err.Number, Err.Source, Err.Description )
		loggit "	- ERROR - " & Err.Number & " " & Err.Source & " " & Err.Description & "------" 
        Err.Clear
        On Error Goto 0
        Exit Function
    End If

    ' Restore default error handling
    On Error Goto 0

    ' Return message if empty subfolders were skipped
    If intSkipped = 0 Then
        strSkipped = "No items skipped."
    Else
        strSkipped = "skipped empty subfolders"
    End If

    ' Return code 0 (no error occurred)
    ZipFolder = Array( 0, intSkipped, strSkipped )
End Function

' close error file, here is where loggit sends the strings
Set fso = Nothing

WScript.Quit(0)
```

## 2026 note

VBScript is deprecated by Microsoft and is being removed from Windows as an optional feature, and CDO mail sending is legacy as well. On current Windows, PowerShell's `Compress-Archive` replaces the shell-object zipping, and for mail a scheduled task calling an authenticated SMTP client or an API is preferable, since `Send-MailMessage` is itself marked obsolete.
