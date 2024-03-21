from data.loader import bot,db

from telebot.types import Message,ReplyKeyboardRemove
from keyboards.default import phone_button
from keyboards.inline import translate
import string
USER_DATE = {}



@bot.message_handler(func=lambda message:message.text == "Ro'yhatdan o'tish")
def registration(mesage: Message):
    chat_id = mesage.chat.id
    from_user_id = mesage.from_user.id
    USER_DATE[from_user_id] = {}
    msg = bot.send_message(chat_id,"F.I.O ni kiriting",reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg,get_name)

def chck_user(name):
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz '"
    for latter in name.lower():
        if not latter in ascii_lowercase:
            return False
        return True
def get_name(message:Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    if chck_user(message.text):
        full_name = message.text
        USER_DATE[from_user_id]["full_name"] = full_name


        text ="Telfon raqamni buttoni bosib kiriting👇"
        markup = phone_button()
        calback = get_contact_and_save



    else:
        text ="Notog'ri \nF.I.O ni kiriting"
        markup = ReplyKeyboardRemove()
        calback = get_name
    msg = bot.send_message(chat_id,text,reply_markup=markup)
    bot.register_next_step_handler(msg, calback)



def get_contact_and_save(message:Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    full_name = USER_DATE[from_user_id]["full_name"]

    phone_number = None

    if message.contact:
        phone_number = message.contact.phone_number
    else:
        if message.text.startswith('+998') and len(message.text) == 13 and message.text[1:].isdigit():

            phone_number = message.text
        else:
            msg = bot.send_message(chat_id,"Telfon raqam noto'gri kiritildi,\n"
                             "Telfon raqamni buttoni bosib kiriting👇",reply_markup=phone_button())
            bot.register_next_step_handler(msg,get_contact_and_save)
    if phone_number:
        db.update_user(full_name,phone_number,from_user_id)
        del USER_DATE[from_user_id]
        bot.send_message(chat_id,"Ro'yhatdan muvafaqiyatli o'tdingiz!!!",reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id,"Translete uchun buttonni bosing",reply_markup=translate())
