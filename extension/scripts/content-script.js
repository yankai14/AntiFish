document.addEventListener('click', function(e) {
    if (e.target.tagName == "A" || e.target.tagName == "a"){
        var url = e.target.href;
        var text = e.target.text;
        
        var exp = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi;
        var regex = new RegExp(exp)

        if (regex.test(text)) {
            if (url == text || url == text + "/"){
                console.log("valid")
            }else{
                alert("Possible phishing detected!")
                console.log("Phishing detected!")
                e.preventDefault()
            }
        } else {
            console.log("No match")
        }
    }
    e.stopPropagation();
    // e.preventDefault();
}, true);