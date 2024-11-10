const form = document.getElementById('form');
const submit = document.getElementById('submit');

function saveInfo(name, email, password, isAdmin, currency){
    localStorage.setItem('userData', JSON.stringify([name, email, password, isAdmin, currency]));
    window.location.href = "./login.html";
}

submit.onclick = (e) => {
    e.preventDefault();
    const { name, email, password, confirmPassword, adminChose, currency } = form.elements;
    if(password.value === confirmPassword.value && name.value && email.value && password.value){
        saveInfo(name.value, email.value, password.value, adminChose.value, currency.value);
    }
}

export default localStorage;
