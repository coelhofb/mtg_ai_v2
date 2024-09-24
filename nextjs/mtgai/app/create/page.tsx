
const CreateCard = () => {
  return (
    <div>
<h1>Create</h1>

<div className="container-sm">
  <div className="row">
  <div className="col-4">
    <h4>Card</h4>  
  </div>
 <div className="col-8">
<form>
  <div className="mb-3">
    {/* <label  className="form-label">Theme</label> */}
    <h4>Theme</h4>
    <input type="text" className="form-control" id="" aria-describedby=""/>
    <div id="" className="form-text">dsds.</div>
  </div>
  <div className="mb-3">
    {/* <label className="form-label">Collection</label> */}
    <h4>Collection</h4>
    <select className="form-select" aria-label="Default select example">
      <option selected>Assign to Collectiion</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>
 
  </div>
  <div className="mb-3">
    {/* <label  className="form-label">Theme</label> */}
    <h4>Author</h4>
    <input type="text" className="form-control" id="" aria-describedby=""/>
  </div>
  <div className="mb-3 form-check">
    <input type="checkbox" className="form-check-input" id=""/>
    <label className="form-check-label" >Check me out</label>
  </div>
  <button type="submit" className="btn btn-primary">Submit</button>
</form>
</div>
    </div>
    </div>

    </div>   
  )
}

export default CreateCard