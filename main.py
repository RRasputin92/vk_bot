from simple_bot import Bot
from scheduled_bot import ScheduledBot
from longpoll_bot import LongPollBot
from nlu_longpoll_bot import NLULongPollBot

if __name__ == '__main__':
    # создание и запуск обычного бота
    bot = Bot()

    # отправка тестового сообщения
    bot.send_message()

    # отправка сообщения с заданными параметрами
    bot.send_message(receiver_user_id="1234567890", message_text="Привет, это сообщение отправлено автоматически")



