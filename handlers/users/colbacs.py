from data.loader import bot,db
from telebot.types import CallbackQuery, Message
from keyboards.inline import langs_buttons,translate

from translate import Translator

@bot.callback_query_handler(func=lambda call:call.data == "translate")
def reaction_to_translete(call:CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id,call.message.message_id)
    bot.send_message(chat_id,"Tarjima qilish uchun til tanlang",reply_markup=langs_buttons())

LANGS = {}
@bot.callback_query_handler(func=lambda call:call.data in ["uz_en","uz_ru","ru_en","ru_uz","en_ru","en_uz"])
def rection_to_lengs(call:CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    from_lang,to_lang = call.data.split('_')
    LANGS[from_user_id] = {
        "from_lang":from_lang,
        "to_lang":to_lang
    }
    bot.delete_message(chat_id,call.message.message_id)
    msg = bot.send_message(chat_id,"Tarjima qilish uchun so'z kiriting")
    bot.register_next_step_handler(msg,get_text)

def get_text(message:Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    from_lang = LANGS[from_user_id]["from_lang"]
    to_lang = LANGS[from_user_id]["to_lang"]
    text = message.text
    translator = Translator(from_lang=from_lang,to_lang=to_lang)
    translation = translator.translate(text)
    bot.send_message(chat_id,translation +'\n---------------------------------------------',reply_markup=translate())
