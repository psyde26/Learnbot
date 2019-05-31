from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import date, datetime


PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = "Вызван /start. Только зачем?" 
    logging.info(text)
    update.message.reply_text(text)
    

def talk_to_me(bot, update):
    user_text = update.message.text
    answer_question = {
    'Как дела?': 'Пока не родила', 
    'Что делаешь?': 'А тебе как кажется? Отвечаю на твои вопросы, судя по всему', 
    'Как настроение?': 'Было хорошо, но потом некий {} написал'.format(update.message.chat.first_name)
    }
    if user_text in answer_question:
        logging.info(answer_question.get(user_text))
        update.message.reply_text(answer_question.get(user_text))
    else:
        logging.info('Я не знаю ответа на этот вопрос, дружочек. Попробуй еще раз')
        update.message.reply_text('Я не знаю ответа на этот вопрос, дружочек. Попробуй еще раз')
        

def planet_info(bot, update):
    user_answer = (update.message.text).split(' ')
    logging.info(user_answer[1])
    time_now = ephem.Date(datetime.now())
    logging.info(time_now)
    planet_dicts = {
                'Mercury': ephem.constellation(ephem.Mercury(time_now)), 'Venus': ephem.constellation(ephem.Venus(time_now)),
                'Mars': ephem.constellation(ephem.Mars(time_now)), 
                'Jupiter': ephem.constellation(ephem.Jupiter(time_now)), 'Saturn': ephem.constellation(ephem.Saturn(time_now)),
                'Uranus': ephem.constellation(ephem.Uranus(time_now)), 'Neptune': ephem.constellation(ephem.Neptune(time_now)),
                'Pluto': ephem.constellation(ephem.Pluto(time_now))
                 }
    if user_answer[1] in planet_dicts:
        result = planet_dicts.get(user_answer[1])
    else:
        result = 'А вот и нет такой планеты, {}'.format(update.message.chat.first_name)
    
    update.message.reply_text(result)

    
def words_count(bot, update):
    x = -1
    user_input = (update.message.text).split()
    for words in user_input:
        words.strip()
        if words == '':
            user_input.remove('')
        x = x + 1
        result = ('Вы ввели {} слова'.format(x))
        logging.info(result)
    update.message.reply_text(result)
    

def next_full_moon(bot, update):
    user_input = update.message.text[16:]
    logging.info(user_input)
    user_input = (user_input).split('-')
    logging.info(user_input)
    new_list = '/'.join(user_input)
    result = ephem.next_full_moon(new_list)
    logging.info(result)

    update.message.reply_text(result)


def calculator(bot, update):
    user_input = update.message.text[6:]
    element_list = []
    for numbers in user_input:
        for elements in numbers:
            element_list.append(elements)

    try:
        if '/' in element_list:
            new_list = []
            numbers = user_input.split('/')
            for e_number in numbers:
                e_number = float(e_number)
                new_list.append(e_number)
                results = new_list[0] / new_list[-1]
            logging.info(results)
        elif '+' in element_list:
            new_list = []
            numbers = user_input.split('+')
            for e_number in numbers:
                e_number = float(e_number)
                new_list.append(e_number)
                results = sum(new_list)
            logging.info(results)
        elif '*' in element_list:
            new_list = []
            numbers = user_input.split('*')
            for e_number in numbers:
                e_number = float(e_number)
                new_list.append(e_number)
            results = new_list[0] * new_list[-1]
            logging.info(results)
        elif '-' in element_list:
            new_list = []
            numbers = user_input.split('-')
            for e_number in numbers:
                e_number = float(e_number)
                new_list.append(e_number)
            results = new_list[0] - new_list[-1]
            logging.info(results)
    except ValueError:
        results = 'Введите 2 числа, используя следующие символы: +, -, *, /'
        logging.info(results)
    except ZeroDivisionError:
        results = 'Деление на 0 невозможно'
        logging.info(results)

    update.message.reply_text(results)




def main():
    mybot = Updater("829589905:AAF9N81vkiZviIV9gIk4P2Af9-lq9vHlBY0", request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet_info))
    dp.add_handler(CommandHandler('wordcount', words_count))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('calc', calculator))

    mybot.start_polling()
    mybot.idle()


main()