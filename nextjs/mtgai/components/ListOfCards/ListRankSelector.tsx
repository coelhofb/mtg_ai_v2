// import ListOfCards, { TListOfCards } from './ListOfCards.tsx'
// import { useState } from 'react'
'use client'
import { TMtgCard } from '../MtgCard/MtgCard';

function ListRankSelector() {

    let listfromserver: Array<TMtgCard> = [
    ] 

    // const [cardList, setCardList] = useState(listfromserver);

    const sortList = (option:number) => {

        // cardList.sort((a,b)=>(a.rank < b.rank ? -1 : 1))
        if (option ==1) {listfromserver.sort((a,b)=>(a.nViews - b.nViews))}
        else {listfromserver.sort((a,b)=>(a.collection < b.collection? -1:1))}  

        // setCardList(listfromserver)
    }


    return (
        <>
        
        <ul className="nav nav-pills m-3" id="pills-tab" role="tablist">
            <li className="nav-item" role="presentation">
                <button onClick={()=>(sortList(1))} className="nav-link active" id="pills-home-tab" data-bs-toggle="pill" data-bs-target="#pills-home" type="button" role="tab" aria-controls="pills-home" aria-selected="true">Trending</button>
            </li>
            <li className="nav-item" role="presentation">
                <button onClick={()=>(sortList(2))} className="nav-link" id="pills-profile-tab" data-bs-toggle="pill" data-bs-target="#pills-profile" type="button" role="tab" aria-controls="pills-profile" aria-selected="false">Recent</button>
            </li>
        </ul>
        {/* <div className="tab-content" id="pills-tabContent">
        <div className="tab-pane fade show active" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab" >...</div>
        <div className="tab-pane fade" id="pills-profile" role="tabpanel" aria-labelledby="pills-profile-tab">...</div>
        <div className="tab-pane fade" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab">...</div>
        <div className="tab-pane fade" id="pills-disabled" role="tabpanel" aria-labelledby="pills-disabled-tab">...</div>
        </div> */}

        {/* <ListOfCards cardList={cardList}/> */}
        
        
        </>
    )
}

export default ListRankSelector