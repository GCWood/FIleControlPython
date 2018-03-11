import os
from datetime import datetime
import calendar


class Listing:
    def __init__(self, directory):
        self.directory = directory
    def listdirs(self):
        os.chdir(self.directory);
        for root, dirs, files in os.walk(".",topdown=True):
           for name in files:
              con = open(name, "r")
              file_o = con.read()
              day = file_o[file_o.index("(") + 1:file_o.index(")")]
              print(os.path.join(root, name) + " " + day)
    def getdirs(self):
        os.chdir(self.directory)
        dirs = []
        for root, dirs, files in os.walk(".",topdown=True):
           for name in files:
              dirs.append(name)

        return dirs

class File:
    def __init__(self,file):
        self.file = file
    def gettimestamp(self):
        mod_time = os.stat(self.file).st_mtime
        return datetime.fromtimestamp(mod_time)

              
adv = Listing("advice")
for i in adv.getdirs():
    fil = File(i)
    print(fil.gettimestamp())
