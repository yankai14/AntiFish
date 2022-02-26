
document.addEventListener('click', function (e) {
    if (e.target.tagName == "A" || e.target.tagName == "a") {
        var url = e.target.href
        var text = e.target.text
        var parent = e.target.parentNode

        var exp = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi;
        var regex = new RegExp(exp)

        if (regex.test(text)) {
            if (url == text || url == text + "/") {
                console.log("valid")
            } else {
                // alert("Possible phishing detected!")

                var unsafeBadge = document.createElement("div")
                var unsafeText = document.createElement("p")
                unsafeText.textContent = "Unsafe!"
                unsafeText.style.cssText = "color: #ffffff; font-size: 32%; font-weight: 600; font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;"
                unsafeBadge.style.cssText = "text-align: center; display: inline-block; vertical-align: baseline; white-space: nowrap; line-height: 0.001; padding-left: 5px; padding-right: 5px; border-radius: 6px; margin-left: 5px; background: #dc3545;"
                unsafeBadge.appendChild(unsafeText)

                parent.append(unsafeBadge)

                console.log("Phishing detected!")
                e.preventDefault()
            }
        } else {
            console.log("No match");
        }

        e.stopPropagation();
    }
    // e.preventDefault();
}, true);