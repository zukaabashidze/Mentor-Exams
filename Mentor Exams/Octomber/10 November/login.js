import localStorage from "./register.js";

const info = JSON.parse(localStorage.getItem('info'));
const form1 = document.getElementById('form1');
const submit = document.getElementById('submit');

submit.addEventListener('click', function(e){
    e.preventDefault();
    const name1 = form1.elements.name.value;
    const email = form1.elements.email.value;
    const password = form1.elements.password.value;
    const adminChose = form1.elements.adminChose.value;
    if(name1 == info[0] && email == info[1] && password == info[2] && adminChose == info[3]){
        window.location.href = "./index.html";
    } else {
        console.log(undefined);
    }
})

console.log(info);

export default info;