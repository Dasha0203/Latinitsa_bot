import logging
import time
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message             # ловим все обновления этого типа 
from aiogram.filters.command import Command   # обрабатываем команды /start, /help и другие
import transliterate
from transliterate import translit


# 2. Инициализация объектов
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)                        # Создаем объект бота
dp = Dispatcher()                             # Создаем объект диспетчера. Все хэндлеры(обработчики) должны быть подключены к диспетчеру
logging.basicConfig(level=logging.INFO, filename="logging.txt", 
                    format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S')

# 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name=} {user_id=} {time.asctime()} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
    await bot.send_message(chat_id=user_id, text='Введите свое полное ФИО:')



    # 4. Обработка/Хэндлер на любые сообщения
@dp.message()
async def translate_name_to_latin(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    FIO=message.text 
    FIO = FIO.lower()
    parts = FIO.split()
    translated_parts = [translit(part, 'ru', reversed=True) for part in parts]
    translated_name = ' '.join(translated_parts)
    translated_name=translated_name.title()
    logging.info(f'{user_name} {user_id}: {translated_name}')
    await message.answer(text=translated_name)
    



    # 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)
