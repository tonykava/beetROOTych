import gspread
from oauth2client.service_account import ServiceAccountCredentials
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
Window.fullscreen = 'auto'
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
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
my_loaded_hours = {}
true_loaded_hours = []


class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        box = MDBoxLayout(orientation='vertical', spacing='16dp', adaptive_size=True,
                          pos_hint={"center_x": .5, "center_y": .5})
        btn1 = MDRoundFlatButton(text='Понеділок', line_width=2, font_size=50, font_name='AA-Haymaker.ttf')
        btn2 = MDRoundFlatButton(text='Вівторок', line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        btn3 = MDRoundFlatButton(text='Середа', line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        btn4 = MDRoundFlatButton(text='Четвер', line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        btn5 = MDRoundFlatButton(text="П'ятниця", line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        btn6 = MDRoundFlatButton(text='Субота', line_width=2, font_size=50, pos_hint={"center_x": .5, "center_y": .5}, font_name='AA-Haymaker.ttf')
        box.add_widget(btn1)
        box.add_widget(btn2)
        box.add_widget(btn3)
        box.add_widget(btn4)
        box.add_widget(btn5)
        box.add_widget(btn6)


        return box


MyApp().run()