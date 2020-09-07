import urllib.request
import telebot
bot = telebot.TeleBot('1385601995:AAH8COBe14U67_m6lbSaFa0v1VHdw7wL0Ew')


aa = 'Основные http статусы:\n200 - всё хорошо\n4XX - сайт не найден\n5ХХ - сайт перегружен, но работает'



vk = urllib.request.urlopen("http://vk.com").getcode()
vk = str(vk)
sendvk = 'vk.com - ' + vk;

tg = urllib.request.urlopen("http://t.me").getcode()
tg = str(tg)
sendtg = 't.me - ' + tg;

ya = urllib.request.urlopen("http://yandex.by").getcode()
ya = str(ya)
sendya = 'yandex.by - ' + ya;

tut = urllib.request.urlopen("http://tut.by").getcode()
tut = str(tut)
sendtut = 'tut.by - ' + tut;

onliner = urllib.request.urlopen("http://onliner.by").getcode()
onliner = str(onliner)
sendonliner = 'onliner.by - ' + onliner

gg = urllib.request.urlopen("http://google.com").getcode()
gg = str(gg)
sendgg = 'google.com - ' + gg;

#print(urllib.request.urlopen("http://nn.by").getcode())

keyboard0 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard0.row('check')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start, используйте клавиатуру ниже', reply_markup=keyboard0)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'check':
        bot.send_message(message.chat.id, aa)
        bot.send_message(message.chat.id, 'Вот http статусы следующих сайтов:')
        bot.send_message(message.chat.id, sendgg)
        bot.send_message(message.chat.id, sendtut)
        bot.send_message(message.chat.id, sendonliner)
        bot.send_message(message.chat.id, sendya)
        bot.send_message(message.chat.id, sendvk)
        bot.send_message(message.chat.id, sendtg)




bot.polling(none_stop=True, interval=0)
bot.polling()
