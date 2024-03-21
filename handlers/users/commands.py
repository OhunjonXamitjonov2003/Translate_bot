from data.loader import bot,db
from telebot.types import Message
from keyboards.default import registr
from keyboards.inline import translate




@bot.message_handler(commands=['start'])
def start(message:Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    db.insert_telegram_id(telegram_id=from_user_id)

    check = db.chsck_user(telegram_id=from_user_id)
    if None in check:
        text =f"Assalomu alaykum {message.from_user.full_name} Translete botga hush kelibsiz\n"\
              "Botdan foydalanish uchun ro'yhatdan o'ting👇"
        markup = registr()

    else:
        text = "siz ro'yhatdan otib bo'lgansiz translete uchun buttonni bosing!!!"
        markup = translate()


    bot.send_message(chat_id,text,reply_markup=markup)

