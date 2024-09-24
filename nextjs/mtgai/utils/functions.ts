export function numberWithCommas(x:number) {
    if (x == null) return ""
    return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
}

export async function GetMtgFeaturedCards() {
    let url = 'http://backend/mtgCards/featured';  
    const response = await fetch(url,{next: {revalidate: 120}});
    const data = await response.json();
    // console.log(data)
    return data;
}

export async function GetMtgFeaturedCollections(nCollections: number) {
    let url = 'http://backend/collections/featured?num_collections='+String(nCollections);  ;  
    const response = await fetch(url,{next: {revalidate: 120}});
    const data = await response.json();
    console.log(data)
    return data;
}

export async function GetRandomMtgCard() {
    let url = 'http://backend/mtgCards/random';  
    const response = await fetch(url);
    const data = await response.json();
    return data;
  }

  export async function GetMtgTrendingCards(nCards: number) {
    let url = 'http://backend/mtgCards/trending/?ncards='+String(nCards);  
    const response = await fetch(url);
    const data = await response.json();
    return data;
}