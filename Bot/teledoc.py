from flask import Flask, request, jsonify, Response
import json
import dns
import requests
import pymongo
import Levenshtein
global cities
app = Flask(__name__)

def DetailExtractor(UserId):
    Items = {1: "Oxygen Cylinder", 2: "Hospital bed", 3: "Plasma", 4: "Remedisvir", 5: "Fabiflu", 6: "Tocilizumbad", 7: "Oxygen Refill"}
    Details = next(Information_Collection.find({'_id': UserId}))
    return 'Your following details are noted:'+'\nPatient Name: '+Details['Name']+'\nLocation: '+Details['Location']+'\nItem: '+ Items[int(Details['Item'])]+'\nPhone Number: '+ Details['Phone Number'] +'\n\nIf you wish to re-enter, type: deleteme'

def locator(location):
    global cities
    scores = []
    for city in cities:
        scores.append(Levenshtein.distance(city, location))
    minimum = min(scores)
    index = 0
    for i in scores:
        if minimum == i:
            return cities[index]
        index += 1



def ValidateNumber(Number):
    if Number.isdigit():
        if int(Number) >= 7000000000 and int(Number) < 10000000000:
            return True
    return False


def SendMessage(UserId, content):
    return requests.get(url='https://api.telegram.org/' + 'bot1677533831:AAE6Pyz91cyqR-zUhJq-ksjo-x13tUx3-Uk' + '/sendMessage' + '?chat_id=' + str(UserId) + '&text=' + content)

def DetailRequired(UserId, Message):
    Status = next(Status_Collection.find({"_id": UserId}, {"Phone Number": 1, "Name": 1, "Location": 1, "Item": 1, "Completed": 1}))
    if Message == "deleteme" and Status["Completed"] == True:
        SendMessage(UserId, "All your current data has been erased. Please enter again if you wish.\n")
        Status_Collection.delete_one({"_id": {"$eq": UserId}})
        Information_Collection.delete_one({"_id": {"$eq": UserId}})
        return True

    if Status["Completed"] == True:
        return 0
    if Status['Phone Number'] == False: # Just receiving phone number
        if ValidateNumber(Message) == False:
            SendMessage(UserId, 'Incorrect phone number format. Please re-enter.')
            return 1
        else:
            Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Phone Number": True}})
            Information_Collection.insert_one({'_id': UserId, 'Phone Number': Message})
            return 2

    if Status["Name"] == False:
        Information_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Name": Message}})
        Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Name": True}})
        return 3

    if Status["Location"] == False:  # Just received location
        Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Location": True}})
        location_ofperson = locator(Message)
        Information_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Location": location_ofperson}})
        SendMessage(UserId, "Your location is noted as: "+location_ofperson)
        return 4

    if Status['Phone Number'] == True and Status["Name"] == True and Status["Location"] == True and Status["Item"] == False:
        if Message.isdigit():
            if int(Message) >= 1 and int(Message) <= 7:
                Information_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Item": int(Message)}})
                Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Item": True}})
                Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Completed": True}})
                return 0
        SendMessage(UserId, "Incorrect value, please re-enter.")
        return 4




def PhoneNumber(UserId):
    SendMessage(UserId, 'What is your phone number? (e.g. 9101234567)')
    if Status_Collection.count_documents({'_id': {"$in": [UserId]}}) == 0:
        Status_Collection.insert_one({"_id": UserId, "Phone Number": False, "Name": False, "Location": False, "Item": False, "Completed": False})
    else:
        Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Phone Number": False}})

def Name(UserId):
    SendMessage(UserId, "What is your name?")


def Location(UserId):  # 1. Put status as [item], 2. Ask for location
    SendMessage(UserId, "Which city are you in? (e.g. kolkata)")


def Item(UserId):  # 1. Put status as [], 2. Ask for item
    SendMessage(UserId, "Write the number of the item you need:\n1. Oxygen Cylinder\n2. Hospital bed\n3. Plasma\n4. Remedisvir\n5. Fabiflu\n6. Tocilizumbad\n7. Oxygen Refill\n")


@app.route('/', methods=['POST'])
def index():
    Data_Received = request.get_json()
    if 'message' not in Data_Received:
        return Response('ok', status=200)
    UserId = Data_Received['message']['from']['id']
    Message = Data_Received['message']['text']

    if Status_Collection.count_documents({'_id': {"$in": [UserId]}}) == 0:
        detail = 1
    else:
        detail = DetailRequired(UserId, Message)
    if detail == 1:
        PhoneNumber(UserId)
    if detail == 2:
        Name(UserId)
    if detail == 3:
        Location(UserId)
    if detail == 4:
        Item(UserId)
    if detail == 0:
        SendMessage(UserId, DetailExtractor(UserId))
    return Response('ok', status=200)

if __name__ == '__main__':
    client = pymongo.MongoClient(
        "mongodb+srv://ojas:Ojulala02@cluster0.kfpcm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database('UserData')
    Status_Collection = db.get_collection("Status")
    Information_Collection = db.get_collection("Information")
    file = open('cities.csv', 'r')
    cities = []
    for city in file:
        cities.append(city.strip().split(',')[0])
    file.close()
    app.run(threaded=True)
