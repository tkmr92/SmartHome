//let loginDiv = null
//let newUserButton = null
//let body = null
//
//const newUserForm = document.createElement('field')
//
//if(document.readyState === 'loading'){
//    document.addEventListener('DOMContentLoaded', runQuerySelectors)
//    }
//    else {
//    runQuerySelectors
//    }
//
//function runQuerySelectors() {
//    loginDiv = document.querySelector('div.login')
//    newUserButton = document.querySelector('button.newUserButton')
//    body = document.querySelector('body')
//    addLoginListeners()
//}
//
//function addLoginListeners() {
//    newUserButton.addEventListener('click', createNewUser)
//}
//
//function createNewUser() {
//    loginDiv.remove()
//    body.appendChild(newUserForm)
//    newUserForm.outerHTML = '<form method="post"><input type=text name=username><button>Use Password Authentication</button><input type=submit value="Use No Authentication"></form>';
//}