from telebot.types import ReplyKeyboardMarkup,KeyboardButton


def registr():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Ro'yhatdan o'tish")
    markup.add(btn1)
    return markup

def phone_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Telfon raqamni yuborish",request_contact=True)
    markup.add(btn1)
    return markup