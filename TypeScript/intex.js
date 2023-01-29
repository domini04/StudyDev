let 이름 = 'Shin';
// 이름 = 10; // Error
let 이름들 = ['Shin', 'Lee', 'Park', 'Kina'];
// 이름들.push(10); // Error
let 이름들2 = { name: 'Shin' }; // ?는 있어도 되고 없어도 되는 옵션 
이름들2 = { name: 'Lee' };
// 이름들2 = {age : 20}; // Error
이름들2 = {}; //?가 있어서 가능
let 이름들3 = { name: 'Shin', age: 30 };
이름들3 = { name: 'Lee', age: 20 };
let Shin = { name: 'Shin', age: 30 }; //Shin은 Person 타입만 받을 수 있다.
let Shin2 = { name: 'Shin', age: 33, Girlfriend: 'Kina' };
let multiType;
multiType = 20;
multiType = true;
let multiType2;
multiType2 = [20, true];
// multiType2 = ['123', false]; // Error
function 함수(x) {
    return x.length;
}
