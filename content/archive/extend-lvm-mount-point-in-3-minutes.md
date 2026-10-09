---
title: "Extend lvm mount point in 3 minutes"
date: 2011-04-17
post_lang: en
tags: [debian, linux, shell, ubuntu]
original_url: http://www.joanmarcriera.es/2011/04/17/extend-lvm-mount-point-in-3-minutes/
summary: "Step-by-step: add a new disk, make it an LVM physical volume, and grow a logical volume and its filesystem online."
draft: false
---

Follow the steps:

1) Add your new disk (Virtual disk or physical LUN)

2) Find them:

```bash
echo "- - -" > /sys/class/scsi_host/host0/scan
```

3) Do a partition (type 8e=> LVM)

```bash
fdisk /dev/sdb
n
p
default =1
default
t
8e
w
```

4) Create Physical Volume on partition

```bash
pvcreate /dev/sdb1
```

5) Add the PV to the Volume Group

```bash
vgdisplay # show your volume groups, I need to add sdb1 to vg01
vgextend vg01 /dev/sdb1
```

6) Add the new space on the VG to the Logical Volume (I add 5GB)

```bash
lvdisplay # shows your logical volumes , I need to extend /dev/vg01/var
lvextend -L+5G /dev/vg01/var
```

7) Resize the filesystem on the LV

```bash
resize2fs /dev/vg01/var
```

Resize your partition, so it gets the new inodes. if it's your root partition a backup may give you some peace.

8) done.

Extra documentation: <http://www.cyberciti.biz/tips/vmware-add-a-new-hard-disk-without-rebooting-guest.html>

## 2026 note

The LVM steps are unchanged and still work. Today `pvcreate` can be given the whole disk (no partition needed), and `lvextend -r -L+5G /dev/vg01/var` grows the filesystem in the same command (`-r` calls the right resize tool, which also covers XFS via `xfs_growfs`; `resize2fs` is only for ext2/3/4). Rescanning a SCSI host with `echo "- - -" > /sys/class/scsi_host/hostN/scan` is still the way to see a newly attached virtual disk without rebooting.
