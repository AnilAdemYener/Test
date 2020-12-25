#!/usr/bin/env python3
import os, sys

class MainApplication:
    username = 'lovisestdeus'
    repository = None
    folder = None
    def __init__(self):
        if len(sys.argv) > 1:
            self.repository = str(sys.argv[1])
            if len(sys.argv) > 2: self.folder = str(sys.argv[2])
            else: self.folder = self.repository 

    def print_info(self):
        print('\n\n\t\t\t\t\t[egit - EasyGiT]')
        print("\t\tfrom %r 's %r repo to %r folder\n\n" % (str(self.username), str(self.repository), str(self.folder)))

    def clone(self):
        os.system("git clone https://github.com/%r/%r %r" % (str(self.username), str(self.repository), str(self.folder)))

if sys.platform == 'linux' and \
    __name__ == '__main__':
        app = MainApplication()
        app.print_info()
        app.clone()
