submitButton = null

if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addButtonListeners)
    }
    else {
    addButtonListeners
}

function addButtonListeners() {
    submitButton = document.querySelector("button#submit")
    submitButton.addEventListener("click", confirmNoAuth)
}

function confirmNoAuth(){
    let username = document.querySelector("input#user").value
    let password = document.querySelector("input#password").value
    let myForm = document.createElement('FORM')
    let user = document.createElement('input')
    user.name = "username"
    user.value = username
    let pass = document.createElement('input')
    pass.name = "password"
    pass.value = password
    myForm.method = 'POST'
    myForm.action = '/login/new'
    myForm.appendChild(user)
    myForm.appendChild(pass)
    if(password === '') {
        if(window.confirm("Are you sure you want to create this user with no password?")) {
            document.querySelector("body").appendChild(myForm)
            myForm.submit()
            document.querySelector("body").removeChild(myForm)
            return
        }
        else {
        }
    }
    else {
            document.querySelector("body").appendChild(myForm)
            myForm.submit()
            document.querySelector("body").removeChild(myForm)
            return
    }
}