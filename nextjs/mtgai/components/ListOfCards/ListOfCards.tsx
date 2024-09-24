'use client'
import { CSSProperties, useEffect, useState } from 'react';
import {MtgCard, TMtgCard } from '@components/MtgCard/MtgCard';
import { newMtgCard } from '@utils/models';

type Props = {
    cardList: TMtgCard[],
    initRank: number

  }

function ListOfCards ({initRank,cardList}:Props) {

    const [showCard,updateShowCard] = useState(newMtgCard);
    const [showCardStyle,updateShowCardStyle] = useState<CSSProperties>(
        {display: "none",
         position: "fixed",
         left:0,
         top:0,
         overflow: "hidden",
         pointerEvents: "none"}
        );

    const updateCard = (i:number,show:boolean,e:any) => {
        updateShowCard(cardList[i]);
        if (show) updateShowCardStyle({...showCardStyle, display: "block",left:e.clientX+50});
        else updateShowCardStyle({...showCardStyle, display: "none"});
        
    }

    return (
        <>
        <div >
            <div style={showCardStyle}>
            <MtgCard mtgCard={showCard}/>
            </div>
       
        <table className="table table-dark table-hover m-5 align-middle ">
        <thead>
            <tr style={{fontSize: "150%"}}>
            <th>#</th>
            {/* <th></th> */}
            <th>Card</th>
            {/* <th>Mana Cost</th> */}
            {/* <th>Collection</th>           */}
            <th>Author</th>
            </tr>
        </thead>
        <tbody >

            {cardList.map((card,i)=>(
                <tr onMouseOver={(e)=>updateCard(i,true,e)} onMouseLeave={(e)=>updateCard(i,false,e)}>
                    <td>{initRank+i}</td>
                    <td >
                        <div className="container-fluid">
                            <div className="row ">
                                <div className="col-3" >
                                  <img src={"/assets/cards/"+card.illustration} width="80" style={{border: "1px solid #CCCCCC", borderRadius: "15%",marginRight: "10px"}}/>
                                </div>
                                <div className="col" >
                                    <div style={{fontSize: "100%"}}>
                                        {card.name}
                                    </div >
                                    <div style={{fontSize: "70%"}}>
                                        {card.type}
                                    </div >
                                    <div >
                                        {card.mana_cost.map((x,i)=>(<img key={i} width="15" src= {"/assets/img/"+x+"_mana.png"}/>))}
                                    </div>
                                    
                                </div>
                            </div>
                        </div>
                    </td>
                   
                    {/* <td>{card.collection}</td> */}
                    <td>mAgIc</td>
                </tr>
            ))}
                    
        </tbody>
        
        </table>
        </div>
    </>

    )

}

export default ListOfCards