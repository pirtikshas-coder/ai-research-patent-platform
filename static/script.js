function searchAI(){

let query =

document
.getElementById(
"query"
)
.value;

fetch(
"/search",

{

method:"POST",

headers:{

"Content-Type":

"application/json"

},

body:

JSON.stringify({

query:query

})

}

)

.then(

response=>

response.json()

)

.then(

data=>{

document

.getElementById(

"resultBox"

)

.innerHTML=

data.result;

}

);

}
