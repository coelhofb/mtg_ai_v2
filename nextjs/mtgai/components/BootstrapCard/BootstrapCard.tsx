import { useState } from "react";
import { numberWithCommas } from "@utils/functions";
import "./Card.css";
import LikeBtn from "@components/LikeBtn/LikeBtn";
import {TMtgCard } from '@components/MtgCard/MtgCard';
import Image from 'next/image'
import { TMtgCollection } from "@utils/models";


type Props = {
    mtgCollections: TMtgCollection
    likes:number
    likedInit:boolean
  }

function BootstrapCard({mtgCollections,likes,likedInit}:Props) {

    // const [cardLikes, setCardLikes] = useState(likes);
    // const [cardLikedbyUser, setLiked] = useState(likedInit);

    // const readCard = (likes:number,liked:boolean) => {
    //     setCardLikes(likes)
    //     setLiked(liked)
    // }

    let colorCode = "";
    if (mtgCollections.color.length > 1) {colorCode="golden"}
      else {colorCode=mtgCollections.color[0]};
   
    const cardIllustration = "/assets/cards/"+mtgCollections.illustration;
    const cardBg = "url(/assets/img/"+colorCode+"_card_cr.png)";
    // const cardBg = "url(/assets/img/"+"C"+"_card_cr.png)";
    const cardViews = numberWithCommas(0);
                          
    const cardWidth={
        width: "24em",
    }
    const cardImgSettings={
        backgroundImage: cardBg,
        backgroundSize: "100%",      
    }

   return (
        <>
                <div className="card m-3 p-1" style={cardWidth}>
                    <div className= "d-flex justify-content-center" style={cardImgSettings}>
                        <img className="card-img-top p-3" src={cardIllustration}  alt="..."/>
                    </div>
                    <div className="card-body p-3">
                    <div className="container p-0 d-inline-flex align-items-center justify-content-between">
                        <h5 className="m-0" >{mtgCollections.collection_name}</h5>               
                            <div className="w-5">
                                {mtgCollections.color.map((x,i)=><img key={i} className="card-mana-symbol" src= {"/assets/img/"+x+"_mana.png"} alt=""/> )}
                            </div>
                    </div>  
                    <h6>Author: {mtgCollections.author}</h6>                     
                    {/* <p className="fst-italic card-text">{mtgCollections.flavour_text}</p> */}
                    
                    <div className="container p-0 d-inline-flex align-items-center justify-content-between">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-eye" viewBox="0 0 16 16">
                            <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8M1.173 8a13 13 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5s3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5s-3.879-1.168-5.168-2.457A13 13 0 0 1 1.172 8z"/>
                            <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5M4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0"/>
                            </svg>
                            <span className="ms-2">{cardViews}</span>
                        </div>
                        <div>
                            {/* <LikeBtn cardLikes={cardLikes} cardLikedbyUser={cardLikedbyUser} updatelikes = {readCard}/> */}
                        </div>
                    </div>    
                  </div>
                  </div>
                
        </>
  )
}

export default BootstrapCard
