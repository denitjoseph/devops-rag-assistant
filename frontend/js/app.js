const questionInput = document.getElementById("question");
const sendButton = document.getElementById("send-btn");
const chatBox = document.getElementById("chat-box");


function addMessage(message, type) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");

    if (type === "user") {
        messageDiv.classList.add("user-message");
    } else {
        messageDiv.classList.add("bot-message");
    }

    const sender = type === "user"
        ? "You:"
        : "AI Assistant:";

    messageDiv.innerHTML = `
        <strong>${sender}</strong>
        <p>${message}</p>
    `;

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendQuestion() {

    const question = questionInput.value.trim();

    if (question === "") {
        return;
    }

    addMessage(question, "user");

    questionInput.value = "";

    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong");
        }

        addMessage(data.answer, "bot");

    } catch (error) {

        addMessage(
            "Error: " + error.message,
            "bot"
        );

    }
}


sendButton.addEventListener("click", sendQuestion);


questionInput.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendQuestion();
    }

});