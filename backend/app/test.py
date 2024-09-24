from mtg_ai_dev import new_mtg_collection


mtg_collection = new_mtg_collection("space travel")

print(mtg_collection)
print(mtg_collection["collection_name"])
for card in mtg_collection["cards"]:
    for key in card.keys():
                print(f"{key}: {card[key]}")


