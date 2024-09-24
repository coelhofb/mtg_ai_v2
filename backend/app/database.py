#Import Dependencies
import os
from dotenv import load_dotenv
from fastapi import HTTPException, status
from datetime import date, datetime, timezone
from pymongo import MongoClient, ASCENDING, DESCENDING
from bson.objectid import ObjectId
from .models import *
from .mtg_ai import *
import urllib

load_dotenv('/data/.env')

#App Constants
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_HOST = os.getenv("MONGO_HOST")
IMG_PATH = os.getenv("IMG_PATH")

MONGO_CONN = 'mongodb://'+ MONGO_USER +':' + MONGO_PASS + '@'+ MONGO_HOST
MONGO_DB = 'db_mtg_ai'
MONGO_COLLECTION = 'mtg_ai_collection'
COLLECTIONS = 'mtg_ai_collections'



def get_random():
    mtg_card={}
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        for card in collection.aggregate([{ "$sample": { "size": 1 } }]):
            mtg_card = card
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    if not mtg_card:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
    del mtg_card["_id"]
    return MtgCardModelDb(**mtg_card)

def get_latest():
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        mtg_card = collection.find_one({}, sort=[( '_id', DESCENDING )])
        client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    if mtg_card == None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
    del mtg_card["_id"]
    return MtgCardModelDb(**mtg_card)

def get_featured():
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        # mtg_cards = collection.find({}, sort=[( 'name', ASCENDING )]).limit(5)
        mtg_cards= collection.aggregate([{ "$sample": { "size": 5 } }])
        
        mtg_cards = list(mtg_cards)
        client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    if len(mtg_cards) == 0:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
    for card in mtg_cards:
        del card["_id"]
    return mtg_cards

def get_trending(nCards: int):
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        # mtg_cards = collection.find({}, sort=[( 'name', ASCENDING )]).limit(5)
        mtg_cards= collection.aggregate([{ "$sample": { "size": nCards } }])
        
        mtg_cards = list(mtg_cards)
        client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    if len(mtg_cards) == 0:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
    for card in mtg_cards:
        del card["_id"]
    return mtg_cards


def get_card_by_id(card_id):
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        mtg_card = collection.find_one({ "_id" : ObjectId(card_id)})
        client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    if mtg_card == None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"Error: Card Not Found")
    del mtg_card["_id"]
    return MtgCardModelDb(**mtg_card)

def post_new_card(theme):
    try:
        mtg_card: MtgCardModel = new_mtg_card(theme)
        mtg_card_dict = mtg_card.dict()
        illustration_url = new_illustration(theme+","+ mtg_card_dict["name"]+" "+mtg_card_dict["type"]+"."+mtg_card_dict["ability"])

        
        mtg_card_dict["collection"] = "core set"
        mtg_card_dict["author"] = "mAgIcTheHazard"
        mtg_card_dict["nViews"] = 0
        
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        card_id = collection.insert_one(mtg_card_dict)

        urllib.request.urlretrieve(illustration_url, filename=IMG_PATH+str(card_id.inserted_id)+".png")

        add_illustration = { "$set": { 'illustration': str(card_id.inserted_id)+".png" } }
        collection.update_one({ "_id" : ObjectId(str(card_id.inserted_id))}, add_illustration) 
        client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return str(card_id.inserted_id)


def post_new_collection(theme):
    try:
        mtg_collection = new_mtg_collection(theme)
        mtg_collection = mtg_collection.dict()
        #illustration_url = new_illustration(theme+","+ mtg_card_dict["name"]+" "+mtg_card_dict["type"]+"."+mtg_card_dict["ability"])

        for mtg_card in mtg_collection["cards"]:
            mtg_card["collection"] = mtg_collection["collection_name"]
            mtg_card["author"] = "mAgIcTheHazard"
            mtg_card["nViews"] = 0

            illustration_url = new_illustration(theme+","+ mtg_card["name"]+" "+mtg_card["type"])
            
            client = MongoClient(MONGO_CONN)
            db = client[MONGO_DB]
            collection = db[MONGO_COLLECTION]
            card_id = collection.insert_one(mtg_card)
            urllib.request.urlretrieve(illustration_url, filename=IMG_PATH+str(card_id.inserted_id)+".png")
    
            add_illustration = { "$set": { 'illustration': str(card_id.inserted_id)+".png" } }
            collection.update_one({ "_id" : ObjectId(str(card_id.inserted_id))}, add_illustration) 
            client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return {"message" : "Collection Created"}


def init_collections()->str:
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        #{'$match': {'collection': {'$ne': "core set"}}},
        mtg_collections= collection.aggregate([{ "$group" :  {"_id" : "$collection",
                                                "illustration" : {"$first":"$illustration"},
                                                "author" : {"$first":"$author"},
                                                "cards" : {"$count":{}}}} ])
        # mtg_collections= collection.aggregate( [{ "$group" :  {"_id" : "$color",
        #                                           "cards" : {"$count":{}}}} ])
        #mtg_collections = list(mtg_collections)
        client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    for mtg_collection in mtg_collections:
        collect_id = db["mtg_ai_collections"].insert_one({
                "collection_name" : mtg_collection["_id"],
                "cards" : [],
                "illustration": mtg_collection["illustration"],
                "color": [] ,
                "author": mtg_collection["author"]
                })
        # print(card)
        # collections_list.append(card["collection"])
    return "ok"


def cards_in_collections(collect:str):
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        mtg_cards = collection.find({"collection" : collect})
        card_ids = []
        colors = []
        for card in mtg_cards:
            card_ids.append(card["_id"])
            for color in card["color"]:
                if color not in colors and color != 'C': 
                    colors.append(color)
        db["mtg_ai_collections"].find_one_and_update({'collection_name':collect},
                        { '$set': { "cards" : card_ids, "color": colors } })
        client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return "ok"


def get_featured_collections(num_collections: int):
    try:
        client = MongoClient(MONGO_CONN)
        db = client[MONGO_DB]
        collection = db[COLLECTIONS]
        mtg_collections= collection.aggregate([{ "$sample": { "size": 5 } }])
        mtg_collections = list(mtg_collections)
        print(mtg_collections)
        client.close
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    if len(mtg_collections) == 0:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
    for collect in mtg_collections:
        del collect["_id"]
        del collect["cards"]
    return mtg_collections
