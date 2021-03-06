#Добавить команду /wordcount котрая считает сова в присланной фразе.
# Например на запрос /wordcount "Привет как дела" бот должен посчитать количество слов в кавычках и ответить: 3 слова.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from api_key import get_key


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Hey, hooman! Type /wordcount \"smth\" - and I\'ll count how many words there are'
    print(text)
    update.message.reply_text(text)


def wordcount(bot, update):
    user_text = update.message.text
    user_text = user_text.split()
    user_text = user_text[1:]
    if len(user_text) == 0:
        print('Incorrect input')
        update.message.reply_text('Incorrect input')
        return
    if len(user_text[0]) < 3:
        print('Incorrect input')
        update.message.reply_text('Incorrect input')
        return
    row_length = len(user_text)
    print(row_length)
    return update.message.reply_text('This text has {} words'.format(row_length))


def main():
    mybot = Updater(get_key(), request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
