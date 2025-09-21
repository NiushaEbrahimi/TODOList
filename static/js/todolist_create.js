document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    form.addEventListener("click", (event) => {
        if (event.target.classList.contains("add-item")) {
            event.preventDefault();

            const child = event.target;
            let child_id = Number(child.id);
            const parent = child.parentNode;

            const todoElement = `
                <input type="text" placeholder="Todo item..." name="item_title[]" class="todo-job-title" required>
                <label for="add-item">Due Date:</label>
                <input type="date" name="item_end_date[]" class="todo-date">
                <button type="delete" class="delete-button">delete</button>
            `;
            child_id += 1;

            const next_input = `
                <div class="item-container" id="${child_id}">
                    <button type="button" class="add-item" id="${child_id}">+</button>
                </div>
            `;
            child.classList.add("invisble");
            parent.classList.add("item-container-after");
            parent.insertAdjacentHTML("beforeend", todoElement);
            parent.insertAdjacentHTML("afterend", next_input);
        }
    });
});
