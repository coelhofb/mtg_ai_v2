#Import Dependencies
import os
from dotenv import load_dotenv
from fastapi import HTTPException, status
load_dotenv()

from datetime import date, datetime, timezone
from pymongo import MongoClient, ASCENDING, DESCENDING
from bson.objectid import ObjectId
from models import MtgCardModel, MtgColors


#App Constants
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_HOST = "mongodb:27017"

MONGO_CONN = 'mongodb://'+ MONGO_USER +':' + MONGO_PASS + '@'+ MONGO_HOST
MONGO_DB = 'db_mtg_ai'
MONGO_COLLECTION = 'mtg_ai_collection'

MONGO_DB_OLD = 'db_mtg_cards'
MONGO_COLLECTION_OLD = 'db_mtg_cards_collection'

def get_random_old():
    mtg_card={}
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB_OLD]
        collection = db[MONGO_COLLECTION_OLD]
        for card in collection.aggregate([{ "$sample": { "size": 1 } }]):
            mtg_card = card
    except Exception as e:
        print(e)
    return mtg_card

def get_latest_old() -> dict:
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB_OLD]
        collection = db[MONGO_COLLECTION_OLD]
        mtg_card = collection.find_one({}, sort=[( '_id', DESCENDING )])
        client.close
        mtg_card_dict = dict(mtg_card)
    except Exception as e:
        print(e)
    return mtg_card_dict

def migrate(mtg_card) -> dict:

    # for key in mtg_card.keys():
    #     print(f"{key}: {mtg_card[key]}")

    new_color : list[MtgColors] = []
    mana_cost: list[int | MtgColors] = []

    for color_cd in mtg_card["color"]:
        color_cd = color_cd.replace(',','')
        match color_cd:
            case "Blue": 
                new_color.append(MtgColors.BLUE)
            case "Black": 
                new_color.append(MtgColors.BLACK)        
            case "White": 
                new_color.append(MtgColors.WHITE) 
            case "Red": 
                new_color.append(MtgColors.RED)
            case "Green": 
                new_color.append(MtgColors.GREEN)    
            case _ : 
                if len(new_color) == 0:
                    new_color.append(MtgColors.COLORLESS)                       
    # print(new_color)

    for mana_cd in mtg_card["mana_cost"][0:4]:
        mana_cost.append(mana_cd)
    # print(mana_cost)

    if mtg_card["pt"] == '' or mtg_card["pt"] == 'N/A':
        power = None
        toughness = None
    else:
        power = int(mtg_card["pt"][0])
        toughness = int(mtg_card["pt"][-1])

    # print(f"{power} {toughness}")

    try:
        mtg_migrated = MtgCardModel(
            name=mtg_card["name"],
            color=new_color,
            mana_cost = mana_cost,
            type = mtg_card["type"],
            ability = mtg_card["ability"][0],
            power = power,
            toughness = toughness,
            flavour_text = ""
        )
        mtg_migrated = dict(mtg_migrated)
        mtg_migrated["illustration"] = mtg_card["illustration"]
        return mtg_migrated
    except Exception as e:
        return e


def post_new_card(mtg_card_dict):
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        mtg_card_dict["collection"] = "core set"
        mtg_card_dict["author"] = "mAgIcTheHazarding"
        card_id = collection.insert_one(mtg_card_dict)
        client.close
    except Exception as e:
        print(e)


full_collection = []

client = MongoClient(MONGO_CONN)
db = client[MONGO_DB_OLD]
collection = db[MONGO_COLLECTION_OLD]
mtg_cards = collection.find()
client.close

for mtg_card in mtg_cards:
    try:
        card_migrated = migrate(mtg_card)
        print("migrated")
        mtg_card_dict = dict(card_migrated)
        mtg_card_dict["collection"] = "core set"
        mtg_card_dict["author"] = "mAgIcTheHazarding"
        full_collection.append(mtg_card_dict)
    except Exception as e:
        print(e)
    
#print(full_collection[0:10])
#print(len(full_collection))

client = MongoClient(MONGO_CONN)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]
collection.drop()
collection.insert_many(full_collection)
client.close

# collection.insert_many(documents, ordered=True, bypass_document_validation=False, session=None)    