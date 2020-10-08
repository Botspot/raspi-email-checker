#!/usr/bin/env python

from imapclient import IMAPClient
import time
import os

DEBUG = True

HOSTNAME = 'hostname2replace'
#Hostmane is the website to check to connect to.
#For Outlook, it is outlook.office365.com
#For Gmail, it is imap.gmail.com
USERNAME = 'email2replace'
PASSWORD = 'password2replace'
MAILBOX = 'mailbox2replace' #folder you want this script checking

NEWMAIL_OFFSET = 0   # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = checkinterval2replace # check mail every 60 seconds

def loop():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    if DEBUG:
        print('Logging in as ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    newmails = int(folder_status['UNSEEN'])

    if DEBUG:
        print "You have", newmails, "new emails!"

    if newmails > NEWMAIL_OFFSET:
        os.system('sudo -u pi zenity --info --text="You just received an email." --icon-name=emblem-mail --no-wrap')

if __name__ == '__main__':
    print'Press Ctrl-C to quit.'
    #os.system('zenity --info --text="checkmail.py initialized" --no-wrap')
    while True:
        try:
            loop()
        except:
            pass
        time.sleep(MAIL_CHECK_FREQ)
