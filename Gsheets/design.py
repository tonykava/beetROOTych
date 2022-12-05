from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from kivy.uix.label import Label


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sh = client.open('Plakhta')
sheet = sh.get_worksheet(0)
names = [''.join(i) for i in sheet.get('B3:B242')]
hours_priority = {'9': 0,
                      '10': 0,
                      '11': 0,
                      '12': 0,
                      '14': 0,
                      '15': 0,
                      '16': 0}
pool_hours = {'9:30': ['9', '10'],
                  '10:30': ['10', '11'],
                  '11:15': ['11', '12'],
                  '14:45': ['14', '15'],
                  '15:30': ['15', '16'],
                  '16:15': ['16']}
final_dic = {}
loaded_hours = {}
true_loaded_hours = {}
free_hours = {}
sample = ['9', '10', '11', '12', '14', '15', '16']


class MyApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        box = BoxLayout(orientation='vertical', spacing=10)
        btn1 = Button(text='Понеділок',
                      font_size=50,
                      size_hint=(.6, .6),
                      pos_hint={'x': .2, 'y': .2},
                      padding_x=100)
        btn1.bind(on_press=self.monday)
        btn2 = Button(text='Вівторок',
                      font_size=50,
                      size_hint=(.6, .6),
                      pos_hint={'x': .2, 'y': .2},
                      padding_x=100)
        btn3 = Button(text='Середа',
                      font_size=50,
                      size_hint=(.6, .6),
                      pos_hint={'x': .2, 'y': .2},
                      padding_x=100)
        btn4 = Button(text='Четвер',
                      font_size=50,
                      size_hint=(.6, .6),
                      pos_hint={'x': .2, 'y': .2},
                      padding_x=100)
        btn5 = Button(text="П'ятниця",
                      font_size=50,
                      size_hint=(.6, .6),
                      pos_hint={'x': .2, 'y': .2},
                      padding_x=100)
        btn6 = Button(text='Субота',
                      font_size=50,
                      size_hint=(.6, .6),
                      pos_hint={'x': .2, 'y': .2},
                      padding_x=100)
        box.add_widget(btn1)
        box.add_widget(btn2)
        box.add_widget(btn3)
        box.add_widget(btn4)
        box.add_widget(btn5)
        box.add_widget(btn6)
        self.sm = ScreenManager()
        screen = Screen()
        screen.add_widget(box)
        self.sm.add_widget(screen)
        return self.sm

    def half_hour(self):
        global loaded_hours


        pprint(loaded_hours)
        a = input('First: ')
        b = input('Second: ')
        loaded_hours[f'{a} {b}'] = list(set(loaded_hours[a] + loaded_hours[b]))
        loaded_hours.pop(a)
        loaded_hours.pop(b)
        s = Screen(name='s')
        self.sm.add_widget(s)
        self.sm.current = 's'
        return self.sm

    def sort_hours_priority(self, time):
        d = {}
        s = sorted(time.items(), key=lambda x: x[1])
        for i in range(len(s)):
            d[s[i][0]] = s[i][-1]
        return d


    def monday(self, *args):
        global loaded_hours
        logoped = [''.join(i) for i in sheet.get('M3:M242')]
        for i in range(len(logoped)):
            if logoped[i] == 'в':
                try:
                    loaded_hours[names[i]] = [i for i in sheet.get(f'F{i + 4}:L{i + 4}')[0]]
                except IndexError:
                    loaded_hours[names[i]] = ['NO']
        self.general()

    def general(self):
        global hours_priority
        global loaded_hours
        for i in loaded_hours:
            if loaded_hours[i][0] in pool_hours:
                loaded_hours[i] += pool_hours[loaded_hours[i][0]]
                loaded_hours[i].pop(0)

        for i in loaded_hours:
            true_loaded_hours[i] = [j[0:2:].lstrip('0') for j in loaded_hours[i] if j != '']
        loaded_hours = true_loaded_hours

        if len(loaded_hours) > 7:
            for i in range(len(loaded_hours) - 7):
                self.half_hour()

        for i in loaded_hours:
            free_hours[i] = [j for j in sample if j not in loaded_hours[i]]

        for i in hours_priority:
            for j in free_hours:
                if i in free_hours[j]:
                    hours_priority[i] += 1

        while free_hours != {}:
            for i in free_hours:
                if list(hours_priority)[0] in free_hours[i]:
                    final_dic[i] = list(hours_priority)[0]
                    for j in free_hours[i]:
                        if j in hours_priority:
                            hours_priority[j] -= 1
                    hours_priority.pop(list(hours_priority)[0])
                    hours_priority = self.sort_hours_priority(hours_priority)
            for i in final_dic:
                if i in free_hours:
                    free_hours.pop(i)

        for i in final_dic:
            final_dic[i] += ':00'

        pprint(final_dic)







if __name__ == '__main__':
    MyApp().run()

