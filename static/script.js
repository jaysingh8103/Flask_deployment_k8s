async function fetchTasks() {
    let response = await fetch("/tasks");
    let tasks = await response.json();
    let taskList = document.getElementById("taskList");
    taskList.innerHTML = "";
    tasks.forEach(task => {
        let li = document.createElement("li");
        li.textContent = task.task;
        let deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.onclick = () => deleteTask(task.task);
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
    });
}

async function addTask() {
    let task = document.getElementById("taskInput").value;
    if (!task) return alert("Enter a task!");
    await fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task })
    });
    document.getElementById("taskInput").value = "";
    fetchTasks();
}

async function deleteTask(task) {
    await fetch("/delete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task })
    });
    fetchTasks();
}

fetchTasks();
