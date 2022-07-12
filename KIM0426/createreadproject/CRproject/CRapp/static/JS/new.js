function check(){

let sum_value = 0;
let Study = document.getElementById('study').checked;
sum_value += Study;
let Social_club = document.getElementById('social_club').checked;
sum_value += Social_club;
let Project = document.getElementById('project').checked;
sum_value += Project;
let survey = document.getElementById('survey').checked;
sum_value += survey;

console.log(sum_value);
if(sum_value != 1){
    alert('모집 분야를 하나만 선택해 주세요');
    return location.reload();
}

let sum_status = 0;
let recruit = document.getElementById('is_recruit').checked;
sum_status += recruit;
let end = document.getElementById('is_end').checked;
sum_status += end;
console.log(sum_status);
if(sum_status != 1){
     alert('모집 상태를 하나만 선택해 주세요!');
     return location.reload();
}

let sum_face = 0;
let face = document.getElementById('face').checked;
sum_face += face;
let not_face = document.getElementById('notface').checked;
sum_face += not_face;
let not_yet = document.getElementById('notyet').checked;
sum_face += not_yet;

if(sum_face != 1){
    alert('대면/비대면 여부를 한가지만 선택해 주세요');
    return location.reload();
}



}