//Context : Context is a container that can be passed as an argument to a function.

//실행 Context : 실행되는 코드에 필요한 환경 정보를 제공하고 코드의 실행 결과를 실제로 관리하는 영역
  // 1. 생성 단계 : 실행 Context가 생성되는 단계
  // 2. 실행 단계 : 선언된 변수나 함수 등의 정보를 기반으로 코드가 실제로 실행되는 단계

  // record : 실행 Context가 생성되는 단계에서 선언된 변수나 함수 등의 정보를 기록하는 영역
  // Outer : 현재 실행 Context를 생성한 실행 Context에 대한 참조


//전역 Context : 전역에 선언된 변수와 함수를 관리하는 영역

// Lexical Scope 예제
let x = 'global';
function call1() {
  let x = 'local';
  call2(); // local이 아닌 global을 출력 : Lexical Context는 함수를 어디서 호출했는지가 아니라 어디에 선언했는지에 따라 결정된다.
}
function call2() {
  console.log(x); // global
}


function call3() {
  let x = 'local';
  call4(); // local 출력
  function call4() {
    console.log(x); // local 출력됨
  }
}

        // 활용
        // ver1 : 전역변수(값이 제대로 보존 되지 않을 수 있음)
let num = 0;

const increase = function() {
    // ver2 : 지역변수(호출될때마다 초기화)
    let num = 0;
    return ++num;
}

console.log(increase()); // 1
num = 10;
console.log(increase()); // 11
console.log(increase()); // 12

        // ver3 : 클로저를 활용(이전 상태 유지, 기능 동작)
const increase = (function(){
  let num = 0; // 클로저 영역에 저장된 변수

  return function() { // 클로저 영역에 저장된 함수
      return ++num;
  }
}());

  console.log(increase());
  num = 10;
  console.log(increase());
  console.log(increase());

const decrease = (function(){
    let num = 0;

    return function() {
        return --num;
    }
}());

  console.log(decrease()); // -1

      // 위 increase, decrease를 하나로 합치기
// const counter = (function(){
//     let num = 0;

//     return {
//         increase: function() {
//             return ++num;
//         },
//         decrease: function() {
//             return --num;
//         }
//     }
// } ());

console.log(counter.increase()); // 1
console.log(counter.increase()); // 2
console.log(counter.decrease()); // 1
console.log(counter.decrease()); // 0

//Ternary Operator(삼항연산자() : 조건 ? 참 : 거짓
// 위 counter함수를 decrease의 경우 0이하로 내려가지 않도록 수정. 삼항연산자 사용
const counter = (function(){
    let num = 0;

    return {
        increase: function() {
            return ++num;
        },
        decrease: function() {
            return num > 0 ? --num : 0;
        }
    }
}
