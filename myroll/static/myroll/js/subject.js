const body = document.querySelector('html body');
// const buttonOpen = document.getElementById('modalOpen');
const buttonOpen = document.getElementsByClassName('button');
const subjectName = document.getElementsByClassName('subjectName');

const modal = document.getElementById('easyModal');
const buttonClose = document.getElementsByClassName('modalClose')[0];

// const subject = getElementById('subject');
const subName = document.getElementById('subName');

// ボタンがクリックされた時
// buttonOpen.addEventListener('click', modalOpen);
// function modalOpen() {
//     modal.style.display = 'block';
//     body.style.backgroundColor = 'black';
// }

for(let i = 0; i < buttonOpen.length; i++) {
    function modalOpen() {
        modal.style.top = document.documentElement.scrollTop + 'px';
        modal.style.display = 'block';
        console.log(modal.style.top);
        console.log(document.documentElement.scrollTop);
        body.style.backgroundColor = 'black';
        subName.innerText = subjectName[i].textContent;
    }
    buttonOpen[i].addEventListener('click', modalOpen);
    // buttonOpen[i].onclick = function() {
    //     modal.style.display = 'block';
    //     // body.style.backgroundColor = 'black';
    //     // subName.innerText = subjectName[i];
    // }
}


// バツ印がクリックされた時
buttonClose.addEventListener('click', modalClose);
function modalClose() {
    modal.style.display = 'none';
    body.style.backgroundColor = 'white';
}

// モーダルコンテンツ以外がクリックされた時
addEventListener('click', outsideClose);
function outsideClose(e) {
    if (e.target == modal) {
        modal.style.display = 'none';
    }
}