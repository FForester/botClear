import telebot
from telebot import types
import threading
import time

bot = telebot.TeleBot('1243149073:AAGj-V0O2ug103Rnb1LGezzyfNwHJEna5_Y')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "clear":
        bot.edit_message_text(
            call.message.text + "\nПодтвердил: " + call.from_user.first_name + " " + call.from_user.last_name,
            773344235, call.message.id)

def thread_function(name):
    status = True
    while True:
        arrTime = [9, 11, 14, 15, 17, 19]
        result = time.gmtime(time.time())
        if (result.tm_wday < 5 and (result.tm_hour in arrTime) and result.tm_min < 1 and status):
            status = False
            keyboard = types.InlineKeyboardMarkup()
            key_ok = types.InlineKeyboardButton(text='❌', callback_data='clear')
            keyboard.add(key_ok)
            bot.send_message(773344235, text='Уборка в '+str(result.tm_hour)+':00', reply_markup=keyboard)
        if not (result.tm_hour in arrTime):
            status = True

if __name__ == '__main__':
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    print(time.time())
    bot.polling()








