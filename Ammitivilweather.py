# подключаем модуль для Телеграма
import telebot

# указываем токен для доступа к боту
bot = telebot.TeleBot('6888460713:AAEGF1AbX_1toFc9a0weHtF0d9_T36j8JPI')

# приветственный текст
start_txt = 'Привет! Напиши свой город. \n И я тебе покажу прогноз погоды.'


# обрабатываем старт бота
@bot.message_handler(commands=['start'])
def start(message):
    # выводим приветственное сообщение
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')

# запускаем бота
if __name__ == '__main__':
    while True:
        # в бесконечном цикле постоянно опрашиваем бота — есть ли новые сообщения
        try:
            bot.polling(none_stop=True, interval=0)
        # если возникла ошибка — сообщаем про исключение и продолжаем работу
        except Exception as e: 
            print('❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌')