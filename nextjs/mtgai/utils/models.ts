import { TMtgCard } from "../components/MtgCard/MtgCard"

export const newMtgCard = {
    name: "",
    color: [""],
    mana_cost: [""],
    type: "",
    ability: "",
    power: NaN,
    toughness: NaN,
    flavour_text: "",
    collection: "",
    illustration: "",
    author: "",
    nViews: 0
  } as TMtgCard

  export type TMtgCollection = {
    collection_name: string
    color: string[]
    illustration: string
    author: string
}