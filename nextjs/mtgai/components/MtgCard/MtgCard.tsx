// import {TMtgCard} from '../../data/Constants.ts'
import './MtgCard.css'

export type TMtgCard = {
    name: string
    color: string[]
    mana_cost: string[]
    type: string
    ability: string
    power: number
    toughness: number
    flavour_text: string
    collection: string
    illustration: string
    author: string
    nViews: number
}

type Props = {
  mtgCard: TMtgCard
}

export function MtgCard({mtgCard}:Props) {

  if (mtgCard.name == "") return (<></>)
  
  let colorCode = "";
  if (mtgCard.color.length > 1) {colorCode="golden"}
  else {colorCode=mtgCard.color[0]}

  let pt = ""
  if (mtgCard.toughness) pt = mtgCard.power+"/"+mtgCard.toughness;


  const cardIllustration={
    backgroundImage: "url('/assets/cards/"+mtgCard.illustration+"')"
  }
  const cardColorBg={
    backgroundImage: "url('/assets/img/"+colorCode+"_card.png')"
  }
 
  return (
    <>
      <div className="mtg-card" style={cardColorBg}>
        <div className="card-name m-0">
          <span>{ mtgCard.name }</span>
          <span className="mana">
            {mtgCard.mana_cost.map((x,i)=>(<img key={i} className="mana-symbol" src= {"/assets/img/"+x+"_mana.png"}/>))}
          </span>
        </div>

        <div className="card-illustration" style={cardIllustration}></div>
      
        <div id="card_type">
            <span>{ mtgCard.type }</span>
            <span className="mana">
                <img className="set-symbol" src= "/assets/img/set_icon_black.png"/>
              </span>
        </div>
        <div id="card_ability">                    
            <p className="no_bullet">{mtgCard.ability}</p>                 
        </div> 
        <div className="container">
        <div className="col d-inline-flex justify-content-between w-100 m-2">
          <div  id="card_credits">
            <span>Illus. mAgIc The Hazarding</span>
            <div id="website">
            <span>magicai.datalabmaster.com</span>
          </div>               
          </div>
          <div id="card_pt">
              <span>{ pt }</span>
            </div> 
          </div>
    
            </div>
          </div>                   
    </>
  )
}

