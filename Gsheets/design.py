import gspread
from oauth2client.service_account import ServiceAccountCredentials
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.label import MDLabel
from kivy.animation import Animation
from kivy.core.window import Window
from pprint import pprint
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
Window.fullscreen = 'auto'

a = ''
b = ''


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

class HoverButton(MDRoundFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = (255/255, 152/255, 0/255, 255/255)
        self.text_color = (2/255, 0/255, 1/255, 1)


    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.bg_darkest
        self.text_color = (255/255, 152/255, 0/255, 255/255)


class MyApp(MDApp):
    def __init__(self):
        super().__init__()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Orange'

    def build(self):

        box = MDBoxLayout(orientation='vertical', spacing='16dp', adaptive_size=True,
                          pos_hint={"center_x": .5, "center_y": .5})
        btn1 = HoverButton(text='Понеділок', line_width=2, font_size=50, font_name='AA-Haymaker.ttf')
        btn1.bind(on_release=self.monday)
        btn2 = HoverButton(text='Вівторок', line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        btn2.bind(on_release=self.tuesday)
        btn3 = HoverButton(text='Середа', line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        btn4 = HoverButton(text='Четвер', line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        btn5 = HoverButton(text="П'ятниця", line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        btn6 = HoverButton(text='Субота', line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        box.add_widget(btn1)
        box.add_widget(btn2)
        box.add_widget(btn3)
        box.add_widget(btn4)
        box.add_widget(btn5)
        box.add_widget(btn6)
        self.sm = MDScreenManager()
        screen = MDScreen(name='m')
        screen.add_widget(box)
        self.sm.add_widget(screen)

        self.screen2 = MDScreen(name='s')
        self.box2 = MDBoxLayout(orientation='horizontal')
        self.lbox = MDBoxLayout(orientation='vertical')
        self.rbox = MDBoxLayout(orientation='vertical')
        self.box2.add_widget(self.lbox)
        self.box2.add_widget(self.rbox)
        self.screen2.add_widget(self.box2)
        self.sm.add_widget(self.screen2)


        self.final_screen = MDScreen(name='final')
        self.finalbox = MDBoxLayout()
        self.final_screen.add_widget(self.finalbox)
        self.sm.add_widget(self.final_screen)
        return self.sm

    def func(self, button):
        global a
        global b
        global loaded_hours
        if a == '' or a == button.text:
            a = button.text
        else:
            b = button.text
            loaded_hours[f'{a}///{b}'] = list(set(loaded_hours[a] + loaded_hours[b]))
            loaded_hours.pop(a)
            loaded_hours.pop(b)
            self.lbox.clear_widgets()
            self.rbox.clear_widgets()
            self.half_hour()

    def half_hour(self):
        global loaded_hours
        global a
        global b
        if len(loaded_hours) <= 7:
            self.final()
        else:
            a, b = '', ''

            for i in loaded_hours:
                btn = MDFlatButton(text=f'{i}',)
                btn.bind(on_release=self.func)

                lbl = MDLabel(text=f'{sorted([int(j) for j in loaded_hours[i]])}',
                            )
                self.lbox.add_widget(btn)
                self.rbox.add_widget(lbl)
                self.sm.current = 's'

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

    def tuesday(self, *args):
        global loaded_hours
        logoped = [''.join(i) for i in sheet.get('W3:W242')]
        for i in range(len(logoped)):
            if logoped[i] == 'в':
                try:
                    loaded_hours[names[i]] = [i for i in sheet.get(f'P{i + 4}:V{i + 4}')[0]]
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
                self.half_hour()
        else:
            self.final()


    def final(self):
        global final_dic
        global hours_priority
        global loaded_hours
        global free_hours

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


        true_final_dic = {}

        for i in final_dic:
            if '///' in i:
                true_final_dic[i.split('///')[0]] = final_dic[i] + '(30хв)'
                true_final_dic[i.split('///')[-1]] = final_dic[i][0:3:] + '30' + '(30хв)'
            else:
                true_final_dic[i] = final_dic[i]

        final_dic = true_final_dic


        data_table = MDDataTable(pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=False,
            column_data=[
                ('[color=#FF9800][size=25]Пацієнт[/size][/color]', dp(300)),
                ("[color=#FF9800][size=25]Час заняття[/size][/color]", dp(120)),
            ])





        str_f_l = ''
        for i in final_dic:
            str_f_l += f'{i}: {final_dic[i]}\n'

        for i in final_dic:
            data_table.add_row((f'[size=20]{i}[/size]', f'[size=20]{final_dic[i]}[/size]'))

        self.finalbox.add_widget(data_table)
        self.sm.current = 'final'
        return self.sm.current


if __name__ == '__main__':
    MyApp().run()

