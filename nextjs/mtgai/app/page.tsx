
import RankTable from '@components/BottomTable/RankTable'
import FeaturedCollections from '@components/FeaturedCollections/FeaturedCollections'
import ListRankSelector from '@components/ListOfCards/ListRankSelector'
import StaffPicks from '@components/StaffPicks/StaffPicks'
import React from 'react'

const Home = () => {
  return (
    <div>
    <div className="container ms-1">
      <h2>Featured Collections</h2>
    </div>
    <FeaturedCollections/>
    {/* <ListRankSelector/> */}
    <RankTable/>
    <div className="container ms-1">
      <h2>Staff Picks </h2>
    </div>
    <StaffPicks/>
    </div>
  )
}

export default Home