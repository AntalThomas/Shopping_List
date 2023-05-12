var items = document.querySelectorAll(".items")

for (let i = 0; i < items.length; i++) {
    items[i].addEventListener("click", function (event) {
        event.target.classList.toggle("crossed_off")
    })
}