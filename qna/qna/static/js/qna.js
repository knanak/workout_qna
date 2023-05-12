const main = document.querySelector("#main");
const qna = document.querySelector(".qBox");
const answer = document.querySelectorAll('.answer1');
const result = document.querySelector("#result");
const endPoint = 7;
const select = [];

// const goNext = (answerId) = {

// }

// function addAnswer(answerText, qIdx, idx){
//   var a = document.querySelector('.answerBox');
//   var answer = document.createElement('button');
//   answer.classList.add('answerList');
//   answer.classList.add('my-3');
//   answer.classList.add('py-1');
//   answer.classList.add('mx-auto');
//   answer.classList.add('fadeIn');

//   a.appendChild(answer);
//   answer.innerHTML = answerText;

//   answer.addEventListener("click", function(){
//     var children = document.querySelectorAll('.answerList');
//     for(let i = 0; i < children.length; i++){
//       children[i].disabled = true;
//       children[i].style.WebkitAnimation = "fadeOut 0.5s";
//       children[i].style.animation = "fadeOut 0.5s";
//      }
//      setTimeout(() => {
//        select[qIdx] = idx;
//        for(let i = 0; i < children.length; i++){
//          children[i].style.display = 'none';
//         }
//       goNext(++qIdx);
//     },450)
//   }, false);
// }

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

// function nextAnswer(qIdx, aIdx){
//   answer[0].addEventListener("click", function(){ // answer이 버튼이 아니어서 에러남

//     setTimeout(() => {
//       select[qIdx] = aIdx;
      
//       goNext(++qIdx);
//     },450)
//   }, false);
// }



async function goNext(qqq){
// let qIdx = parseInt(qqq.split("-").shift())
// let aName = qqq.split("-").pop()
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

    answer[0].innerHTML = data['a'][0]['text'];
    answer[1].innerHTML = data['a'][1]['text'];
    answer[2].innerHTML = data['a'][2]['text'];
    
    answer[0].addEventListener("click", function(){
      goNext(++qqq)
    })
    // answer[1].addEventListener("click", function(){
    //   goNext(++qqq)
    // })
    // answer[2].addEventListener("click", function(){
    //   goNext(++qqq)
    // })

  })
}



// function begin(){
//   qna.style.WebkitAnimation = "fadeIn 1s";
//   qna.style.animation = "fadeIn 1s";
//   setTimeout(() => {
//     main.style.display = "none";
//     qna.style.display = "block";
//   }, 450)
//   let qIdx = 0;
//   goNext(qIdx);
  
//    }