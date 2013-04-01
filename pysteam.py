from xml.dom.minidom import parse
import urllib, urllib2, os, codecs, platform, getpass
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# -- Define OS specifc variables --

if(platform.system()) == "Posix":
    steamapps = "steamapps"
    steamcmd = "steamcmd.sh"
    url = "http://media.steampowered.com/client/steamcmd_linux.tar.gz"
    def cls():
      os.system("clear")
    def getsteamcmd():
        steamcmd_download = urllib2.urlopen(url)
        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(steamcmd_download.read())
            with zipfile.ZipFile('steamcmd_linux.tar.gz', "r") as z:
                z.extractall(os.getcwd())
    cls()
    print('Linux is not supported at this time. Watch the GitHub repo or check back later!')
    raw_input('Press enter to close...')
    cls()
    exit()

elif(platform.system()) == "Darwin":
    steamapps = "steamapps"
    steamcmd = "steamcmd.sh"
    url = "http://media.steampowered.com/client/steamcmd_linux.tar.gz"
    def cls():
      os.system("clear")
    def getsteamcmd():
        steamcmd_download = urllib2.urlopen(url)
        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(steamcmd_download.read())
            with zipfile.ZipFile('steamcmd_linux.tar.gz', "r") as z:
                z.extractall(os.getcwd())
    cls()
    print('OS X is not supported at this time. Watch the GitHub repo or check back later!')
    raw_input('Press enter to close...')
    cls()
    exit()

elif(platform.system()) == "Windows":
    steamapps = "SteamApps"
    steamcmd = "steamcmd.exe"
    url = 'hhttp://media.steampowered.com/client/steamcmd_win32.zip'
    def cls():
        os.system("cls")
    def getsteamcmd():
        steamcmd_download = urllib2.urlopen(url)
        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(steamcmd_download.read())
            with zipfile.ZipFile('steamcmd_win32.zip', "r") as z:
                z.extractall(os.getcwd())

# -- MAIN PROGRAM --

username = raw_input('Please enter your username you use to login: ')
password = getpass.getpass('Please enter your password: ')
steam_id = raw_input('Please enter your SteamID/custom URL: ')

if os.path.exists(steamapps) == False:
   #Change example location for future use
   print('Not in Steam root folder (eg. C:\Program File (x86)\Steam\)!')
   print('Please move to Steam root and run again!')
   raw_input('Press enter to close...')
   exit()

try:
   with open(steamcmd): pass
except IOError:
   print steamcmd+' not found!'
   print 'Downloading '+steamcmd
   getsteamcmd()
   os.system(steamcmd+" +quit")

print 'Connecting to Steam...'
xml = urllib.urlopen('http://steamcommunity.com/id/'+steam_id+'/games?tab=all&xml=1')
print 'Parsing response...'
dom = parse(xml)
x = 0

cls()

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

# -- "Documentation" --

# TODO:
'''
Log output
OSX/Linux support (OS specific variables semi-done)
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