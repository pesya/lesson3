#Научите бота играть в города.
#Правила такие - внутри бота есть список городов, пользователь пишет /goroda Москва и если в списке такой город есть,
#бот отвечает городом на букву "а" - "Альметьевск, ваш ход". Оба города должны удаляться из списка


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
    text = 'Привет, человек! Напиши мне /goroda - и я с тобой поиграю'
    print(text)
    update.message.reply_text(text)


def goroda(bot, update):
    user_text = update.message.text
    user_text = user_text.split()
    user_city = user_text[1]

    all_cities = ['Москва',
                  'Лондон',
                  'Берлин',
                  'Мадрид',
                  'Киев',
                  'Рим',
                  'Париж',
                  'Минск',
                  'Бухарест',
                  'Вена',
                  'Гамбург',
                  'Будапешт',
                  'Варшава',
                  'Барселона',
                  'Мюнхен',
                  'Харьков',
                  'Милан',
                  'Прага',
                  'София',
                  'Казань',
                  'Белград',
                  'Брюссель',
                  'Самара',
                  'Уфа',
                  'Бирмингем',
                  'Тбилиси',
                  'Кёльн',
                  'Ереван',
                  'Пермь',
                  'Воронеж',
                  'Волгоград',
                  'Одесса',
                  'Неаполь',
                  'Донецк',
                  'Стокгольм',
                  'Краснодар',
                  'Турин',
                  'Марсель',
                  'Скопье',
                  'Амстердам',
                  'Саратов',
                  'Кишинёв',
                  'Загреб',
                  'Валенсия',
                  'Лидс',
                  'Краков',
                  'Запорожье',
                  'Франкфурт',
                  'Львов',
                  'Тольятти',
                  'Лодзь',
                  'Севилья',
                  'Палермо',
                  'Сарагоса',
                  'Владикавказ',
                  'Ижевск',
                  'Кривой Рог',
                  'Рига',
                  'Роттердам',
                  'Вроцлав',
                  'Хельсинки',
                  'Ульяновск',
                  'Вильнюс',
                  'Тирана',
                  'Ярославль',
                  'Генуя',
                  'Штутгарт',
                  'Глазго',
                  'Осло',
                  'Копенгаген',
                  'Дюссельдорф',
                  'Дортмунд',
                  'Эссен',
                  'Малага',
                  'Оренбург',
                  'Шеффилд,'
                  'Познань',
                  'Бремен',
                  'Лиссабон',
                  'Рязань',
                  'Астрахань',
                  'Гомель',
                  'Дублин',
                  'Пенза',
                  'Дрезден',
                  'Лейпциг',
                  'Ганновер',
                  'Манчестер',
                  'Гётеборг',
                  'Ливерпуль',
                  'Липецк',
                  'Лион',
                  'Гаага',
                  'Киров']

    city_in_dict = 0
    for city in all_cities:
        if city == user_city:
            city_in_dict = city

    if city_in_dict == 0:
        update.message.reply_text('Попробуй еще какой-нибудь город')
        return

    if city_in_dict[-1] == 'ь':
        last_letter = city_in_dict[-2]
    else:
        last_letter = city_in_dict[-1]

    for city in all_cities:
        if city[0].lower() == last_letter.lower():
            update.message.reply_text('{}, твой ход!'.format(city))
            all_cities.remove(city)
            all_cities.remove(city_in_dict)
            print(all_cities)
            return


def main():
    mybot = Updater(get_key(), request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("goroda", goroda))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
