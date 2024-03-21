from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton





def translate():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Translate",callback_data="translate")
    markup.add(btn1)
    return markup



def langs_buttons():
    markup = InlineKeyboardMarkup(row_width=2)
    uz_en = InlineKeyboardButton("Uz-En",callback_data="uz_en")
    uz_ru = InlineKeyboardButton("Uz-Ru",callback_data="uz_ru")
    ru_en = InlineKeyboardButton("Ru-En",callback_data="ru_en")
    ru_uz = InlineKeyboardButton("Ru-uz",callback_data="ru_uz")
    en_ru = InlineKeyboardButton("En-Ru",callback_data="en_ru")
    en_uz = InlineKeyboardButton("En-Uz",callback_data="en_uz")
    markup.add(uz_en,uz_ru,ru_en,ru_uz,en_ru,en_uz)
    return markup