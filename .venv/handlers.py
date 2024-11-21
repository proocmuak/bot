from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from misc import dp, bot
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, ContentType

import kb
import text

name = ''

@dp.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet, reply_markup=kb.menu)

@dp.callback_query(F.data=="createAgreement") #Уточнение имени
async def name_step(callback: CallbackQuery):
    await callback.message.answer(text.name.format(name=callback.from_user.full_name), reply_markup=kb.keyboard)
    await callback.answer()

@dp.message(F.text.lower() == "нет")
async def not_my_name(message: types.Message):
    await message.reply(text.correct_name, reply_markup=types.ReplyKeyboardRemove())
    @dp.message(F.text)
    async def handle_message(message: types.Message):
        global name 
        name = message.text
        await message.reply(text.nice_to_meet_you.format(name = message.text), reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text.ask_for_what.format(name = message.text), reply_markup=kb.forWhat)

@dp.message(F.text.lower() == "да")
async def my_name(message: types.Message):
    global name 
    name = message.from_user.full_name
    await message.reply(text.nice_to_meet_you.format(name = message.from_user.full_name), reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text.ask_for_what.format(name = message.from_user.full_name), reply_markup=kb.forWhat)


@dp.callback_query(F.data=="improveStudiest")
async def improve_step(callback: CallbackQuery):
    await callback.message.answer(text.ask_class, reply_markup=kb.chooseclass)
    await callback.answer()

@dp.callback_query(F.data=="WriteExam")
async def exam_step(callback: CallbackQuery):
    await callback.message.answer(text.which_exam, reply_markup=kb.ask_which_exam)
    await callback.answer()

@dp.callback_query(F.data=="class_7")
async def improve_step(callback: CallbackQuery):
    global name
    await callback.message.answer(text.the_end)
    await bot.send_message(710425319, ("Новая заявка, улучшить успеваемость 7 класс\n" + "@"+callback.from_user.username + "\n" + name))
    await callback.answer()

@dp.callback_query(F.data=="class_8")
async def improve_step(callback: CallbackQuery):
    global name
    await callback.message.answer(text.the_end)
    await bot.send_message(710425319, ("Новая заявка, улучшить успеваемость 8 класс\n" + callback.from_user.username + "\n" + name))
    await callback.answer()
@dp.callback_query(F.data=="class_9")
async def improve_step(callback: CallbackQuery):
    global name
    await callback.message.answer(text.the_end)
    await bot.send_message(710425319, ("Новая заявка, улучшить успеваемость 9 класс\n" + callback.from_user.username + "\n" + name))
    await callback.answer()
@dp.callback_query(F.data=="class_10")
async def improve_step(callback: CallbackQuery):
    global name
    await callback.message.answer(text.the_end)
    await bot.send_message(710425319, ("Новая заявка, улучшить успеваемость 10 класс\n" + callback.from_user.username + "\n" + name))
    await callback.answer()
@dp.callback_query(F.data=="exam_oge")
async def improve_step(callback: CallbackQuery):
    global name
    await callback.message.answer(text.the_end)
    await bot.send_message(710425319, ("Новая заявка, сдать ОГЭ\n" + callback.from_user.username + "\n" + name))
    await callback.answer()
@dp.callback_query(F.data=="exam_ege")
async def improve_step(callback: CallbackQuery):
    global name
    await callback.message.answer(text.the_end)
    await bot.send_message(710425319, ("Новая заявка, сдать ЕГЭ\n" + callback.from_user.username + "\n" + name))
    await callback.answer()


