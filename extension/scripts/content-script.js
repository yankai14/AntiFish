const coreApi = axios.create({
    baseURL: 'https://asia-southeast1-spry-sentry-340405.cloudfunctions.net',
});
  

document.addEventListener('click', function (e) {
    if (e.target.tagName == "A" || e.target.tagName == "a") {
        var url = e.target.href
        var text = e.target.text
        var parent = e.target.parentNode

        var exp = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi;
        var regex = new RegExp(exp)

        // const response = await coreApi.get("https://asia-southeast1-spry-sentry-340405.cloudfunctions.net")
        // alert(response.data)

        // call api here if unsafe then inject
        // var xhr = new XMLHttpRequest();
        // xhr.open("GET", "https://asia-southeast1-spry-sentry-340405.cloudfunctions.net/validateUrl", true);
        // xhr.onreadystatechange = function() {
        //     if (xhr.readyState == 4) {
        //         // JSON.parse does not evaluate the attacker's scripts.
        //         var resp = JSON.parse(xhr.responseText);
        //         alert(resp)
        //     }
        // }
        // xhr.onload = function() {
        //     alert("sdhifuish")
        // }
        // xhr.send({
        //     "url": "https://www.goldmansachs.com.sg/"
        // });

        // encodeURIComponent(flskdj)

        $.ajax({
            type: 'GET',
            url: 'https://asia-southeast1-spry-sentry-340405.cloudfunctions.net/validateUrl?url=https%3A%2F%2Fwww.goldmansachs.com.sg%2F',
            // dataType: 'json',
            // crossDomain: true,
            success: function(responseData, textStatus, jqXHR) {
                var value = responseData.fish;
                alert(value)
            },
            error: function (responseData, textStatus, errorThrown) {
                alert('GET failed.');
            }
        });
        
        if (regex.test(text)) {
            if (url == text || url == text + "/") {
                console.log("valid")
            } else {
                injectUnsafeBadge(parent, e.target.nextSibling)
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