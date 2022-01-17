from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tarjima qilmoqchi bolgan matnni kiriting😊")],
        [KeyboardButton(text="ID ni bilish🆔")]
      
      
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
orqa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Orqaga🔙")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)