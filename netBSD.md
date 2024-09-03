## NetBSD:

### Install NetBSD on VMware Workstation:
```bash
# 0:00 -> 6:40
https://www.youtube.com/watch?v=Nfd4IdzdicM
```

### Download file iso:
```bash
https://drive.google.com/file/d/1jFF6ZwTF_Zq2sIa3_siHqoF6FSFKybWz/view
```

### Install NetBSD on VMware Workstation:
```bash
whoami
pkgin update
pkgin upgrade
pkgin install bash nano
bash
pkgin install xfce4 xfce4-desktop fam tdb gvs xfce4-thunar hal

nano .xinitrc
xfce4-session
# ctrl X --> Y --> enter to save file

ln -s .xinitrc .xsession
ls -al
cp .xinitrc /home/phanvanbang/
chown phanvanbang:wheel /home/phanvanbang/.xinitrc
ln -s /home/phanvanbang/.xinitrc /home/phanvanbang/.xsession
cp /usr/pkg/share/examples/rc.d/famd /etc/rc.d/
cp /usr/pkg/share/examples/rc.d/dbus /etc/rc.d/
cp /usr/pkg/share/examples/rc.d/hal /etc/rc.d/

nano /etc/rc.conf
rpcbind=YES
dbus=YES
hal=YES
famd=YES
vmtools=YES

pkgin install open-vm-tools
cp /usr/pkg/share/examples/rc.d/vmtools /etc/rc.d/vmtools

# github in netBSD
pkgin install firefox
pkgin install git

# fix bug github
git config --global http.sslVerify false
git clone ...

reboot

# account
login: phanvanbang
passwd: 123456

startx

# p/s: all "phanvanbang" is user name, if your set another user name, change it :v
```