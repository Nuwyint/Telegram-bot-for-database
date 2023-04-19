from pymongo import *


# http://t.me/DataBaseUploadBot

def uploadDataBase(structItem, user_id):
    cluster = MongoClient("mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    print("Conect on")

    pos = list(map(int, (structItem[user_id]['positions']).split()))
    pos = ({"x": pos[0], "y": pos[1]})

    users = {
        "name": structItem[user_id]['name'],
        "category": structItem[user_id]['category'],
        "position": pos,
        "imgUrl": structItem[user_id]['ImgUrl'],
        "text": structItem[user_id]['text'],
        "modelName": structItem[user_id]['modelName'],
    }

    db.struct_for_webSite.insert_one(users)  # не забудь здесь поменять коллекции на нужную


def uploadNewModel(structItem, user_id):
    cluster = MongoClient(
        "mongodb+srv://Nuwyint:23112004@testfortelegramapi.pcazooy.mongodb.net/telebot?retryWrites=true&w=majority")
    db = cluster["telebot"]
    print("Conect on")

    model = {
        "name": structItem[user_id]['name'],
        "Url": structItem[user_id]['Url'],
    }

    db.strcut.insert_one(model) # не забудь здесь поменять коллекции на нужную
