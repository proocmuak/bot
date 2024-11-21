from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Записаться", callback_data="createAgreement")]
]
ask_name = [
   [KeyboardButton(text="Да"),     
   KeyboardButton(text="Нет")]
]
forWhat = [
    [InlineKeyboardButton(text="Улучшить успеваемость", callback_data="improveStudiest")], 
     [InlineKeyboardButton(text="Сдать экзамен", callback_data="WriteExam")]
]
chooseclass = [
    [InlineKeyboardButton(text="7", callback_data="class_7"), 
    InlineKeyboardButton(text="8", callback_data="class_8") ],
    [InlineKeyboardButton(text="9", callback_data="class_9"), 
    InlineKeyboardButton(text="10", callback_data="class_10")]
]
ask_which_exam = [
    [InlineKeyboardButton(text="ОГЭ", callback_data="exam_oge")],
    [InlineKeyboardButton(text="ЕГЭ", callback_data="exam_ege")]
]
keyboard = ReplyKeyboardMarkup(
        keyboard=ask_name,
        resize_keyboard=True,
        input_field_placeholder="Выберите ответ",
        one_time_keyboard=True
        
    )

menu = InlineKeyboardMarkup(inline_keyboard=menu)
forWhat = InlineKeyboardMarkup(inline_keyboard=forWhat)
chooseclass = InlineKeyboardMarkup(inline_keyboard=chooseclass)
ask_which_exam = InlineKeyboardMarkup(inline_keyboard=ask_which_exam)
