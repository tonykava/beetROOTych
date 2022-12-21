import logging
from aiogram import Bot, Dispatcher, executor, types
from pprint import pprint
from aiogram.dispatcher.filters import Text
import gspread
from oauth2client.service_account import ServiceAccountCredentials

API_token = '5825484965:AAHZZSDwXy0eOI2_1lK8Uanck6zmZhvkc0A'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_token)
dp = Dispatcher(bot)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sh = client.open('Plakhta')
sheet = sh.get_worksheet(0)
current_day = ''
a = ''
b = ''

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
backup_loaded_hours = {}
names = [''.join(i) for i in sheet.get('B3:B242')]
chat_id = ''
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    global scope, creds, client, sh, sheet, current_day, a, b, hours_priority, pool_hours, final_dic, loaded_hours, true_loaded_hours, free_hours, sample, backup_loaded_hours, names

    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    client = gspread.authorize(creds)
    sh = client.open('Plakhta')
    sheet = sh.get_worksheet(0)
    current_day = ''
    a = ''
    b = ''

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
    backup_loaded_hours = {}
    names = [''.join(i) for i in sheet.get('B3:B242')]

    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Понеділок', callback_data='Monday')
    btn2 = types.InlineKeyboardButton(text='Вівторок', callback_data='Tuesday')
    btn3 = types.InlineKeyboardButton(text='Середа', callback_data='Wednesday')
    btn4 = types.InlineKeyboardButton(text='Четвер', callback_data='Thursday')
    btn5 = types.InlineKeyboardButton(text="П'ятниця", callback_data='Friday')
    btn6 = types.InlineKeyboardButton(text='Субота', callback_data='Saturday')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    await message.reply(text='Обери день тижня:', reply_markup=markup)

@dp.callback_query_handler()
async def monday_callback(call):
    global scope, creds, client, sh, sheet, current_day, a, b, hours_priority, pool_hours, final_dic, loaded_hours, true_loaded_hours, free_hours, sample, backup_loaded_hours, names
    if call.data == 'Monday':
        monday()
        general()
        if len(loaded_hours) > 7:
            await half_hour(call)
            return
        else:
            await final()
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text='Завантажити графік у плахту', callback_data='suka')
            btn2 = types.InlineKeyboardButton(text='Створити графік на іший день', callback_data='suka')
            markup.add(btn1, btn2)

            str_final_dict = 'Графік на понеділок:\n\n'
            for i in final_dic:
                str_final_dict += f'{i}:   {final_dic[i]}\n'
            await bot.send_message(call.message.chat.id, text=str_final_dict, reply_markup=markup)
            return
    # обробка запиту із розподілу по півгодини
    elif call.data in loaded_hours:
        if a == '' or a == call.data:
            a = call.data
        else:
            b = call.data
            loaded_hours[f'{a}///{b}'] = list(set(loaded_hours[a] + loaded_hours[b]))
            loaded_hours.pop(a)
            loaded_hours.pop(b)
            if len(loaded_hours) > 7:
                await half_hour(call)
            else:
                await final()
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton(text='Завантажити графік у плахту', callback_data='push')
                btn2 = types.InlineKeyboardButton(text='Створити графік на іший день', callback_data='new')
                markup.add(btn1, btn2)

                str_final_dict = 'Графік на понеділок:\n\n'
                for i in final_dic:
                    str_final_dict += f'{i}:   {final_dic[i]}\n'
                await bot.send_message(call.message.chat.id, text=str_final_dict, reply_markup=markup)
                return
    # обробка пушу
    elif call.data == 'push':
        if current_day == 'Monday':
            for i in range(len(names)):
                if names[i] in final_dic:
                    sheet.update(f'M{i + 4}', final_dic[names[i]])
        await bot.send_message(call.message.chat.id, text='Графік успішно завантажено=)')

    #новий графік
    elif call.data == 'new':
        current_day = ''
        a = ''
        b = ''

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
        backup_loaded_hours = {}

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Понеділок', callback_data='Monday')
        btn2 = types.InlineKeyboardButton(text='Вівторок', callback_data='Tuesday')
        btn3 = types.InlineKeyboardButton(text='Середа', callback_data='Wednesday')
        btn4 = types.InlineKeyboardButton(text='Четвер', callback_data='Thursday')
        btn5 = types.InlineKeyboardButton(text="П'ятниця", callback_data='Friday')
        btn6 = types.InlineKeyboardButton(text='Субота', callback_data='Saturday')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        await bot.send_message(call.message.chat.id, text='Обери день тижня:', reply_markup=markup)

async def half_hour(call):
    global a
    global b
    a = ''
    b = ''
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i in loaded_hours:
        btn = types.InlineKeyboardButton(text=f'{i}:   {sorted(loaded_hours[i])}', callback_data=i)
        markup.add(btn)
    await bot.send_message(call.message.chat.id, "Обери в кого заняття будуть по півгодини:", reply_markup=markup)

def monday():
    global current_day
    global loaded_hours
    global names
    global sheet
    logoped = [''.join(i) for i in sheet.get('M3:M242')]
    for i in range(len(logoped)):
        if logoped[i] == 'в':
            try:
                loaded_hours[names[i].split(' ')[0] + ' ' + names[i].split(' ')[1][0]] = [i for i in sheet.get(f'F{i + 4}:L{i + 4}')[0]]
            except IndexError:
                loaded_hours[names[i]] = ['NO']
    current_day = 'Monday'

def general():
    global hours_priority
    global loaded_hours
    global backup_loaded_hours
    for i in loaded_hours:
        if loaded_hours[i][0] in pool_hours:
            loaded_hours[i] += pool_hours[loaded_hours[i][0]]
            loaded_hours[i].pop(0)

    for i in loaded_hours:
        true_loaded_hours[i] = [j[0:2:].lstrip('0') for j in loaded_hours[i] if j != '']
    loaded_hours = true_loaded_hours

async def final():
    global chat_id
    global final_dic
    global hours_priority
    global loaded_hours
    global free_hours
    global backup_loaded_hours
    for i in loaded_hours:
        free_hours[i] = [j for j in sample if j not in loaded_hours[i]]

    for i in hours_priority:
        for j in free_hours:
            if i in free_hours[j]:
                hours_priority[i] += 1


    true_hours_priority = {}
    for i in hours_priority:
        if hours_priority[i] != 0:
            true_hours_priority[i] = hours_priority[i]
    hours_priority = true_hours_priority


    counter = 0
    while free_hours != {}:
        if counter >= 30:
            break
        for i in free_hours:
            if list(hours_priority)[0] in free_hours[i]:
                final_dic[i] = list(hours_priority)[0]
                for j in free_hours[i]:
                    if j in hours_priority:
                        hours_priority[j] -= 1
                hours_priority.pop(list(hours_priority)[0])
                hours_priority = sort_hours_priority(hours_priority)
        for i in final_dic:
            if i in free_hours:
                free_hours.pop(i)
        counter += 1






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

    HUY = {}
    for i in final_dic:
        for j in names:
            if i in j:
                HUY[j] = final_dic[i]

    final_dic = HUY

def sort_hours_priority(time):
    d = {}
    s = sorted(time.items(), key=lambda x: x[1])
    for i in range(len(s)):
        d[s[i][0]] = s[i][-1]
    return d

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

