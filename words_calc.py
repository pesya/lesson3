#Научите бота выполнять основные арифметические действия с числами: сложение, вычитание, умножение и деление.
#Если боту сказать “2-3=”, он должен ответить “-1”. Все выражения для калькулятора должны заканчиваться знаком равно.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import re


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Hey, hooman! Type \"/calc сколько будет n плюс/минус/умножить/разделить m\" - and I\'ll count all the shit'
    print(text)
    update.message.reply_text(text)


def calc(bot, update):
    user_text = update.message.text
    user_text = user_text.split()
    words_to_digits = {'один': 1,
                       'два': 2,
                       'три': 3,
                       'четыре': 4,
                       'пять': 5,
                       'шесть': 6,
                       'семь': 7,
                       'восемь': 8,
                       'девять': 9,
                       'плюс': '+',
                       'минус': '-',
                       'умножить': '*',
                       'разделить': '/'}
    equasion = []
    for word in user_text:
        a = words_to_digits.get(word, 0)
        if a != 0:
            equasion.append(a)
    x = int(equasion[0])
    sign = equasion[1]
    y = int(equasion[2])
    if sign == '+':
        result = x + y
        print(result)
        return update.message.reply_text(result)
    elif sign == '-':
        result = x - y
        print(result)
        return update.message.reply_text(result)
    elif sign == '*':
        result = x * y
        print(result)
        return update.message.reply_text(result)
    elif sign == '/':
        try:
            result = x / y
            print(result)
            return update.message.reply_text(result)
        except ZeroDivisionError:
            print('Zero division')
            return update.message.reply_text('You can not divide by zero!')





def main():
    mybot = Updater("659806032:AAEzxPcmOtNRtawBl_maB_zF4Nzxpz_oGFQ", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("calc", calc))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
