const form = document.getElementById('form');
const submit = document.getElementById('submit');

function saveInfo(name, email, password, isAdmin){
    localStorage.setItem('userData', JSON.stringify([name, email, password, isAdmin]));
    window.location.href = "./login.html";
}

submit.onclick = (g) => {
    g.preventDefault();
    const { name, email, password, confirmPassword, adminChose } = form.elements;
    if(password.value === confirmPassword.value && name.value && email.value && password.value){
        saveInfo(name.value, email.value, password.value, adminChose.value);
    }
}

export default localStorage;
