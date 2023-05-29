const main = document.querySelector("#main");
const qna = document.querySelector(".qBox");
const answerList = document.querySelector(".answerList");
const answer = document.querySelectorAll('.answer1');
const result = document.querySelector("#result");
const endPoint = 11;
var pointArray=[
  {name : 'hipAB' , value : 0, key : 0},
  {name : 'hipAD' , value : 0, key : 0},
  {name : 'hipEXT' , value : 0, key : 0},
  {name : 'hipFLEX' , value : 0, key : 0},
];


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

function goResult(category, value) {
    // 선택한 답안을 session 스토리지에 저장하기
  // Retrieve the array from session storage
  let answersDict = JSON.parse(sessionStorage.getItem('result')) || {};

  // Add the clicked answer ID to the array
  answersDict[category]=value

  // Store the updated array in session storage
  sessionStorage.setItem('answers', JSON.stringify(answersDict));
}


async function goNext(qqq) {
  const Qname=qqq.split("-")[0]
  const Qqid=qqq.split("-")[1]
  const aid=qqq.split("-")[2]
  a_num=(parseInt(aid)-16)%3
  const broker = { qqid: Qqid, aaid: aid };

  // 선택한 답안을 session 스토리지에 저장하기
  // Retrieve the array from session storage
  let answersArray = JSON.parse(sessionStorage.getItem('a')) || [];

  // Add the clicked answer ID to the array
  answersArray.push(Qname);

  // Store the updated array in session storage
  sessionStorage.setItem('a', JSON.stringify(answersArray));

  const csrftoken = getCookie('csrftoken');

  const url = '/qna/' + Qname +'/'+ Qqid + '/';
  await fetch(url, {
    method: 'POST',
    mode: 'same-origin',
    headers: { 'X-CSRFToken': csrftoken ,'Content-Type': 'application/json',},
    body : JSON.stringify(aid),
  })
    .then((response) => {
      if (!response.ok) {
        throw 'Error';
      }
      return response.json();
    })
    .then(data => {
        selected_caterogy = data['a'][a_num]['category']
        selected_value = parseInt(data['a'][a_num]['value'])

        let answersDict = JSON.parse(sessionStorage.getItem('r')) || {};

        // Add the clicked answer ID to the array
        // answersDict[selected_caterogy]=selected_value 
        if(answersDict[selected_caterogy]){
          answersDict[selected_caterogy] +=selected_value
          }
        else {
          answersDict[selected_caterogy] =selected_value
        }
      
        // Store the updated array in session storage
        sessionStorage.setItem('r', JSON.stringify(answersDict));

 
      // qna.innerHTML = data['q'];
      // console.log(answer[0].qid)
      // for (let i = 0; i < answer.length; i++) {
      //   answer[i].innerHTML = data['a'][i]['text'];
      //   answer[i].qid = data['q_id'].toString();
      //   // answer[i].removeEventListener('click', clickHandler); 
      //   // answer[i].addEventListener('click', clickHandler);
      // }
      // answerList.removeEventListener('click', clickHandler); 
      // answerList.addEventListener('click', clickHandler); // , {once:true}를 누르면, 오히려 오름차순 진행이 안됨

      // function clickHandler(event) {
      //   const q_id = event.target.qid;
      //   console.log(q_id)
      //   // x[data['a'][i].category]=data['a'][i].value;
      //   // console.log(x)

      //   if (q_id===endPoint.toString()){
      //     goResult()
      //     return;
      //   } 
      //   else {
      //     goNext(q_id + '-');
      //   }
    
          
      // }

    }).then(goResult())
//       .then(function(){
//         console.log('sss')
//         console.log(sessionStorage.getItem("r"));
//         const url = '/result'; // url로 최고값을 보내면 됨
//         fetch(url)
//           .then((response) => response.json())      
//           .then((data) => console.log(data));

//           // .then((data) => console.log(data));

//     }

// )


}
// console.log(sessionStorage.getItem('a'))
// sessionStorage.clear()
        
