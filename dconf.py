#!/usr/bin/env python3
import os, sys

# ./dconf.py --dump settings.ini
# ./dconf.py --load settings.ini

class dconfy:
    ini_path = ""
    def init(self, path):
        self.ini_path = path
        return
    
    def dump(self):
        os.system("dconf dump / > " + self.ini_path)
        return

    def load(self):
        os.system("dconf load / < " + self.ini_path)
        return

def main():
    option = sys.argv[1]
    path = sys.argv[2]
    dc = dconfy()
    dc.init(path)
    if option == "--dump":
        dc.dump()
    elif option == "--load":
        dc.load();
    else:
        print("unexpected params!")

try:
    main()
except:
    print("\n")
    print("true usage\n==========")
    print(" -> ./dconf.py --dump <*.ini>")
    print(" -> ./dconf.py --load <*.ini>")
    print("\n")
    
main()
