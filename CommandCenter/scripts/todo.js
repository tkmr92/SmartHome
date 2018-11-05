let tasksDiv = null;
let toDoURL =


function pageLoaded(){
    tasksDiv = document.getElementById("tasks");
};
function addNewTask(){
    let newTaskInstruct = document.createElement("p");
    let newTaskDesc = document.createElement("textarea");
    let submitButton = document.createElement("button");
    newTaskInstruct.textContent = "In the box provided, type the description of the task to be performed";
    submitButton.textContent = "Submit to ToDo List";
    submitButton.onclick = submitTask(newTaskDesc);
    tasksDiv.insertAdjacentElement("beforeend", newTaskInstruct);
    tasksDiv.insertAdjacentElement("beforeend", newTaskDesc);
    tasksDiv.insertAdjacentElement("beforeend", submitButton)
}
function submitTask(task){
    let toDoFile =

}