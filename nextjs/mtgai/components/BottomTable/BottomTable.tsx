'use client'
import {GetMtgTrendingCards } from "@utils/functions";
import {TMtgCard } from '@components/MtgCard/MtgCard';
import { useEffect, useState } from 'react';
import { newMtgCard } from "@utils/models";
import ListOfCards from "@components/ListOfCards/ListOfCards";


type Props = {
  mtgCards: TMtgCard[]
}

function BottomTable({mtgCards}:Props) {

  // const [mtgCards, setCards] = useState([newMtgCard] as TMtgCard[])
  const [width, setWidth] = useState<number>(window.innerWidth);
 
  // useEffect(()=>{
  //   GetMtgTrendingCards(10).then((data)=>{
  //     console.log(data.name)
  //     setCards(data)
  //   })
  // }, [])
 
  const bootstrapStyle={
    width:"100vw",
    overflow: "scroll",
    contain: "content"
  };

if (width > 750) {
   return (
    <>
    <div style={bootstrapStyle}>
    <div className="container-fluid">
      <div className="row">
        <div className="col">
          <ListOfCards initRank = {1} cardList={mtgCards.slice(0,5)}/>
        </div>
        <div className="col">
        <ListOfCards initRank = {6} cardList={mtgCards.slice(5)}/>
        </div>
      </div>
    </div>
    </div>
    </>
  )
}
 else return (
  <>
  <div style={bootstrapStyle}>
        <ListOfCards initRank = {1} cardList={mtgCards.slice(0,5)}/>
        <h6>More</h6>
    </div>

  </>
)

}

export default BottomTable
