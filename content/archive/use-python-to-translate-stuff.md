---
title: "Use python to handle email, translate , and publish to wordpress"
date: 2014-08-10
post_lang: en
tags: [divertimento]
original_url: http://www.joanmarcriera.es/2014/08/10/use-python-to-translate-stuff/
summary: "Python 2 script that reads unread Gmail messages over IMAP, translates them with goslate and saves them as WordPress drafts."
draft: false
---

This weekend I tried to refresh my python with one single idea in mind. But now I don't have time to explain it, so here comes the code:


```python
#!/usr/bin/env python
#
#usage: python2 translate_mail.py

from GmailClass import GmailClass
import goslate
import datetime, xmlrpclib
import time

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from datetime import datetime


gs=goslate.Goslate()

correo=GmailClass("user@example.com","CHANGE_ME","Foldera")
correo.connect()
correo.select_mailbox()
no_leidos=correo.get_unreaded_list()

wp_url = 'https://example.com/blog/xmlrpc.php'
wp_username = 'CHANGE_ME'
wp_password = 'CHANGE_ME'




for un_correo_no_leido in no_leidos[0].split():
      
    print "\nProcessing one unread..."
    msg=correo.get_a_mail(un_correo_no_leido)
    titulo_original=correo.get_the_subject(msg)
    print "\t " + titulo_original
    body_original=correo.get_the_body(msg)
    titulo_es=gs.translate(titulo_original,'es')
    body_es=gs.translate(body_original,'es')
      
    title=titulo_es
    content=body_es
    
    post = WordPressPost()
    post.title = title
    post.content = content
    post.date = datetime(2014, 8, 10, 12, 34, 2, 860000)
    post.post_status = 'draft'
    try:
        wp = Client(wp_url,wp_username,wp_password) 
        wp.call(NewPost(post))
    except  ServerConnectionError as e:
        #do something with e
        #or by now pass
        print "serverconnection error"
        pass
    except ProtocolError as e:
        #do something or pass
        print "protocol error"
        pass
    else:
        del post
        del wp
    
    print "\t Done."
    print "Now wait 10 seconds\n"
    time.sleep(10)
    
```



```python
#!/usr/bin/env python
#
#usage: imported by the script above

import sys
import imaplib
#not needed #import getpass
import email
import email.header
import datetime

#class to manage gmail.
class GmailClass(object):
   
    #Basic initialize.
    #Here is were we need to declare which account and folder we would like to process
    #example a=GmailClass('user@example.com','CHANGE_ME','kate')
    def __init__(self, account, pwsd, folder):
        self.folder = folder
        self.email_account = account
        self.email_password = pwsd

    #automatic for test 
    def prepare(self):
        self.connect()
        self.select_mailbox()
        
    
    #Connect to the mailbox.
    def connect(self):
        self.mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
        try:
            rv, data = self.mailbox.login(self.email_account, self.email_password)
        except imaplib.IMAP4.error:
            print "LOGIN FAILED!!! "
            sys.exit(1)
        print rv, data
        print "You can now select a mailbox"
    
    #just if you want to know how many folders do you have    
    def list_mailboxes(self):
        #needs pretty print
        rv, mailboxes = self.mailbox.list()
        if rv == 'OK':
            print "Mailboxes:"
            print mailboxes
            print "Select one of them to be able to process it."
    
    #go into the folder
    def select_mailbox(self):
        rv, data = self.mailbox.select(self.folder)
        if rv == 'OK':
            print "You can now start processing mailbox...\n"
        else:
            print "ERROR: Unable to open mailbox ", rv    
            
    #which mails are still unread
    def get_unreaded_list(self):
        rv, data = self.mailbox.search(None, "UnSeen")
        if rv != 'OK':
            print "No messages found!"
            return
        else:
            print "Messages found "
            return data
    
    #return a mail object
    #the list from get_unreaded_list needs to be looped data[i]
    def get_a_mail(self,num):
        rv, data = self.mailbox.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            return
        else:
            msg = email.message_from_string(data[0][1])
            return msg

     
    #from a mail object get the subject   
    def get_the_subject(self,msg):
        decode = email.header.decode_header(msg['Subject'])[0]
        subject = unicode(decode[0])
        #print 'Message Subject: %s' % ( subject)
        return subject
    
    #from a mail object the date
    def get_the_date(self,msg):
        #print 'Raw Date:', msg['Date']
        return msg['Date']

        
    #from a mail object get the body    
    def get_the_body(self,msg):
        maintype = msg.get_content_maintype()
        if maintype == 'multipart':
            for part in msg.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return msg.get_payload()


    #method to process mailbox    
    def process_mailbox(self):
        """
        Do something with emails messages in the folder.  
        For the sake of this example, print some headers.
        """
        rv, data = self.mailbox.search(None, "ALL")
        if rv != 'OK':
            print "No messages found!"
            return
    
        for num in data[0].split():
            rv, data = self.mailbox.fetch(num, '(RFC822)')
            if rv != 'OK':
                print "ERROR getting message", num
                return
    
            msg = email.message_from_string(data[0][1])
            decode = email.header.decode_header(msg['Subject'])[0]
            subject = unicode(decode[0])
            print 'Message %s: %s' % (num, subject)
            print 'Raw Date:', msg['Date']
            # Now convert to local date-time
            date_tuple = email.utils.parsedate_tz(msg['Date'])
            if date_tuple:
                local_date = datetime.datetime.fromtimestamp(
                    email.utils.mktime_tz(date_tuple))
                print "Local Date:", \
                    local_date.strftime("%a, %d %b %Y %H:%M:%S")
                
    #Close the sessions at the end
    def close(self):
        self.mailbox.close()
        self.mailbox.logout()
    
```

## 2026 note

This is Python 2 code (`print` statements, `xmlrpclib`, `unicode`) and will not run on Python 3 without porting. `goslate` stopped working when Google changed the web endpoint it scraped, so use an official translation API or a local model instead, and Gmail IMAP now needs an app password or OAuth rather than the account password. WordPress has a REST API with application passwords, which is the current way to create draft posts.
