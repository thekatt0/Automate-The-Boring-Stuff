#! python3
#datedetect.py - Finds dates from the clipboard


import re

text = '''Speaking of dates did you know 02/14/2020 is Valentine's Day? I really didn't know. The more you learn the the more you know. When I was born on that dark day 9/1/1989 I don't know if it was dark. The moon was new. The weather was normal california weather. And then in 10/01/2019 it was Halloween!'''

#empty lists
matches = []
months = []
days = []
years = []

#compiler
monthRegex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{2,4})')

#formating and appending lists
for groups in monthRegex.findall(text):
    months.append(groups[0])
    dates = '-'.join([groups[0],groups[1],groups[2]])
    matches.append(dates)


#print
print(months)