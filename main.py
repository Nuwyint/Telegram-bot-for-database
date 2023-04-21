# кнопки
# поле приоретета
# кнопки для названия моделей
# удаление
# вайтлист

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from ConectToMongodb import uploadDataBase, uploadNewModel, uploadNewClass, downloadModels, downloadRadius, downloadClass, downloadDeleteData, deleteStruct


def start(update: Update, context: CallbackContext):
    function_keyboard = create_function_keyboard()
    update.message.reply_text("Привет, я телеграм-бот созданный для заполения и управления mongodb")
    update.message.reply_text("Пожалуйста, выберите функцию:", reply_markup=function_keyboard)


def menu(update: Update, context: CallbackContext):
    function_keyboard = create_function_keyboard()
    update.message.reply_text("Пожалуйста, выберите функцию:", reply_markup=function_keyboard)


def create_function_keyboard():
    keyboard = [
        [KeyboardButton("Создать новую структуру базы данных"), KeyboardButton("Создать новую модель")], [KeyboardButton("Создать новый класс"), KeyboardButton("Удалить структуру")]
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)


def create_Models_keyboard():
    listModels = downloadModels()
    keyboard = []
    for i in range(0, len(listModels), 2):
        row = [KeyboardButton(listModels[i])]
        if i + 1 < len(listModels):
            row.append(KeyboardButton(listModels[i + 1]))
        keyboard.append(row)
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)


def create_Radius_keyboard():
    listModels = downloadRadius()
    keyboard = [[KeyboardButton(func) for func in listModels]]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)


def create_Class_keyboard():
    listModels = downloadClass()
    print(listModels)
    keyboard = []
    for i in range(0, len(listModels), 2):
        row = [KeyboardButton(listModels[i])]
        if i + 1 < len(listModels):
            row.append(KeyboardButton(listModels[i + 1]))
        keyboard.append(row)
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

def create_delete_keyboard():
    listModels = downloadDeleteData()
    keyboard = []
    for i in range(0, len(listModels), 2):
        row = [KeyboardButton(listModels[i])]
        if i + 1 < len(listModels):
            row.append(KeyboardButton(listModels[i + 1]))
        keyboard.append(row)
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

def newModel(update: Update, context: CallbackContext):
    update.message.reply_text("Вы начали создание новой модели, чтобы отменить /exit \nНапишите название модели: ")

    context.user_data.pop("name", None)
    context.user_data.pop("pos", None)
    context.user_data.pop("imgUrl", None)
    context.user_data.pop("textImg", None)
    context.user_data.pop("modelName", None)
    context.user_data.pop("radius", None)
    context.user_data.pop("anamorthClass", None)
    context.user_data.pop("nameModel", None)
    context.user_data.pop("url", None)

    context.user_data['state'] = "nameModel"


def newData(update: Update, context: CallbackContext):
    update.message.reply_text("Вы начали создание новой структуры объекта, чтобы отменить /exit \nНапишите название объекта: ")

    context.user_data.pop("name", None)
    context.user_data.pop("pos", None)
    context.user_data.pop("imgUrl", None)
    context.user_data.pop("textImg", None)
    context.user_data.pop("modelName", None)
    context.user_data.pop("radius", None)
    context.user_data.pop("anamorthClass", None)
    context.user_data.pop("nameModel", None)
    context.user_data.pop("url", None)

    context.user_data['state'] = "name"


def newClass(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Вы начали создание нового класса, чтобы отменить /exit \nНапишите название класса: ")

    context.user_data.pop("name", None)
    context.user_data.pop("pos", None)
    context.user_data.pop("imgUrl", None)
    context.user_data.pop("textImg", None)
    context.user_data.pop("modelName", None)
    context.user_data.pop("radius", None)
    context.user_data.pop("anamorthClass", None)
    context.user_data.pop("nameModel", None)
    context.user_data.pop("url", None)
    context.user_data.pop('nameClass', None)

    context.user_data['state'] = "nameClass"


def process_manager(update: Update, context: CallbackContext):
    state = context.user_data.get("state")
    uData = context.user_data
    text = update.message.text
    answer = update.message.reply_text

    print(state)
    if state is not None:
        # Creating new struct ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
        if state == "name":
            uData["name"] = text
            answer('Введите позицию через пробел: ', reply_markup=ReplyKeyboardRemove())
            uData['state'] = 'pos'
        elif state == 'pos':
            uData["pos"] = text
            answer('Вставте ссылку на фотографию: ')
            uData['state'] = 'imgUrl'
        elif state == 'imgUrl':
            uData['imgUrl'] = text
            answer('Введите текст: ')
            uData['state'] = 'textImg'
        elif state == "textImg":
            uData['textImg'] = text
            Models_keyboard = create_Models_keyboard()
            answer('Выберете модель: ', reply_markup=Models_keyboard)
            uData['state'] = 'modelName'
        elif state == 'modelName':
            Radius_keyboard = create_Radius_keyboard()
            answer('Выберете радиус: ', reply_markup=Radius_keyboard)
            uData['modelName'] = text
            uData['state'] = 'radius'
        elif state == 'radius':
            uData['radius'] = text
            Class_keyboard = create_Class_keyboard()
            answer('Выберете класс: ', reply_markup=Class_keyboard)
            uData['state'] = 'anamorthClass'
        elif state == 'anamorthClass':
            uData['anamorthClass'] = text
            uploadDataBase(uData)
            answer(
                f'Объект: {uData["name"]}\nПозиция: {uData["pos"]} \nСсылка: {uData["imgUrl"]} \nТекст: {uData["textImg"]}\nМодель: {uData["modelName"]} \nРадиус: {uData["radius"]} \nКласс: {uData["anamorthClass"]}\nбыли сохранены в базе данных.', reply_markup=create_function_keyboard())
            uData["state"] = None
            menu(update, context)
        # creating model ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
        elif state == "nameModel":
            uData["nameModel"] = text
            answer('Введите ссылку: ', reply_markup=ReplyKeyboardRemove())
            uData['state'] = 'url'
        elif state == 'url':
            uData["url"] = text
            uploadNewModel(uData)
            answer(f'Модель: {uData["nameModel"]}\nСсылка: {uData["url"]} была сохранена в базе данных.')
            uData["state"] = None
        # creating "class"⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
        elif state == "nameClass":
            uData['nameClass'] = text
            uploadNewClass(uData)
            answer(f'Класс {uData["nameClass"]} инициализирован')
            uData["state"] = None
        # deleting ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
        elif state == "death":
            died = update.message.text
            deleteStruct(died)
            update.message.reply_text(f'Структура с названием {died} удалена')
            died = None
            menu(update, context)
        # error ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
        else:
            print(state)
            answer('Пожалуйста, используйте команду /start, чтобы начать сбор данных.')

    # Button trigger ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
    elif text == "Создать новую модель":
        newModel(update, context)
    elif text == "Создать новую структуру базы данных":
        newData(update, context)
    elif text == "Создать новый класс":
        newClass(update, context)
    elif text == "Удалить структуру":
        deleteEleventDb(update, context)
    # ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂


def deleteEleventDb(update: Update, context: CallbackContext):
    context.user_data['state'] = "death"
    update.message.reply_text("Выберете имя по которому хотите удалить структуру", reply_markup = create_delete_keyboard())


def deleteNew(update: Update, context: CallbackContext):
    context.user_data['state'] = None
    update.message.reply_text('Наполнение отклонено')
    menu(update, context)


def help(update: Update, context: CallbackContext):
    update.message.reply_text("/start, /menu, /newdatam, /newNodel, /exit, /newClass, /delete, /help")


def main():
    token = '6022951486:AAFsk95GftNYjSnB2Awl4E0o0zmELIoiLS0'
    updater = Updater(token, use_context=True)
    print("Bot enable")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CommandHandler("newData", newData))
    dispatcher.add_handler(CommandHandler('newModel', newModel))
    dispatcher.add_handler(CommandHandler('exit', deleteNew))
    dispatcher.add_handler(CommandHandler('newClass', newClass))
    dispatcher.add_handler(CommandHandler('delete', deleteEleventDb))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_manager))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
