from xml.dom.minidom import parse
import urllib
import os
import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
print 'Connecting to Steam...'
xml = urllib.urlopen('http://steamcommunity.com/id/yourUserNameHere/games?tab=all&xml=1')
print 'Parsing response...'
dom = parse(xml)
x = 0

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
        os.system("E:/Steam/steamcmd.exe +login yourLoginHere yourPasswordHere +app_update "+appID+" +quit")
        x += 1

# TODO:
'''
Download steamcmd.exe from steam servers and unzip
Write Check if file exisits function
Log output
'''
# PLAN
'''
CHECK IF steam.exe EXISITS:
-IF FALSE: print "not in steam root"
-IF TRUE: continue

CHECK IF steamcmd.exe EXISTS:
-IF FALSE:
        DOWNLOAD steamcmd.exe:
        import os
        import urllib2

        url = 'http://starick.me/steamcmd.exe'
        steamcmd = urllib2.urlopen(url)

        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(steamcmd.read())
-IF TRUE:continue

ASK FOR STEAMID,USERNAME,PASSWORD
'''
