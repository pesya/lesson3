#Установите модуль ephem
#Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /ephem Mars
#В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
#При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime
from api_key import get_key


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Hi! Give me a date - and I\'ll tell when the nearest full moon is '
    print(text)
    update.message.reply_text(text)


def full_moon(bot, update):
    user_text = update.message.text
    user_text = user_text.split()
    date = 0
    for word in user_text:
        try:
            date = datetime.datetime.strptime(word, "%Y-%m-%d")
        except ValueError:
            print(word, 'not a date')
    if date != 0:
        answer = ephem.next_full_moon(date)
        update.message.reply_text('The nearest full moon is at {}'.format(answer))
    else:
        update.message.reply_text('Please give me a valid date')


def main():
    mybot = Updater(get_key(), request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("date", full_moon))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
