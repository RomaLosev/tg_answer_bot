import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from lists import simple_answers, drink, buy_car, dinara, drink_question
import random
from search_word_in_list import is_part_in_list


load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
button = KeyboardButton('Получить ответ')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


@dp.message_handler(commands=['start'])
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    logging.info(f'User {message.from_user.full_name}, started bot ')
    await message.answer(f'👋 Привет, {message.from_user.full_name}!\n'
                         '🤓Я помогаю принимать важные решения\n'
                         'Напиши мне свой вопрос❓ Или жми на кнопку 🔳\n'
                         'По кнопке доступны не все ответы!', reply_markup=greet_kb)


@dp.message_handler(content_types=['text'])
async def answer_handler(message: Message) -> None:
    """
    Handler will answer for some questions
    """
    logging.info(f'User {message.from_user.full_name}, asks {message.text}')
    try:
        if is_part_in_list(message.text, drink_question):
            await message.answer(text=random.choice(drink))
        elif is_part_in_list(message.text, dinara):
            await message.answer(text=random.choice(buy_car))
        else:
            await message.answer(text=random.choice(simple_answers))
    except TypeError:
        await message.answer('Это что?? Давай, напиши нормальный вопрос текстом!')


def main() -> None:
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
