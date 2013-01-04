from xml.dom.minidom import parse
import urllib
import webbrowser
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

cls()
steam_id = raw_input('Please enter your Steam ID: ')
cls()
print 'Connecting to Steam...'
#xml = urllib.urlopen('http://steamcommunity.com/id/tstarick/games?tab=all&xml=1')
xml = urllib.urlopen('http://steamcommunity.com/id/'+steam_id+'/games?tab=all&xml=1')
print 'Parsing response...'
dom = parse(xml)
x = 0

for node in dom.getElementsByTagName('game'):
	#for node in dom.getElementsByTagName('appID'):
	appID = dom.getElementsByTagName('appID')[x].toxml()
	appID = appID.replace("<appID>", "")
	appID = appID.replace("</appID>", "")
	
	#--	TO ADD [$NAME | $APPID] --#
	#for node in dom.getElementsByTagName('name'):
	#	name = dom.getElementsByTagName('name')[x].toxml()
	#	name = appID.replace("<name><![CDATA[", "")
	#	name = appID.replace("]]></name>", "")
	#print name + " | " + appID
	
	print appID
	url = 'steam://validate/'+appID
	webbrowser.open(url)
	pause = raw_input('Press enter when the Steam validation window closes...')
	x += 1