let passwordButton = null
let noAuthButton = null
let passwordField = document.createElement('input')

if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addPasswordButtonListener)
    }
    else {
    addPasswordButtonListener
}

function addPasswordButtonListener() {
    passwordButton = document.querySelector('button#password')
    passwordButton.addEventListener('click', addPasswordField)
}

function addPasswordField() {
    let form = document.querySelector('form')
    form.appendChild(passwordButton)
    document.querySelector('input#noAuth').remove()
    form.insertBefore(passwordField, passwordButton)
    passwordField.outerHTML = "<input type=text name=password value=Password>"
    passwordButton.outerHTML = "<input type=submit value='Create New User'>"
}