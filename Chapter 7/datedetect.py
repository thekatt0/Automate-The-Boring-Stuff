#! python3
#datedetect.py - Finds dates from the clipboard


import re
import pyperclip

text = '''Speaking of dates did you know 32/14/2020 is Valentine's Day? I really didn't know. The more you learn the the more you know. When I was born on that dark day 1/9/1989 I don't know if it was dark. The moon was new. The weather was normal california weather. And then in 10/01/2019 it was Halloween!'''

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

