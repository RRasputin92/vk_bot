# vk_bot
[RU] Бот для ВКонтакте, способный писать сообщения от лица пользователя по заданному расписанию, с использованием технологий NLU (Nature Language Understanding) или отвечая на строго заданные сообщения.
ребования:
pip install -r requirements.txt
создать .env-файл для того, чтобы хранить переменные окружения ACCESS_TOKEN и USER_ID
Пример .env-файла:
ACCESS_TOKEN="1q2w3e4r5t6y7u8i9o..."
USER_ID="1234567890"
Где взять ACCESS_TOKEN?
быстрый путь: использовать https://vkhost.github.io/
сложный путь: декомпилировать приложение KateMobile и получить данные приложения для получения токена через запрос
стандартный путь: создать своё приложение для ВКонтакте см. документацию
Примеры использования
Использование Bot:
from simple_bot import Bot

# создание и запуск обычного бота
bot = Bot()
    
# отправка тестового сообщения
bot.send_message()
    
# отправка сообщения с заданными параметрами
bot.send_message(receiver_user_id="1234567890", message_text="Привет, это сообщение отправлено автоматически")
Использование Scheduled Bot:
from scheduled_bot import ScheduledBot

# создание и запуск бота, отправляющего сообщения по расписанию
scheduled_bot = ScheduledBot()
Использование LongPoll Bot:
from longpoll_bot import LongPollBot

# создание и запуск бота, автоматически отвечающего на заданные сообщения
long_poll_bot = LongPollBot()
long_poll_bot.run_long_poll()
Использование NLU LongPoll Bot:
from nlu_longpoll_bot import NLULongPollBot

# создание и запуск бота, автоматически отвечающего на любые сообщения
nlu_longpoll_bot = NLULongPollBot()
nlu_longpoll_bot.run_long_poll()
