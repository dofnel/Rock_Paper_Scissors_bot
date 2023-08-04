from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

# Инициализируем builder
start_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

buttons: list[KeyboardButton] = [KeyboardButton(text='Давай!'),
                                 KeyboardButton(text='Не хочу!')]

start_builder.row(*buttons)
