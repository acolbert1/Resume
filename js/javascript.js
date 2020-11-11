function updateCounter(){
    fetch('https://099xyslc8b.execute-api.us-east-1.amazonaws.com/test/counter',{
        method: 'GET'
    })
  .then(response => {
    
    if (
        // check if response's status is 200
        response.ok 
    ) {
      return response.json()
    } else {
      throw new Error('something went wrong');
    }
  })
  .then(data => document.getElementById("VisitorCount").innerText = data.Visit_Count)

  
}
