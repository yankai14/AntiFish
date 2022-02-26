// const coreApi = axios.create({
//     baseURL: 'https://asia-southeast1-spry-sentry-340405.cloudfunctions.net',
// });

document.addEventListener('click', function (e) {
    if (e.target.tagName == "A" || e.target.tagName == "a") {
        var url = e.target.href
        var text = e.target.text
        var parent = e.target.parentNode

        var validUrlExp = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi;
        var validUrlRegex = new RegExp(validUrlExp)

        var stripUrlExp = /(^https?:\/\/)?([\w.]+)(\/[\w.\/]*)?/
        var stripUrlRegex = new RegExp(stripUrlExp)
        console.log(text)
        var strippedUrl = stripUrlRegex.exec(url)[2]
        var strippedText = stripUrlRegex.exec(text)[2]
        console.log(strippedUrl)
        console.log(strippedText)

        var isFish = false

        var uriComp = encodeURIComponent(strippedUrl)
        // const response = await coreApi.get("https://asia-southeast1-spry-sentry-340405.cloudfunctions.net")
        // alert(response.data)
        $.ajax({
            type: 'GET',
            url: 'https://asia-southeast1-spry-sentry-340405.cloudfunctions.net/validateUrl?url=' + uriComp,
            success: function(responseData, textStatus, jqXHR) {
                console.log(responseData)
                isFish = responseData.fish
                if (isFish) {
                    console.log("i am a fish")
                    injectUnsafeBadge(parent, e.target.nextSibling)
                    e.preventDefault()
                }
            },
            error: function (responseData, textStatus, errorThrown) {
                console.log('GET failed.')
            }
        });

        if (!isFish && validUrlRegex.test(text)) {
            if (strippedUrl == strippedText) {
                console.log("URL == text")
            } else {
                isFish = true
                console.log("URL and text are different, possible phishing detected!")
                injectUnsafeBadge(parent, e.target.nextSibling)
                e.preventDefault()
            }
        } else {
            console.log("Text is not a URL")
        }
        
        if (isFish) {
            injectUnsafeBadge(parent, e.target.nextSibling)
            e.preventDefault()
        }

        e.stopPropagation();
    }
    // e.preventDefault();
}, true);

function injectUnsafeBadge(parent, nextSibling) {
    if (!parent.querySelector("#badge")) {
        var unsafeBadge = document.createElement("div")
        var unsafeText = document.createElement("p")
        unsafeText.textContent = "Unsafe!"
        unsafeText.style.cssText = "color: #ffffff; font-size: 32%; font-weight: 600; font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;"
        unsafeBadge.style.cssText = "text-align: center; display: inline-block; vertical-align: baseline; white-space: nowrap; line-height: 0.001; padding-left: 5px; padding-right: 5px; border-radius: 6px; margin-left: 5px; margin-right: 5px; background: #dc3545;"
        unsafeBadge.setAttribute("id", "badge")
        unsafeBadge.appendChild(unsafeText)

        parent.insertBefore(unsafeBadge, nextSibling)
    }
}