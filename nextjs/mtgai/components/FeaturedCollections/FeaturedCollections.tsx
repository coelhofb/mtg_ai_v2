import { GetMtgFeaturedCards, GetMtgFeaturedCollections } from "@utils/functions";
// import {TMtgCard } from '@components/MtgCard/MtgCard';
import BootstrapCard from "@components/BootstrapCard/BootstrapCard";
import { TMtgCollection } from "@utils/models";

async function FeaturedCollections() {

  let mtgCollections : TMtgCollection[] = []
  
//   GetMtgFeaturedCards().then((data)=>{
//     console.log(data[0].name)
//     mtgCards=data
//   }
//  )
mtgCollections = await GetMtgFeaturedCollections(5)

  const bootstrapStyle={
    width:"100vw",
    overflow: "scroll",
    contain: "content"
}

   return (
    <>
    <div style={bootstrapStyle}>
      <div className="col d-inline-flex align-items-center justify-content-center"> 
        {/* <p>{mtgCollections[0].collection_name}</p> */}
        {mtgCollections.map((mtgCollections,i)=><BootstrapCard key={i} mtgCollections={mtgCollections} likes={111} likedInit ={false}/>)}
      </div>
     </div>
    </>
  )
}

export default FeaturedCollections
