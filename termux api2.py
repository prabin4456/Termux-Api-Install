import os
r='\033[1;31m'
s='\033[0m'
g='\033[1;32m'
y='\033[1;33m'
b='\033[1;34m'
cyan='\033[1;36m'
p='\033[1;35m'

os.system("termux-brightness 150")
os.system("termux-volume music 100")
os.system("termux-tts-speak -p 1 -r 0.6 welcome sir. choose any option")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$                      $$")
print(f"$$  {r} $${s}                 $$")
print(f"$$  {r} $$ {s}                $$         CODER -{b} _A.R.O_{s}")
print(f"$$  {r} $$ {s}                $$         FOLLOW -{p} an.onymous0{s}")
print(f"$$  {r} $$ {s}                $$")
print("$$                      $$")
print("$$                      $$")
print("$$                      $$")
print("$$                      $$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("")
print(f"   {g}  ANDRO_INFORMER")
print("")
print(f"{r}1.{s}vibrate")
print(f"{r}2.{s}volume")
print(f"{r}3.{s}torch")
print(f"{r}4.{s}battery-info")
print(f"{r}5.{s}brightness")
print(f"{r}6.{s}speek")
print(f"{r}7.{s}wifi-info")
print(f"{r}8.{s}send-files")
print(f"{r}9.{s}calling")
print(f"{r}10.{s}current-wifi-info")
print(f"{r}11.{s}wifi")
print(f"{r}12.{s}speech-to-text")
print(f"{r}13.{s}contact-list")
print(f"{r}14.{s}termux-info")
print(f"{r}15.{s}telephony-deviceinfo")
print(f"{r}16.{s}camera-info")
print("")
b=int(input(f"{g}==={s}>{y} "))
if b==1:
    print("for example 5000")
    c=input("duration = ")
    os.system(f"termux-vibrate -d {c} -f")
if b==2:
    print("1.music")
    print("2.alarm")
    print("3.system")
    d=int(input("==× "))
    if d==1:
        print("for example 150")
        e=input("volume = ")
        os.system(f"termux-volume music {e}")
    if d==2:
        print("for example 150")
        e=input("volume = ")
        os.system(f"termux-volume alarm {e}")
    if d==3:
        print("for example 150")
        e=input("volume = ")
        os.system(f"termux-volume system {e}")
if b==3:
    os.system("termux-torch on")
if b==4:
    os.system("termux-battery-status")
if b==5:
    c=input("brightness 1-250 = ")
    os.system(f"termux-brightness {c}")
if b==6:
    c=input("(default 0.1) pitch = ")
    d=input("(default 0.1) rate = ")
    e=input("enter your message = ")
    os.system(f"termux-tts-speak -p {c} -r {d} {e}")

if b==7:
    os.system("termux-wifi-scaninfo")
if b==8:
    c=input(" file name = ")
    os.system(f"termux-open --send {c}")
if b==9:
    d=int(input("enter number = "))
    os.system(f"termux-telephony-call {d}")
if b==10:
    os.system("termux-wifi-connectioninfo")
if b==11:
    print("1.wifi-on")
    print("2.wifi-off")
    d=input("==> ")
    if d==1:
        os.system("termux-wifi-enable true")
    if d==2:
        os.system("termux-wifi-enable false")
if b==12:
    print("for example speek hello")
    os.system("termux-speech-to-text")
if b==13:
    os.system("termux-contact-list")
if b==14:
    os.system("termux-info")
if b==15:
    os.system("termux-telephony-deviceinfo")
if b==16:
    os.system("termux-camera-info")
os.system(" cd")
os.system("cd /data/data/com.termux/files/home/andro_informer")
os.system("python ai.py")

