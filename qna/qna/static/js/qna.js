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


function goNext(qnaId){
const qID = document.getElementById(qnaId);
const qIdx = qnaId.split("-").shift()
const aIdx = qnaId.split("-").pop()

const csrftoken = getCookie('csrftoken');


if(qIdx === endPoint){
  goResult();
  return;
}


const url = '/qna/' + qIdx;
fetch(url, {
  method : 'POST',
  mode : 'same-origin',
  headers : { 'X-CSRFToken': csrftoken},
  
})
  .then(response =>response.json()) //Convert response to JSON
  .then(data => {
    qna.innerHTML = data['q'];

    answer[0].innerHTML = data['answers'][0]['text'];
    answer[1].innerHTML = data['answers'][1]['text'];
    answer[2].innerHTML = data['answers'][2]['text'];
    
        // check if qIdx is 7, if not, call goNext with the next qIdx
        if (qIdx < 7) {
          const nextIdx = parseInt(qIdx) + 1;
          const nextId = "q-" + nextIdx + "-" + aIdx;
          goNext(nextId);
        } else {
          // if qIdx is 7, call goResult
          goResult();
        }

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