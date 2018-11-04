let usersDiv = document.getElementById("userlist");
let usersURL = "http://smarthome/data/users.json";
let usersRequest = new XMLHttpRequest();

function changeUser(){
    usersDiv.innerHTML = "";
    usersRequest.open('GET', usersURL);
    usersRequest.send();
    usersRequest.onload = function() {
        let usersList = usersRequest.response;
        populateUsers(usersList);
    };
}
function populateUsers(jsonArray){
    for(let i = 0; i < jsonArray.length; i++){
        let newButton = document.createElement("button");
        newButton.insertAdjacentHTML("afterbegin", jsonArray[i]);
        usersDiv.insertAdjacentHTML("beforeend", newButton)
    }

}
function newUser(){

}