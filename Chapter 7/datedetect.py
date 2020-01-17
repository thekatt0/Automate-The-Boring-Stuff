#! python3
#datedetect.py - Finds dates from the clipboard


import re

text = '''Speaking of dates did you know 02/14/2020 is Valentine's Day? I really didn't know. The more you learn the the more you know. When I was born on that dark day 9/1/1989 I don't know if it was dark. The moon was new. The weather was normal california weather. And then in 10/01/2019 it was Halloween!'''

matches = []
monthRegex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{2,4})')

for groups in monthRegex.findall(text):
    dates = '-'.join([groups[0],groups[1],groups[2]])
    matches.append(dates)

month = groups[0]
day = groups[1]
year = groups[2]


print(matches)