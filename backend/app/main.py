from dataclasses import Field
from typing import Annotated, Optional
from fastapi import FastAPI, Response, HTTPException, status, Depends, Form
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.collection import Collection
from .database import *
from .models import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root ():
    return {"root_ddddd"}

@app.get("/mtgCards/latest", status_code=status.HTTP_200_OK)
def mtgCards_latest (mtg_card: MtgCardModelDb = Depends(get_latest)):
    return mtg_card

@app.get("/mtgCards/featured", status_code=status.HTTP_200_OK)
def mtgCards_featured (mtg_card = Depends(get_featured)):
    return mtg_card

@app.get("/mtgCards/trending/", status_code=status.HTTP_200_OK)
def mtgCards_trending (ncards: int):
    mtg_card: MtgCardModelDb =  get_trending(ncards)
    return mtg_card

@app.post("/mtgCards/create",status_code=status.HTTP_201_CREATED)
def mtgCards_create (theme: Annotated[str, Form()]):
    new_card_id = post_new_card(theme)
    return (new_card_id)

@app.post("/collections/create",status_code=status.HTTP_201_CREATED)
def mtgCards_create_collection (theme: Annotated[str, Form()]):
    result = post_new_collection(theme)
    return (result)

@app.get("/collections/featured",status_code=status.HTTP_200_OK)
def mtgCards_featured_collections (num_collections:int):
    result = get_featured_collections(num_collections)
    return (result)


# @app.get("/collections/list",status_code=status.HTTP_200_OK)
# def mtgCards_cards_in_collections ():
#     result = cards_in_collections("Harry Potter Collection")
#     return (result)


@app.get("/mtgCards/random",status_code=status.HTTP_200_OK)
def mtgCards_random(mtg_card = Depends(get_random)):
      return (mtg_card)

@app.get("/mtgCards/{cardId}", status_code=status.HTTP_200_OK)
def mtgCards_byId (cardId: str):
    mtg_card: MtgCardModelDb =  get_card_by_id(cardId)
    return mtg_card

# @app.get("/mtgCards/latest", response_model=MtgCardModel)
# def test_mongo (collection: Collection = Depends(get_latest)):
#     mtg_card = collection.find_one({}, sort=[( '_id', DESCENDING )])
#     if mtg_card == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
#     #del mtg_card["_id"]
#     return mtg_card

# @app.get("/mtgCards/random", response_model=MtgCardModel)
# def test_mongo (collection: Collection = Depends(get_mongodb)):
#     for card in collection.aggregate([{ "$sample": { "size": 1 } }]):
#         mtg_card = card
#     if mtg_card == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
#     #del mtg_card["_id"]
#     return mtg_card



# @app.get("/mtgCards/latest")
# def test_mongo (collection: Collection = Depends(get_mongodb)):
# # def test_mongo ():
#     mtg_card = collection.find_one(
#         {"theme": "Tennis"},
#         sort=[( '_id', DESCENDING )]
#     )
#     if mtg_card == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)

#     # resp = MtgCardModel(**mtg_card)
#     # #mtg_card = MtgCardModel(collection.find_one())
#     del mtg_card["_id"]
#     return {"mtg_card": MtgCardModel(**mtg_card)}

# @app.get("/posts")
# def get_posts (db: Session= Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post:Post):
#     post_dict=post.model_dump()
#     post_dict["_id"]=randrange(0,100000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[-1]
#     return {"data": post}


# @app.get("/posts/{id}")
# def get_post(id:int):
#     print (id)
#     for p in my_posts:
#         if p["_id"]==id:
#             return {"data": p}
        
#     raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
#                          detail="Not Found")

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     for i, p in enumerate(my_posts):
#         if p["_id"]==id:
#             my_posts.pop(i)
#             # return {"message": "post deleted"}
        
#     raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
#                          detail="Not Found")

# @app.put("/posts/{id}",status_code=status.HTTP_200_OK)
# def update_post(id:int, post:Post):
#     for i, p in enumerate(my_posts):
#         if p["_id"]==id:
#             post_dict = post.model_dump()
#             post_dict["_id"] = id
#             my_posts[i] = post_dict
#             return {"data": my_posts[i]}
        
#     raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
#                          detail="Not Found")