#!/usr/bin/env python3
import os, sys

def print_err(msg=None):
    print('\t\t[egit ERR_!]')
    if msg != None: print('==> %r' % msg)
    else: print('\tan error occured')

class MainApplication:
    username = 'lovisestdeus'
    repository = None
    folder = None
    method = 'https' 
    def __init__(self):
        if len(sys.argv) > 1:
            self.repository = str(sys.argv[1])
            if len(sys.argv) > 2:
                if sys.argv[2] == 'ssh' or sys.argv[2] == 'https': 
                    if sys.argv[2] == 'https': self.method = 'https'
                    elif sys.argv[2] == 'ssh': self.method = 'ssh'
                    self.folder = self.repository
                else: self.folder = str(sys.argv[2])
                if len(sys.argv) > 3:
                    if sys.argv[3] == 'https': self.method = 'https'
                    elif sys.argv[3] == 'ssh': self.method = 'ssh'
            else: self.folder = self.repository 

    def print_info(self):
        print('\n\n\t\t\t[egit - EasyGiT]')
        print("\t\t[Method: %r] from %r 's %r repo to %r folder\n\n" % (str(self.method.upper()), str(self.username), str(self.repository), str(self.folder)))

    def clone(self):
        if self.method == 'https':
            os.system("git clone https://github.com/%r/%r %r" % (str(self.username), str(self.repository), str(self.folder)))
        if self.method == 'ssh':
            os.system("git clone git@github.com:%r/%r %r" % (str(self.username), str(self.repository), str(self.folder)))

if sys.platform == 'linux' and \
    __name__ == '__main__':
        app = MainApplication()
        if app.repository == None: print_err("you didn't enter the repo's name")
        else:
            app.print_info()
            app.clone()
