

function BlankCard() {
  //const [count, setCount] = useState(0)

  return (
    <>
          <div className="mtg_card mtg_Blank_card">
              <div className= "card_form">
                  <form method="POST"action="">  
                      <label id="labelbox">ddd</label>
                      <input type="text" id="theme" name="theme"/>
                      <button id="botao" type="submit">Generate Card</button>
                  </form>
              </div>
          </div>
    </>
  )
}

export default BlankCard
