import os
import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
def main():
    lnk=input('\n[?] Enter a web-link... > ')
    try:
        #lnk=str(lnk)
        page=requests.get(str(lnk))
        page_status = str(page.status_code)
        print('\n'+'[*] Status: '+page_status+'\n')
        print('[*] Encoding: ')
        print(page.encoding)
        print('\n')
        print('[*] JSON: ')
        print(page.json)
        print('\n')
        print('[*] Headers: ')
        print(page.headers)
        print('\n')
        print('[*] Json: ')
        print(page.json)
        print('\n')
        soup=BeautifulSoup(page.content, 'html.parser')
        print('[*] Content: ')
        print(soup)
        print('\n')
        def ask():
            ans=input('[?] Scrape another link? (y/n) > ')
            if ans == 'y':
                main()
            if ans == 'n':
                exit(0)
            elif ans != 'y' or ans != 'n':
                print('[!] Not a valid answer.\n')
                ask()
        ask()
    except MissingSchema:
        print('[!] Not a valid link. Please prepend "http://" or "https://", respectively.\n')
        main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[!] Ctrl+C Interrupt. Quitting!\n')
        quit(0)
