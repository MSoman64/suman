function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        let chatBox = document.getElementById("chat-box");

        chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;
        chatBox.innerHTML += `<p><b>Bot:</b><pre>${data.reply}</pre></p>`;

        input.value = "";
    });
}
