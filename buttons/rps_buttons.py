from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

# Инициализируем билдер
rps_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Инициализируем кнопки
buttons: list[KeyboardButton] = [KeyboardButton(text='Камень'),
                                 KeyboardButton(text='Ножницы'),
                                 KeyboardButton(text='Бумага')]

# Добавляем кнопки
rps_builder.row(*buttons)
