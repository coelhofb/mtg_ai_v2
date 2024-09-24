from langchain_core.pydantic_v1 import BaseModel, Field, constr
from enum import Enum

class MtgColors(Enum):
    RED = "R"
    GREEN = "G"
    BLUE = "U"
    WHITE = "W"
    BLACK = "B"
    COLORLESS = "C"

class MtgCardModel(BaseModel):
    name: str = Field(description="maximum 35 characters",max_length=35)
    color: list[MtgColors] = Field()
    mana_cost: list[int | MtgColors] = Field(max_items=4)
    type: str = Field()
    ability: str = Field(description="maximum of 300 characters.",max_length=303)
    power: int | None = Field()
    toughness: int | None = Field()
    flavour_text: str | None = Field()

    class Config:  
        use_enum_values = True

class MtgCardModelDb(MtgCardModel):
    collection: str = Field(default="core set")
    illustration: str | None = Field(default="")
    author: str = Field(default="mAgIcTheHazard")
    nViews: int = Field(default=0)

class MtgCollectionModel(BaseModel):
    collection_name: str = Field()
    cards: list[MtgCardModel] = Field()

class MtgCollectionModelDb(BaseModel):
    collection_name: str = Field()
    cards: list = Field(default=[])
    illustration: str = Field()
    color: list[MtgColors] = Field(default=[])
    author: str = Field(default="mAgIcTheHazard")