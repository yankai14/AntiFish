$(document).ready(() => {
    var head = document.head;
    var link = document.createElement("link");
    link.type = "text/css";
    link.rel = "stylesheet";
    link.href = "../ui/bootstrap.css";
    head.appendChild(link);
});


document.addEventListener('click', function(e) {
    if (e.target.tagName == "A" || e.target.tagName == "a"){
        var url = e.target.href
        var text = e.target.text
        var parent = e.target.parentNode

        console.log(parent)
        
        var unsafeBadge = document.createElement("span")
        unsafeBadge.classList.add("badge", "badge-danger")
        unsafeBadge.textContent = "Unsafe!"

        
        parent.append(unsafeBadge)
        
        var exp = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi;
        var regex = new RegExp(exp)

        if (regex.test(text)) {
            if (url == text || url == text + "/"){
                console.log("valid")
            } else {
                alert("Possible phishing detected!")
                console.log("Phishing detected!")
                e.preventDefault()
            }
        } else {
            console.log("No match");
        }
    }
    e.stopPropagation();
    // e.preventDefault();
}, true);