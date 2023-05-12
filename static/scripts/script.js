const items = document.querySelectorAll(".items")

console.log(items)

console.log("Hello")

items.addEventListener("click", () => {
  items.classList.toggle("crossed_off")
  console.log("Clicked")
})