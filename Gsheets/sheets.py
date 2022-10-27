import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Plakhta').sheet1


loaded_hours = {}
names = [''.join(i) for i in sheet.get('B3:B242')]


logoped = [''.join(i) for i in sheet.get('M3:M242')]

for i in range(len(logoped)):
    if logoped[i] == 'в':
        loaded_hours[names[i]] = [i[0:2:].lstrip('0') for i in sheet.get(f'F{i+4}:L{i+4}')[0] if i != '']

free_hours = {}
sample = ['9', '10', '11', '12', '14', '15', '16']

for i in loaded_hours:
    free_hours[i] = [j for j in sample if j not in loaded_hours[i]]

pprint(free_hours)

hours_priority = {'9': 0,
                  '10': 0,
                  '11': 0,
                  '12': 0,
                  '14': 0,
                  '15': 0,
                  '16': 0}

for i in hours_priority:
    for j in free_hours:
        if i in free_hours[j]:
            hours_priority[i] += 1

def sort_hours_priority(time):
    d = {}
    s = sorted(time.items(), key=lambda x: x[1])
    for i in range(len(s)):
        d[s[i][0]] = s[i][-1]
    return d


final_dic = {}

for i in free_hours:
    if list(hours_priority)[0] in free_hours[i]:
        final_dic[i] = list(hours_priority)[0]
        free_hours[i].remove(list(hours_priority)[0])
        hours_priority.pop(list(hours_priority)[0])
        for j in free_hours[i]:
            hours_priority[j] -= 1
        hours_priority = sort_hours_priority(hours_priority)

print(final_dic)


