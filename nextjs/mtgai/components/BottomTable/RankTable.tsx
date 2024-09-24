
import {GetMtgTrendingCards } from "@utils/functions";
import {TMtgCard } from '@components/MtgCard/MtgCard';
import { useEffect, useState } from 'react';
import { newMtgCard } from "@utils/models";
import ListOfCards from "@components/ListOfCards/ListOfCards";
import BottomTable from "./BottomTable";

async function RankTable() {

  // const [mtgCards, setCards] = useState([newMtgCard] as TMtgCard[])
  // const [width, setWidth] = useState<number>(window.innerWidth);
 
  // useEffect(()=>{
  //   GetMtgTrendingCards(10).then((data)=>{
  //     console.log(data.name)
  //     setCards(data)
  //   })
  // }, [])

  const trendingMtgCards = await GetMtgTrendingCards(10);
  // const recentMtgCards = await GetMtgRecentCards(10);
 
  const bootstrapStyle={
    width:"100vw",
    overflow: "scroll",
    contain: "content"
  };

  return (
    <div>
      <BottomTable mtgCards={trendingMtgCards}/>
    </div>
  )

}

export default RankTable
