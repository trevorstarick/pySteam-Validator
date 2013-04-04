#!/usr/bin/python
# -*- coding: utf-8 -*-

# pySteam-Validator: Validates and downloads a users Steam library.

# Version:  1.1 (2013/04/03)
# Author:   Trevor Starick <trevor.starick@gmail.com>


from xml.dom.minidom import parse
import urllib
import os
import codecs
import platform
import getpass
import zipfile
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# -- Define OS specific variables --
if(platform.system()) == "Windows":
    url = 'http://media.steampowered.com/client/steamcmd_win32.zip'
    os.system("cls")
elif(platform.system()) == "Posix" or "Linux":
    os.system('clear')
    print(
        'Linux is not supported at this time.'
        'Watch the GitHub repo or check back later!')
    raw_input('Press enter to close...')
    os.system('clear')
    exit()
elif(platform.system()) == "Darwin":
    os.system('clear')
    print(
        'OS X is not supported at this time.'
        'Watch the GitHub repo or check back later!')
    raw_input('Press enter to close...')
    os.system('clear')
    exit()

# -- MAIN PROGRAM --
username = raw_input('Please enter your username you use to login: ')
password = getpass.getpass('Please enter your password: ')
steam_id = raw_input('Please enter your SteamID/custom URL: ')

if os.path.exists("SteamApps") is False:
    # Change example location for future use
    print('Not in Steam root folder (eg. C:\Program File (x86)\Steam\)!')
    print('Please move to Steam root and run again!')
    raw_input('Press enter to close...')
    exit()

try:
    with open("steamcmd.exe"):
        pass
except IOError:
    print 'steamcmd.exe not found!'
    print 'Downloading steamcmd.exe'
    urllib.urlretrieve(url, "steamcmd_win32.zip")
    with zipfile.ZipFile('steamcmd_win32.zip', "r") as z:
        z.extractall(os.getcwd())
    os.system("steamcmd.exe +quit")

print 'Connecting to Steam...'
xml = urllib.urlopen(
    'http://steamcommunity.com/id/'+steam_id+'/games?tab=all&xml=1')
print 'Parsing response...'
dom = parse(xml)
x = 0

os.system("cls")

for node in dom.getElementsByTagName('game'):
    appID = dom.getElementsByTagName('appID')[x].toxml()
    appID = appID.replace("<appID>", "")
    appID = appID.replace("</appID>", "")
    name = dom.getElementsByTagName('name')[x].toxml()
    name = name.replace("<name><![CDATA[", "")
    name = name.replace("]]></name>", "")
    name = name.encode('ascii', 'ignore')
    print name + " | " + appID + '\n'
    os.system("title Updating: "+name)
    os.system("steamcmd.exe +login "+username+" "+password+" +app_update "+appID+" +quit")
    x += 1
