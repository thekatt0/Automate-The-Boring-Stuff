#! python3
#datedetect.py - Finds dates from the clipboard


import re
import pyperclip

text = str(pyperclip.paste()) 

#empty lists
matches = []
months = []
days = []
years = []

#compiler
dateRegex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{2,4})')

monthRegex = re.compile(r'0[1-9]|1[0-9]|2[0-9]|3[0-1]')

#formating and appending lists


for groups in dateRegex.findall(text):

    dates = '-'.join([groups[0],groups[1],groups[2]])
    matches.append(dates)


if len(matches) > 0:
    pyperclip.copy('n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No dates found.')

