import telebot
from config import keys
from config import TOKEN
from utils import APIException
from utils import CryptoConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в формате:\n \
<имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> \
<количество первой валюты>\n Список доступных валют можно узнать при помощи команды /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def curr(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, f'{key.title()} - {keys[key]}'))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Неправильное количество параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote.lower(), base.lower(), amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'не удалось обработать команду\n{e}')
    else:
        text = f'Стоимость {amount} {keys[quote]} в {keys[base]} = {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
