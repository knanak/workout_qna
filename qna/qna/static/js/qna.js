const main = document.querySelector("#main");
const qna = document.querySelector(".qBox");
const answerList = document.querySelector(".answerList");
const answer = document.querySelectorAll('.answer1');
const result = document.querySelector("#result");
const endPoint = 11;
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

function goResult() {
  alert('dd')
}


function goNext(qqq) {
  const csrftoken = getCookie('csrftoken');

  const url = '/qna/' + qqq + '/';
  fetch(url, {
    method: 'POST',
    mode: 'same-origin',
    headers: { 'X-CSRFToken': csrftoken },
  })
    .then((response) => {
      if (!response.ok) {
        throw 'Error';
      }
      return response.json();
    })
    .then(data => {
      qna.innerHTML = data['q'];
      // console.log(answer[0].qid)
      for (let i = 0; i < answer.length; i++) {
        answer[i].innerHTML = data['a'][i]['text'];
        answer[i].qid = data['q_id'].toString();
        // answer[i].removeEventListener('click', clickHandler); 
        // answer[i].addEventListener('click', clickHandler);
      }
      answerList.removeEventListener('click', clickHandler); 
      answerList.addEventListener('click', clickHandler); // , {once:true}를 누르면, 오히려 오름차순 진행이 안됨

      function clickHandler(event) {
        const q_id = event.target.qid;
        console.log(q_id)
        goNext(q_id);
        // if (q_id===endPoint.toString()){
        //   goResult()
        //   return;
        // } 
        // else {
          
        // }
    
          
      }

    });


}
