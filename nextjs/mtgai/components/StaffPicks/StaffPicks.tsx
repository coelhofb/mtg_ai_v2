import { GetMtgFeaturedCards } from "@utils/functions";
import {MtgCard, TMtgCard } from '@components/MtgCard/MtgCard';
// import { useEffect, useState } from 'react';
// import { newMtgCard } from "../../utils/models.ts";

async function StaffPicks() {

    // const [mtgCards, setCards] = useState([newMtgCard] as [TMtgCard])

    // useEffect(()=>{
    //   GetMtgFeauturedCards().then((data)=>{
    //     console.log(data.name)
    //     setCards(data)
    //   })
    // }, [])
  
    const mtgCards: TMtgCard[] = await GetMtgFeaturedCards();

    const bootstrapStyle={
      width:"100vw",
      overflow: "scroll",
      contain: "content"
  }
  
     return (
      <>
      <div style={bootstrapStyle}>
        <div className="col d-inline-flex align-items-center justify-content-center"> 
          {mtgCards.map((mtgCard,i)=><MtgCard key={i} mtgCard={mtgCard}/>)}
        </div>
       </div>
      </>
    )
  }






//   const [mtgCard, setCard] = useState(newMtgCard)

 
//   useEffect(()=>{
//     GetRandomMtgCard().then((data)=>{
//       console.log(data.name)
//       setCard(data)
//     })
//   }, [])

//    return (
//     <>
 
//     <MtgCard mtgCard={mtgCard}/>
//     {/* <MtgCard mtgCard={mtgCard}/> */}
//     </>
//   )
// }

export default StaffPicks
