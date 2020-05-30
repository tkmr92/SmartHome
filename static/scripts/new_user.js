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
    data = new FormData()
    data.append('username', username)
    data.append('password', password)
    if(password === '') {
        if(window.confirm("Are you sure you want to create this user with no password?")) {
            return fetch('/login/new', {method: 'POST', body: data})
        }
        else {
        }
    }
    else {
        return fetch('/login/new', {method: 'POST', body: data})
    }
}