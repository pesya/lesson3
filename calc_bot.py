#Научите бота выполнять основные арифметические действия с числами: сложение, вычитание, умножение и деление.
#Если боту сказать “2-3=”, он должен ответить “-1”. Все выражения для калькулятора должны заканчиваться знаком равно.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import re
from api_key import get_key


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Hey, hooman! Type \"/calc smth = \" - and I\'ll count all the shit'
    print(text)
    update.message.reply_text(text)


def calc(bot, update):
    user_text = update.message.text
    user_text = user_text.split()
    if len(user_text) > 2:
        print('Input error')
        return update.message.reply_text('Input error')
    user_text = user_text[1]
    user_text = user_text[:-1]
    split = re.findall("(\d+)([\+\*\/\-])(\d+)*", user_text)
    x = split[0][0]
    y = split[0][2]
    sign = split[0][1]
    x = int(x)
    y = int(y)
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
    mybot = Updater(get_key(), request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("calc", calc))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
