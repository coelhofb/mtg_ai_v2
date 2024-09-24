import NavItems from '@components/Navbar/NavItems'
import Navbar from '@components/Navbar/Navbar'
import '@styles/globals.css'
import 'bootstrap/dist/css/bootstrap.css'

type Props = {
  children: React.JSX.Element
}

const Rootlayout = ({children}:Props) => {
  return (
    <html lang="en">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link href="https://fonts.cdnfonts.com/css/goudy-mediaeval" rel="stylesheet"/>
        <title>Magic The Hazarding</title>
     </head>
   
    <body data-bs-theme="dark">
      <div >
      <Navbar/>
    <NavItems/>
      </div>
      <main className="app">
        {children}
      </main>
      
    </body> 
    </html>
  )
}

export default Rootlayout
