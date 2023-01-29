let 이름 : string = 'Shin';
// 이름 = 10; // Error

let 이름들 : string[] = ['Shin', 'Lee', 'Park', 'Kina'];
// 이름들.push(10); // Error

let 이름들2 : {name? : string} = {name : 'Shin'}; // ?는 있어도 되고 없어도 되는 옵션 
이름들2 = {name : 'Lee'};
// 이름들2 = {age : 20}; // Error
이름들2 = {} //?가 있어서 가능


type Person = {name : string, age : number};
let 이름들3 : Person = {name : 'Shin', age : 30};
이름들3 = {name : 'Lee', age : 20};
let Shin : Person = {name : 'Shin', age : 30}; //Shin은 Person 타입만 받을 수 있다.

type Person2 = {
  [key : string] : string | number; // Person2의 모든 key는 string이고 value는 string이거나 number이다.
}
let Shin2 : Person2 = {name : 'Shin', age : 33, Girlfriend : 'Kina'}

let multiType : number | boolean;
multiType = 20;
multiType = true;

let multiType2 : [number, boolean];
multiType2 = [20, true];
// multiType2 = ['123', false]; // Error


function 함수(x : string) : number { //string 타입의 x를 받아서 number 타입을 리턴
    return x.length;
}

