let passwordButton = null
let noAuthButton = null
let passwordField = document.createElement('input')

if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addButtonListeners)
    }
    else {
    addButtonListeners
}

function addButtonListeners() {
    passwordButton = document.querySelector('button#password')
    passwordButton.addEventListener('click', addPasswordField)
    noAuthButton = document.querySelector('button#noAuth')
    noAuthButton.addEventListener('click', confirmNoAuth)
}

function confirmNoAuth(){
    if (window.confirm("Are you sure you want to create this user with no password?")) {
        let username = document.querySelector("input#user").value
        data = new FormData();
        data.append('username', username)
        return fetch('/login/new', {method: 'POST', body: data})
    }
    else {
    }
}

function addPasswordField() {
    let form = document.querySelector('form')
    form.appendChild(passwordButton)
    document.querySelector('button#noAuth').remove()
    form.insertBefore(passwordField, passwordButton)
    passwordField.outerHTML = "<input type=text name=password placeholder=Password>"
    passwordButton.outerHTML = "<input type=submit value='Create New User'>"
}