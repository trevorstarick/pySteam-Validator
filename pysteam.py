from xml.dom.minidom import parse
import urllib
import urllib2
import os
import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

username = raw_input('Please enter your username you use to login: ')
password = raw_input('Please enter your password: ')
steam_id = raw_input('Please enter your SteamID: ')

os.system('cls')

try:
   with open('steam.exe'): pass
except IOError:
   print('Not in Steam root folder (eg. C:\Program File (x86)\Steam\)!')
   raw_input('Please move to Steam root and run again!')
   exit()

try:
   with open('steamcmd.exe'): pass
except IOError:
   print 'steamcmd.exe not found!'
   print 'Downloading steamcmd.exe'
   url = 'http://starick.me/steamcmd.exe'
   steamcmd = urllib2.urlopen(url)
   with open(os.path.basename(url), "wb") as local_file:
           local_file.write(steamcmd.read())
   os.system("steamcmd.exe +quit")

print 'Connecting to Steam...'
xml = urllib.urlopen('http://steamcommunity.com/id/'+steam_id+'/games?tab=all&xml=1')
print 'Parsing response...'
dom = parse(xml)
x = 0

os.system('cls')

for node in dom.getElementsByTagName('game'):
	appID = dom.getElementsByTagName('appID')[x].toxml()
	appID = appID.replace("<appID>", "")
	appID = appID.replace("</appID>", "")
	name = dom.getElementsByTagName('name')[x].toxml()
	name = name.replace("<name><![CDATA[", "")
	name = name.replace("]]></name>", "")
	name = name.encode('ascii','ignore')
        print name + " | " + appID + '\n'
        os.system("title Updating: "+name)
        os.system("steamcmd.exe +login "+username+" "+password+" +app_update "+appID+" +quit")
        x += 1


# TODO:
'''
Download steamcmd.exe from steam servers and unzip
Log output
OSX/Linux support
Installer
'''
# PLAN
'''
CHECK IF steam.exe EXISITS:
-IF FALSE: print "not in steam root (C:\Program File (x86)\Steam\"
-IF TRUE: continue

CHECK IF steamcmd.exe EXISTS:
-IF FALSE:DOWNLOAD steamcmd.exe:
-IF TRUE:continue

ASK FOR STEAMID,USERNAME,PASSWORD
'''
