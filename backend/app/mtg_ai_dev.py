import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain.prompts import PromptTemplate
from models import MtgCardModel, MtgCollectionModel
# from database import *
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
import urllib.request


load_dotenv('/data/.env')

os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(temperature=0.9)

def new_mtg_card(theme:str) -> MtgCardModel:

    mtg_prompt = "You are a Magic The Gathering Card designer. You need to create a card based on a theme asked by the user."
    #card_characteristics = "The card needs to be a Blue, land card, with total mana cost of 2."
    card_characteristics = ""

    parser = JsonOutputParser(pydantic_object=MtgCardModel)

    prompt = PromptTemplate(
        template=mtg_prompt+"\n{card_characteristics}\n{format_instructions}\nCreate a card based on {query}.\n",
        input_variables=["query"],
        partial_variables={"card_characteristics": card_characteristics, "format_instructions": parser.get_format_instructions()},
    )

    #output_parser = JsonOutputParser()
    chain = prompt | llm | parser
    try:
        new_mtg_card = chain.invoke({"query": theme})
        for key in new_mtg_card.keys():
            print(f"{key}: {new_mtg_card[key]}")
    except Exception as e:
        print(e)
    return MtgCardModel(**new_mtg_card)
    

def new_illustration(image_desc: str) -> str:
    prompt = PromptTemplate(
        input_variables=["image_desc"],
        template="Generate a simple prompt to generate an image based on the following description: {image_desc}. Do not include any Cards in the illustration.",
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    illus_prompt = chain.invoke(image_desc)
    print(illus_prompt)
    try:
        image_url = DallEAPIWrapper(model="dall-e-3").run(illus_prompt)
    except Exception as e:
        print(e)
    return str(image_url)


def new_mtg_collection(theme:str) -> dict:

    mtg_prompt = "You are a Magic The Gathering Card designer.\
    You need to create a collection of cards based on a theme asked by the user.\
    The cards need to have sinergy between each other."
    #card_characteristics = "The card needs to be a Blue, land card, with total mana cost of 2."
    # card_characteristics = ""
    cards_specification = "Create 6 cards: 3 creatures, 2 spells and 1 land, based on"

    parser = JsonOutputParser(pydantic_object=MtgCollectionModel)
    # parser = StrOutputParser()


    prompt = PromptTemplate(
        template=mtg_prompt+"\n{format_instructions}\n{cards_specification} {query}.\n",
        # template=mtg_prompt+"\n{cards_specification} {query}.\n",
        input_variables=["query"],
        # partial_variables={"cards_specification": cards_specification},
        partial_variables={"cards_specification": cards_specification, "format_instructions": parser.get_format_instructions()},
    )

    print(prompt)

    #output_parser = JsonOutputParser()
    chain = prompt | llm | parser
    new_mtg_collection=""
    try:
        new_mtg_collection = chain.invoke({"query": theme})
        new_mtg_collection = new_mtg_collection.dict()
        # for key in new_mtg_collection.keys():
        #     print(f"{key}: {new_mtg_collection[key]}")
    except Exception as e:
        print(e)
    return new_mtg_collection


