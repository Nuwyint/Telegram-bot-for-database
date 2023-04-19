import telebot
from ConectToMongodb import *

TOKEN = '6022951486:AAFsk95GftNYjSnB2Awl4E0o0zmELIoiLS0'
bot = telebot.TeleBot(TOKEN)
print('Bot on')
structItem = {}


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.chat.id, "Вот скажи, тебе где нашли в капусте или в караганде? А Привет писать кто будет?")
@bot.message_handler(func= lambda x : x.text == "Привет" )
def giveInstructions(message):
    bot.send_message(message.chat.id, "Привет, коль тебе надобно Михаил, иль хочешь бд обновить, тогда /new пропиши")



@bot.message_handler(commands=['new'])
def structTake(message):
    user_id = message.chat.id
    structItem[user_id] = {"stage": "id"}
    msg = bot.reply_to(message, 'Введите id')
    bot.register_next_step_handler(msg, process_step)


def process_step(message):
    print("debug: enter in newData")

    user_id = message.chat.id
    stage = structItem[user_id]['stage']

    if stage == 'id':
        print("debug: still working in newData")
        structItem[user_id] = {"id": message.text, "stage": "name"}
        msg = bot.reply_to(message, 'name: "....",')
    elif stage == 'name':
        structItem[user_id].update({"name": message.text, "stage": "category"})
        msg = bot.reply_to(message, 'category": "...."')
        print(structItem)
    elif stage == 'category':
        structItem[user_id].update({"category": message.text, "stage": "positions"})
        msg = bot.reply_to(message, 'positions" через пробел координаты: ".. .."')
        print(structItem)
    elif stage == 'positions':
        structItem[user_id].update({"positions": message.text, "stage": "modelName"})
        msg = bot.reply_to(message, 'modelName": "...."')
        print(structItem)
    elif stage == 'modelName':
        structItem[user_id].update({"modelName": message.text, "stage": "___V"})
        msg = bot.reply_to(message, '___V": "...."')
        print(structItem)
    elif stage == '___V':
        structItem[user_id].update({"___V": message.text, "stage": "ImgUrl"})
        msg = bot.reply_to(message, 'ImgUrl": "...."')
        print(structItem)
    elif stage == 'ImgUrl':
        structItem[user_id].update({"ImgUrl": message.text, "stage": "text"})
        msg = bot.reply_to(message, 'text": "...."')
        print(structItem)
    elif stage == 'text':
        structItem[user_id].update({"text": message.text, "stage": "done"})
        msg = bot.reply_to(message,
                           f"Так уж и быть. Получены следующие данные:\nid: {structItem[user_id]['id']}\n"
                           f"Имя: {structItem[user_id]['name']}\n"
                           f"Категория: {structItem[user_id]['category']}\n"
                           f"Позиция:{structItem[user_id]['positions']}\n"
                           f"Имя модели:{structItem[user_id]['modelName']}\n"
                           f"___V:{structItem[user_id]['___V']}\n"
                           f"Ссылка на картинку: {structItem[user_id]['ImgUrl']}\n"
                           f"Доп текст: {structItem[user_id]['text']}")
        print(structItem)
        uploadDataBase(structItem, user_id)
        bot.send_message(message.chat.id, "Данные успешно загружены в базу данных")

    else:
        msg = bot.reply_to(message, "Введите команду /new, чтобы начать сначала.")

    if structItem[user_id]['stage'] != 'done':
        bot.register_next_step_handler(msg, process_step)

@bot.message_handler(commands=['newModel'])
def createModel(message):
    user_id = message.chat.id
    structItem[user_id] = {"stage": "id"}
    msg = bot.reply_to(message, 'Введите id новой модели')
    bot.register_next_step_handler(msg, step_model)


def step_model(message):
    print("debug: enter in newmodel")
    user_id = message.chat.id
    stage = structItem[user_id]['stage']

    if stage == 'id':
        print("debug: still working in newmodel")
        structItem[user_id] = {"id": message.text, "stage": "name"}
        msg = bot.reply_to(message, 'name: "....",')
    elif stage == 'name':
        structItem[user_id].update({"name": message.text, "stage": "__V"})
        msg = bot.reply_to(message, '__V": "...."')
        print(structItem)
    elif stage == '__V':
        structItem[user_id].update({"__V": message.text, "stage": "Url"})
        msg = bot.reply_to(message, 'Url": "...."')
        print(structItem)
    elif stage == 'Url':
        structItem[user_id].update({"Url": message.text, "stage": "done"})
        msg = bot.reply_to(message,
                           f"Так уж и быть. Получены следующие данные для новой модели:\nid: {structItem[user_id]['id']}\n"
                           f"Имя: {structItem[user_id]['name']}\n"
                           f"___V: {structItem[user_id]['__V']}\n"
                           f"Url:{structItem[user_id]['Url']}\n")
        print(structItem)
        uploadNewModel(structItem, user_id)
        bot.send_message(message.chat.id, "Данные об новой модели успешно загружены в базу данных")
    else:
        msg = bot.reply_to(message, "Введите команду /new, чтобы начать сначала.")

    if structItem[user_id]['stage'] != 'done':
        bot.register_next_step_handler(msg, step_model)


bot.polling(none_stop=True, interval=0)