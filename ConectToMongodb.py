from pymongo import MongoClient
from bson.objectid import ObjectId

# http://t.me/DataBaseUploadBot

def uploadDataBase(structItem):
    cluster = MongoClient(
        "mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    print("Connect on")

    pos = list(map(int, (structItem['pos']).split()))
    pos = ({"x": pos[0], "y": pos[1]})

    users = {
        "name": structItem['name'],
        "position": pos,
        "imgUrl": structItem['imgUrl'],
        "text": structItem['textImg'],
        "modelName": structItem['modelName'],
        "radius": int(structItem['radius']),
        "anamorphClass": structItem['anamorthClass'],
    }

    db.struct_for_webSite.insert_one(users)  # не забудь здесь поменять коллекции на нужную


def uploadNewModel(structItem):
    cluster = MongoClient(
        "mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    print("Connect on")

    model = {
        "name": structItem['nameModel'],
        "Url": structItem['url'],
    }

    db.models.insert_one(model)  # не забудь здесь поменять коллекции на нужную


def uploadNewClass(structItem):
    cluster = MongoClient("mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    print("Connect on")

    _class = {
        "name": structItem['nameClass'],
    }

    db.Class.insert_one(_class)  # не забудь здесь поменять коллекции на нужную


def downloadModels():
    cluster = MongoClient("mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    collection = db['models']
    downloads = collection.find()
    massOfModelsName = []
    for download in downloads:
        if 'name' in download:
            massOfModelsName.append(download['name'])
    return sorted(set(massOfModelsName))


def downloadRadius():
    cluster = MongoClient("mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    collection = db['struct_for_webSite']
    downloads = collection.find()
    massOfRadius = []
    for download in downloads:
        if 'radius' in download:
            massOfRadius.append(download['radius'])
    return sorted(set(massOfRadius))


def downloadClass():
    cluster = MongoClient("mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    collection = db['Class']
    downloads = collection.find()
    massOfClass = []
    for download in downloads:
        if 'name' in download:
            massOfClass.append(download['name'])
    return sorted(set(massOfClass))

def downloadDeleteData():
    cluster = MongoClient("mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    collection = db['struct_for_webSite']
    downloads = collection.find()
    massOfClass = []
    for download in downloads:
        if 'name' in download:
            massOfClass.append(download['name'])
    return sorted(set(massOfClass))


def deleteStruct(nameindex):
    client = MongoClient("mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = client['telebot']
    collection = db['struct_for_webSite']

    # Укажите фильтр для удаления
    delete_filter = {"name": str(nameindex)}

    # Удалите один документ, соответствующий фильтру
    result = collection.delete_one(delete_filter)
    print(f"Удалено документов: {result.deleted_count}")