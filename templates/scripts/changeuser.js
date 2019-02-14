let usersURL = "http://smarthome/data/users.json";
let usersRequest = new XMLHttpRequest();


function changeUser(){
    let usersDiv = document.getElementById("userList");
    usersDiv.innerHTML = "";
    usersRequest.open('GET', usersURL);
    usersRequest.responseType = "json";
    usersRequest.send();
    usersRequest.onload = function() {
        let usersList = usersRequest.response;
        populateUsers(usersList);
    };
}
function populateUsers(myData){
    let userList = myData['users'];
    for(let i = 0; i < userList.length; i++){
        let newButton = document.createElement("button");
        newButton.insertAdjacentHTML("afterbegin", myData[i]);
        usersDiv.insertAdjacentHTML("beforeend", newButton)
    }

}
function newUser(){

}