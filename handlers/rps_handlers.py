from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Router
from lexicon.lexicon import LEXICON
from buttons.rps_buttons import rps_builder
from buttons.other_buttons import start_builder
from services.choice import (rps_choice, get_winner)

# Создание роутера для связи с bot.py
router: Router = Router()


@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(LEXICON['/start'],
                         reply_markup=start_builder.as_markup(resize_keyboard=True,
                                                              one_time_keyboard=True))


@router.message(F.text == '/help')
async def help_message(message: Message):
    await message.answer(LEXICON['/help'])


@router.message(F.text == 'Давай!')
async def lets_message(message: Message):
    await message.answer(LEXICON['lets'],
                         reply_markup=rps_builder.as_markup(resize_keyboard=True, ))


@router.message(F.text == 'Не хочу!')
async def no_message(message: Message):
    await message.answer(LEXICON['no'])


@router.message(F.text.in_({'Камень', 'Ножницы', 'Бумага'}))
async def rock_message(message: Message):
    bot_choice = rps_choice()
    await message.answer(f"Бот выбрал - {bot_choice}")
    result = get_winner(message.text, bot_choice)
    await message.answer(LEXICON[result], reply_markup=start_builder.as_markup(resize_keyboard=True,
                                                                               one_time_keyboard=True))


@router.message()
async def another_message(message: Message):
    await message.answer(LEXICON['another'])
