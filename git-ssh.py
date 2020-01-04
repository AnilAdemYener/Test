#!/usr/bin/env python3
import os, sys

class App:
    def take_values(self):
        mail = input('==> enter your mail: ')
        cmd = 'ssh-keygen -t rsa -b 4096 -C "'+mail+'"'
        os.system(cmd)
    
    def check_sshagent(self):
        print('==> CHECK SSH AGENT')
        os.system('eval "$(ssh-agent -s)"')

    def add_ssh(self):
        print("==> ADDING SSH")
        os.system('ssh-add ~/.ssh/id_rsa')

    def print_pub(self):
        print("==> ID RSA PUB")
        os.system('cat ~/.ssh/id_rsa.pub')

    def check_git(self):
        print("==> CHECK GIT")
        os.system('ssh -T git@github.com')

    def main(self):
        self.take_values()
        self.check_sshagent()
        self.add_ssh()
        self.print_pub()
        self.check_git()

if sys.platform == 'linux' and __name__ == '__main__':
    app = App()
    app.main()
