import {TMtgCard } from '../../components/MtgCard/MtgCard.tsx';

// export type TListOfCards = {
//     rank: number,
//     cardName: String,
//     collection: String,
//     author: String
// }


type Props = {
    cardList: [TMtgCard]
  }

function ListOfCards ({cardList}:Props) {

    return (

        <>
        <table className="table table-dark table-hover m-5 align-middle ">
        <thead>
            <tr>
            <th>#</th>
            <th>Name</th>
            <th>Type</th>
            <th>Mana Cost</th>
            <th>Collection</th>          
            <th>Author</th>
            </tr>
        </thead>
        <tbody >

            {cardList.map((card,i)=>(
                <tr>
                    <td>{i+1}</td>
                    <td><img src={"src/assets/cards/"+card.illustration} width="100" style={{marginRight: "10px"}}/>{card.name}</td>
                    <td>{card.type}</td>
                    <td >{card.mana_cost.map((x,i)=>(<img key={i} className="card-mana-symbol" src= {"src/assets/img/"+x+"_mana.png"}/>))}</td>
                    <td>{card.collection}</td>
                    <td>{card.author}</td>
                </tr>
            ))}
                    
        </tbody>
        
        </table>
            
    </>

    )

}

export default ListOfCards