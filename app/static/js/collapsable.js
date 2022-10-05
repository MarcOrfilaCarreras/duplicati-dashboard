var c = document.getElementsByClassName("content-list-item-expand");

for (var i = 0; i < c.length; i++) {
    c[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}