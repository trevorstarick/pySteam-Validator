#pySteam Validator


A program written to validate and download a users Steam game library. Uses the SteamCMD.exe application by Valve.

##Usage
If you have Python 2.7.3 installed you can skip to part 3.

1. Download [Python 2.7.3](http://www.python.org/getit/releases/2.7.3/)
2. Install Python 2.7.3 and make sure that `C:\Python27\` is in your `$PATH`
3. To run the program, copy `pysteam.py` to your Steam root directory (eg. `C:\Program Files(x86)\Steam\`) and execute `python steam.py`

**Bonus:**

1. If you want to compile `pysteam.py` into an executable file download and install [py2exe](http://www.py2exe.org/) and run `build.py`
2. Navigate to `dist` and copy everything to your Steam root directory
3. Now you should be able to run `pysteam.exe`

##Common Issues
###pysteam.py
* `Not in Steam root folder (eg. C:\Program File (x86)\Steam\)!` - Move `pysteam.py` or `pysteam.exe` to wherever you installed Steam and the `steam.exe` executable is located.

###setup.py
* `ImportError: No module named py2exe` - Install [py2exe](http://www.py2exe.org/).

###Steam
* Steam isn't loading now or crashes! - Delete the `ClientRegistry.blob` file located inside your Steam root directory. This generaly fixes most Steam loading issues.


##Donations
**Bitcoin:** _1PLi4dHvvghyrCjm5fwnN7Ap1FwxrdWKVk_
