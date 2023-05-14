const main = document.querySelector("#main");
const qna = document.querySelector(".qBox");
const answerList = document.querySelector(".answerList");
const answer = document.querySelectorAll('.answer1');
const result = document.querySelector("#result");
const endPoint = 7;
const select = [];


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


async function goNext(qqq){
const csrftoken = getCookie('csrftoken');


// if(qqq === endPoint){
//   goResult();
//   return;
// }


const url = '/qna/' + qqq + '/';
await fetch(url, {
  method : 'POST',
  mode : 'same-origin',
  headers : { 'X-CSRFToken': csrftoken},
})
  .then((response) => {
    if (!response.ok) {
      // error processing
      throw 'Error';
  }
  return response.json()
  }) 
  .then(data => {
    qna.innerHTML = data['q'];
    
    for(let i=0; i < answer.length; i++){
      answer[i].innerHTML = data['a'][i]['text'];
    }

    let q_id = data['q_id'].toString()
    console.log(q_id)
    answerList.addEventListener("click", function() {
      goNext(q_id);
    }, { once: true });

  })
}

