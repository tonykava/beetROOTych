import gspread
from oauth2client.service_account import ServiceAccountCredentials
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton, MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.metrics import sp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

Window.fullscreen = 'auto'

current_day = ''
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

class Final_screen_HoverButton(MDRaisedButton, HoverBehavior):
    def on_enter(self, *args):
        self.text_color = 'orange'
        self.md_bg_color = 'black'
        self.line_color = 'orange'

    def on_leave(self, *args):
        self.text_color = 'black'
        self.md_bg_color = 'orange'
        self.line_color = 'black'

class HoverButton(MDRoundFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = (255/255, 152/255, 0/255, 255/255)
        self.text_color = (2/255, 0/255, 1/255, 1)
        self.font_size = 60

    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.bg_darkest
        self.text_color = (255/255, 152/255, 0/255, 255/255)
        self.font_size = 50


class HoverButton1(MDRoundFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = (0/255, 128/255, 0/255, 255/255)
        self.font_size = 60

    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.bg_darkest
        self.font_size = 50


class HoverButton2(MDRoundFlatButton, HoverBehavior):
    def on_enter(self, *args):
        self.md_bg_color = (255/255, 0/255, 0/255, 255/255)
        self.font_size = 60

    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.bg_darkest
        self.font_size = 50

class MyApp(MDApp):
    def __init__(self):
        super().__init__()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Orange'
        self.sm = MDScreenManager()



        #описуємо стартовий екран

        start_screen = MDScreen(name='start_screen')
        start_screen_layout = MDFloatLayout()
        start_screen_lbl = MDFlatButton(
            text='Привіт!\n\n Я твій персональний помічник,\n для створення графіку роботи.\n\n Почнемо складати графіки?',
            halign='center', pos_hint={"center_x": 0.5, "center_y": 0.7},
            font_name='AA-Haymaker', text_color='orange'
            )
        start_screen_lbl.font_size = '60px'
        start_screen_layout.add_widget(start_screen_lbl)

        start_screen_button_box = MDBoxLayout(
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )

        btn1 = HoverButton1(text='Вйо до роботи!', font_size=50, line_color='green', font_name='AA-Haymaker.ttf',
                            text_color='white', line_width=2)
        btn1.bind(on_release=self.start)
        btn2 = HoverButton2(text='Жуй сраку', font_size=50, line_color='red', font_name='AA-Haymaker.ttf',
                            text_color='white', line_width=2)
        btn2.bind(on_release=self.close_application)
        start_screen_button_box.add_widget(btn1)
        start_screen_button_box.add_widget(btn2)
        start_screen_layout.add_widget(start_screen_button_box)
        start_screen.add_widget(start_screen_layout)
        self.sm.add_widget(start_screen)

        #описуємо екран вибору днів тижня

        day_selection_screen = MDScreen(name='day_selection_screen')
        day_selection_layout = MDFloatLayout()
        day_selection_lbl = MDFlatButton(text='Обери день будь ласка:', font_size=60, font_name='AA-Haymaker.ttf', pos_hint={"center_x": 0.5, "center_y": 0.8})
        day_selection_button_box = MDBoxLayout(orientation='vertical', spacing='16dp', adaptive_size=True,
                          pos_hint={"center_x": .5, "center_y": .5})
        day_selection_btn1 = HoverButton(text='Понеділок', line_width=2, font_size=50, font_name='AA-Haymaker.ttf', pos_hint={"center_x": .5, "center_y": .5})
        day_selection_btn1.bind(on_release=self.monday)
        day_selection_btn2 = HoverButton(text='Вівторок', line_width=2, font_size=50, font_name='AA-Haymaker.ttf', pos_hint={"center_x": .5, "center_y": .5})
        day_selection_btn2.bind(on_release=self.tuesday)
        day_selection_btn3 = HoverButton(text='Середа', line_width=2, font_size=50, font_name='AA-Haymaker.ttf', pos_hint={"center_x": .5, "center_y": .5})
        day_selection_btn3.bind(on_release=self.wednesday)
        day_selection_btn4 = HoverButton(text='Четвер', line_width=2, font_size=50, font_name='AA-Haymaker.ttf', pos_hint={"center_x": .5, "center_y": .5})
        day_selection_btn4.bind(on_release=self.thursday)
        day_selection_btn5 = HoverButton(text="П'ятниця", line_width=2, font_size=50, font_name='AA-Haymaker.ttf', pos_hint={"center_x": .5, "center_y": .5})
        day_selection_btn5.bind(on_release=self.friday)
        day_selection_btn6 = HoverButton(text='Субота', line_width=2, font_size=50, font_name='AA-Haymaker.ttf', pos_hint={"center_x": .5, "center_y": .5})
        day_selection_btn6.bind(on_release=self.saturday)

        day_selection_button_box.add_widget(day_selection_btn1)
        day_selection_button_box.add_widget(day_selection_btn2)
        day_selection_button_box.add_widget(day_selection_btn3)
        day_selection_button_box.add_widget(day_selection_btn4)
        day_selection_button_box.add_widget(day_selection_btn5)
        day_selection_button_box.add_widget(day_selection_btn6)

        day_selection_layout.add_widget(day_selection_button_box)
        day_selection_layout.add_widget(day_selection_lbl)
        day_selection_screen.add_widget(day_selection_layout)
        self.sm.add_widget(day_selection_screen)

        #описуємо екран з фінальним графіком

        self.final_screen = MDScreen(name='final_screen')
        self.final_layout = MDFloatLayout()
        self.final_data_table = MDDataTable(pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            rows_num=20,
            use_pagination=False,
            column_data=[
                ('[color=#FF9800][size=25]Пацієнт[/size][/color]', sp(250)),
                ("[color=#FF9800][size=25]Час заняття[/size][/color]", sp(120)),
            ])
        self.final_screen_box_button = MDBoxLayout(pos_hint={"center_x": 0.5, 'center_y': 0.15},
            adaptive_size=True,
            spacing="24dp",)
        final_screen_btn1 = Final_screen_HoverButton(text='Скласти ще один графік', font_size=20, on_release=self.one_more_time)
        final_screen_btn2 = Final_screen_HoverButton(text='Закінчити роботу', font_size=20, on_release=self.close_application)
        final_screen_btn3 = Final_screen_HoverButton(text='Записати графік у плахту', font_size=20, on_release=self.push)
        self.final_screen_box_button.add_widget(final_screen_btn1)
        self.final_screen_box_button.add_widget(final_screen_btn2)
        self.final_screen_box_button.add_widget(final_screen_btn3)
        self.final_layout.add_widget(self.final_screen_box_button)
        self.final_layout.add_widget(self.final_data_table)
        self.final_screen.add_widget(self.final_layout)
        self.sm.add_widget(self.final_screen)

        # описуємо екран вибору в кого заняття буде по півгодини

        self.half_hour_screen = MDScreen(name='half_hour_screen')
        self.half_hour_layout = MDFloatLayout()
        self.half_hour_data_table = MDDataTable(pos_hint={"center_y": 0.5, "center_x": 0.5},
                                     size_hint=(0.9, 0.6),
                                     rows_num=20,
                                     use_pagination=False,
                                     column_data=[
                                         ('[color=#FF9800][size=25]Пацієнт[/size][/color]', sp(250)),
                                         ("[color=#FF9800][size=25]Зайняті години[/size][/color]", sp(120)),
                                     ])
        self.half_hour_data_table.bind(on_row_press=self.func)

        self.half_hour_layout.add_widget(self.half_hour_data_table)
        self.half_hour_screen.add_widget(self.half_hour_layout)
        self.sm.add_widget(self.half_hour_screen)


    def build(self, *args):
        self.sm.current = 'start_screen'
        return self.sm

    def start(self, *args):
        self.sm.current = 'day_selection_screen'
        return self.sm

    def close_application(self, *args):
        MyApp.get_running_app().stop()
        Window.close()

    def one_more_time(self, *args):
        global hours_priority, final_dic, loaded_hours, true_loaded_hours, free_hours, sample, current_day
        for i in range(len(final_dic)):
            self.final_data_table.remove_row(self.final_data_table.row_data[-1])
        current_day = ''
        hours_priority = {'9': 0,
                          '10': 0,
                          '11': 0,
                          '12': 0,
                          '14': 0,
                          '15': 0,
                          '16': 0}
        final_dic = {}
        loaded_hours = {}
        true_loaded_hours = {}
        free_hours = {}
        sample = ['9', '10', '11', '12', '14', '15', '16']
        self.sm.current = 'day_selection_screen'
        return self.sm



    def func(self, instance_table, instance_row):
        global a
        global b
        global loaded_hours
        if a == '' or a == instance_row.text[9:-7:]:
            a = instance_row.text[9:-7:]
        else:
            b = instance_row.text[9:-7:]
            loaded_hours[f'{a}///{b}'] = list(set(loaded_hours[a] + loaded_hours[b]))
            loaded_hours.pop(a)
            loaded_hours.pop(b)
            for i in range(len(loaded_hours) + 1):
                self.half_hour_data_table.remove_row(self.half_hour_data_table.row_data[-1])
            self.half_hour()

    def monday(self, *args):
        global current_day
        global loaded_hours
        logoped = [''.join(i) for i in sheet.get('M3:M242')]
        monday_logoped = logoped
        for i in range(len(logoped)):
            if logoped[i] == 'в':
                try:
                    loaded_hours[names[i]] = [i for i in sheet.get(f'F{i + 4}:L{i + 4}')[0]]
                except IndexError:
                    loaded_hours[names[i]] = ['NO']
        current_day = 'monday'
        self.general()

    def tuesday(self, *args):
        global loaded_hours
        global current_day
        logoped = [''.join(i) for i in sheet.get('W3:W242')]
        for i in range(len(logoped)):
            if logoped[i] == 'в':
                try:
                    loaded_hours[names[i]] = [i for i in sheet.get(f'P{i + 4}:V{i + 4}')[0]]
                except IndexError:
                    loaded_hours[names[i]] = ['NO']
        current_day = 'tuesday'
        self.general()

    def wednesday(self, *args):
        global loaded_hours
        global current_day
        logoped = [''.join(i) for i in sheet.get('AF3:AF242')]
        for i in range(len(logoped)):
            if logoped[i] == 'в':
                try:
                    loaded_hours[names[i]] = [i for i in sheet.get(f'Y{i + 4}:AE{i + 4}')[0]]
                except IndexError:
                    loaded_hours[names[i]] = ['NO']
        current_day = 'wednesday'
        self.general()

    def thursday(self, *args):
        global loaded_hours
        logoped = [''.join(i) for i in sheet.get('AO3:AO242')]
        for i in range(len(logoped)):
            if logoped[i] == 'в':
                try:
                    loaded_hours[names[i]] = [i for i in sheet.get(f'AI{i + 4}:AN{i + 4}')[0]]
                except IndexError:
                    loaded_hours[names[i]] = ['NO']
        current_day = 'thursday'
        self.general()

    def friday(self, *args):
        global loaded_hours
        logoped = [''.join(i) for i in sheet.get('AX3:AX242')]
        for i in range(len(logoped)):
            if logoped[i] == 'в':
                try:
                    loaded_hours[names[i]] = [i for i in sheet.get(f'AQ{i + 4}:AW{i + 4}')[0]]
                except IndexError:
                    loaded_hours[names[i]] = ['NO']
        current_day = 'friday'
        self.general()

    def saturday(self, *args):
        global loaded_hours
        logoped = [''.join(i) for i in sheet.get('BG3:BG242')]
        for i in range(len(logoped)):
            if logoped[i] == 'в':
                try:
                    loaded_hours[names[i]] = [i for i in sheet.get(f'AZ{i + 4}:BF{i + 4}')[0]]
                except IndexError:
                    loaded_hours[names[i]] = ['NO']
        current_day = 'saturday'
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

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)


    def push(self, *args):
        global current_day
        if current_day == 'monday':
            for i in range(len(names)):
                if names[i] in final_dic:
                    sheet.update(f'M{i + 4}', final_dic[names[i]])
        if current_day == 'tuesday':
            for i in range(len(names)):
                if names[i] in final_dic:
                    sheet.update(f'W{i + 4}', final_dic[names[i]])
        if current_day == 'wednesday':
            for i in range(len(names)):
                if names[i] in final_dic:
                    sheet.update(f'AF{i + 4}', final_dic[names[i]])
        if current_day == 'thursday':
            for i in range(len(names)):
                if names[i] in final_dic:
                    sheet.update(f'AO{i + 4}', final_dic[names[i]])
        if current_day == 'friday':
            for i in range(len(names)):
                if names[i] in final_dic:
                    sheet.update(f'AX{i + 4}', final_dic[names[i]])
        if current_day == 'saturday':
            for i in range(len(names)):
                if names[i] in final_dic:
                    sheet.update(f'BG{i + 4}', final_dic[names[i]])
        self.dialog = MDDialog(title='Графік успішно внесено до плахти',
                               size_hint=(0.4, 0.3),
                               buttons=[Final_screen_HoverButton(text='OK', on_release=self.dialog_close, font_size=20)])
        self.dialog.open()

    def half_hour(self):
        global loaded_hours
        global a
        global b

        if len(loaded_hours) <= 7:
            self.final()
        else:
            a, b = '', ''
            for i in loaded_hours:
                data = ', '.join(sorted([f'{j}' for j in loaded_hours[i]]))
                self.half_hour_data_table.add_row((f'[size=20]{i}[/size]', f'[size=20]{data}[/size]'))
            self.sm.current = 'half_hour_screen'
            return self.sm

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
        for i in final_dic:
            self.final_data_table.add_row((f'[size=20]{i}[/size]', f'[size=20]{final_dic[i]}[/size]'))
        self.sm.current = 'final_screen'

        return self.sm

    def sort_hours_priority(self, time):
        d = {}
        s = sorted(time.items(), key=lambda x: x[1])
        for i in range(len(s)):
            d[s[i][0]] = s[i][-1]
        return d


#try:
MyApp().run()
#except:
    #google.auth.exceptions.TransportError('NO INTERNET')
    #print('NO INTERNET')

