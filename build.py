import os
import zipfile

os.system("python setup.py install")
os.system("python setup.py py2exe")
os.system("mkdir dist\src")
os.system("copy *.py dist\src")
