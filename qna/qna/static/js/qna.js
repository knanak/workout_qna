const main = document.querySelector("#main");
const qna = document.querySelector("#qna");
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

function goNext(qnaId){
const qID = document.getElementById(qnaId);
const qIdx = qnaId.split("-").shift()
const aIdx = qnaId.split("-").pop()

if(qIdx === endPoint){
  goResult();
  return;
}

const url = '/qna/'+ qIdx
fetch(url, {
    mode : 'same-origin'
  })
  .then(response => {
    return response.json() //Convert response to JSON
  })
  .then(data => {
    console.log(data)
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