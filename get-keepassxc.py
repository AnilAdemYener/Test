#!/usr/bin/env python3
import os, sys

passwd_download_url = 'https://drive.google.com/u/0/uc?id=1oLlH1hNfrDq6qRsAs4nOlLLvcHYDMaRI&export=download'

def main():
    if os.path.exists('/usr/bin/chromium'): os.system('chromium ' + passwd_download_url)
    else: print("couldn't find the chromium browser")

main()
