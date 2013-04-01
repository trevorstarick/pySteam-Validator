#pySteam Validator


A program written to validate and download a users Steam game library. Uses the SteamCMD.exe application by Valve.

##Usage


To run the program, copy `pysteam.py` to your Steam root directory (eg. `C:\Program Files(x86)\Steam\`) and execute `python steam.py` or copy everything from the `dist` folder into the root Steam folder and run `pysteam.exe`

##Common Issues
###setup.py
* `ImportError: No module named py2exe` - Install [py2exe](http://www.py2exe.org/)
