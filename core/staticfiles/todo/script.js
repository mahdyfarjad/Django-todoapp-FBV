{/* <script>
    // JavaScript function to add a new task
    function addTask() {
        var newTaskText = document.getElementById("newTask").value;
        if (newTaskText.trim() !== "") {
            var taskContainer = document.querySelector(".todo-container");
            var newTask = document.createElement("div");
            newTask.classList.add("task");
            newTask.innerHTML = `
                <span>${newTaskText}</span>
                <div class="task-buttons">
                    <button class="delete-btn" onclick="deleteTask(this)">Delete</button>
                    <button class="done-btn" onclick="markDone(this)">Done</button>
                </div>
            `;
            taskContainer.insertBefore(newTask, taskContainer.firstChild);
            document.getElementById("newTask").value = "";
        }
    }

    // JavaScript function to delete a task
    function deleteTask(button) {
        var task = button.parentNode.parentNode;
        task.remove();
    }

    // JavaScript function to mark a task as done
    function markDone(button) {
        var task = button.parentNode.parentNode;
        task.style.textDecoration = "line-through";
    }
</script> */}
