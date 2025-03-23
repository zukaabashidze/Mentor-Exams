const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const placeholder = document.getElementById("empty-state");

const loadTasks = () => {
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    if (tasks.length === 0) {
        placeholder.style.display = "flex";
    } else {
        placeholder.style.display = "none"; 
        tasks.forEach(task => createTaskElement(task.text, task.completed, task.date, task.description));
    }
};

const handleSubmit = (e) => {
    e.preventDefault();
    handleAddTask();
};

const handleAddTask = () => {
    const taskText = taskInput.value.trim();
    const taskDescription = prompt("Enter task description:");  // Prompt to add description
    const currentDate = new Date().toLocaleString();  // Get current date and time

    if (taskText) {
        createTaskElement(taskText, false, currentDate, taskDescription);
        taskInput.value = "";  
    }
};

const createTaskElement = (taskText, isCompleted = false, taskDate = "", taskDescription = "") => {
    const li = document.createElement("li");

    const taskSpan = document.createElement("span");
    taskSpan.textContent = taskText;
    taskSpan.classList.add("task-text"); 

    const checkIcon = document.createElement("span");
    checkIcon.innerHTML = "&#x2713;";  
    checkIcon.style.display = isCompleted ? "inline" : "none";
    checkIcon.classList.add("check-icon");

    const dateSpan = document.createElement("span");
    dateSpan.textContent = taskDate ? `Added on: ${taskDate}` : ""; 
    dateSpan.classList.add("task-date");

    const descriptionSpan = document.createElement("span");
    descriptionSpan.textContent = taskDescription ? `Description: ${taskDescription}` : ""; 
    descriptionSpan.classList.add("task-description");

    li.appendChild(checkIcon);
    li.appendChild(taskSpan);
    li.appendChild(dateSpan);  
    li.appendChild(descriptionSpan);  // Add description to the list item

    const deleteButton = createDeleteButton(li);

    li.appendChild(deleteButton);

    if (isCompleted) {
        li.classList.add("completed"); 
    }

    li.onclick = () => toggleCompleteTask(li, checkIcon); 

    taskList.appendChild(li);

    updateLocalStorage(); 
    updatePlaceholder(); 
};

const createDeleteButton = (li) => {
    const deleteButton = document.createElement("button");
    deleteButton.innerHTML = "&times;";
    deleteButton.classList.add("delete-task");

    deleteButton.onclick = (e) => {
        e.stopPropagation();  
        deleteTask(li); 
    };

    return deleteButton;
};

const toggleCompleteTask = (li, checkIcon) => {
    li.classList.toggle("completed");  
    checkIcon.style.display = li.classList.contains("completed") ? "inline" : "none"; 

    updateLocalStorage();  
};

const deleteTask = (li) => {
    li.remove(); 
    updateLocalStorage(); 
    updatePlaceholder()
};

const updateLocalStorage = () => {
    const tasks = [...document.querySelectorAll("li")].map(li => ({
        text: li.querySelector(".task-text").textContent,
        completed: li.classList.contains("completed"), 
        date: li.querySelector(".task-date") ? li.querySelector(".task-date").textContent : "",
        description: li.querySelector(".task-description") ? li.querySelector(".task-description").textContent : ""
    }));
    localStorage.setItem("tasks", JSON.stringify(tasks)); 
};

const updatePlaceholder = () => {
    if (taskList.children.length === 0) {
        placeholder.style.display = "block";  
    } else {
        placeholder.style.display = "none";  
    }
};

taskInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        e.preventDefault();
        handleAddTask();
    }
});

loadTasks();
