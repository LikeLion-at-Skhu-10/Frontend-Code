function formsubmit(){
    const Monday = document.getElementById('Monday');
    const Tuesday = document.getElementById('Tuesday');
    const Wednesday = document.getElementById('Wednesday');
    const Thursday = document.getElementById('Thursday');
    const Friday = document.getElementById('Friday');
    const Saturday = document.getElementById('Saturday');
    const Sunday = document.getElementById('Sunday');

    const starttime = document.getElementById('starttime').value;
    const endtime = document.getElementById('endtime').value;
    const name = document.getElementById('name_study').value;

    if(starttime == ''){
        return alert('시작시간을 선택해 주세요');
    }
    else if(endtime == ''){
        return alert('끝나는 시간을 선택해 주세요');
    }


}