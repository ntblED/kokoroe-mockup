const inputListen = document.getElementById("textinput");

let conversationHistory = [];

inputListen.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    const message = inputListen.value.trim();
    if (message) {
      document.getElementById("askbutton").click();
    }
  }
});

function SendPrompt() {
  const inputBar = document.getElementById("textinput");

  if (inputBar.value === "") {
    window.alert("You have to enter something, silly!");
    return;
  } else {
    CreateBubble(inputBar.value, true);
    AskAI(inputBar.value);

    inputBar.value = "";
  }
}

function CreateBubble(text, isUser = false) {
  const messageContainer = document.getElementById("messages");

  const bubbleDiv = document.createElement("div");
  bubbleDiv.classList.add("bubble");
  bubbleDiv.classList.add(isUser ? "user-message" : "ai-message");

  const bubbleText = document.createElement("p");
  bubbleText.textContent = text;

  bubbleDiv.appendChild(bubbleText);
  messageContainer.appendChild(bubbleDiv);

  messageContainer.scrollTop = messageContainer.scrollHeight;
}

async function AskAI(prompt) {
    document.getElementById("askbutton").disabled = true;
    const messageContainer = document.getElementById("messages");
    const loaderDIV = document.createElement("div");
    loaderDIV.classList.add("loader");

    const loaderGIF = document.createElement("img");
    loaderGIF.setAttribute("src", "/assets/loader.gif");
    loaderGIF.setAttribute("alt", "Our ai is thinking...");
    loaderGIF.setAttribute("width", "25%");


    loaderDIV.appendChild(loaderGIF);
    messageContainer.appendChild(loaderDIV);
    messageContainer.scrollTop = messageContainer.scrollHeight;

    const response = await fetch("http://localhost:80/api/ai-prompt", {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({ message: prompt, history: conversationHistory }),
    });


    const data = await response.json();
    console.log(data.reply);
    loaderDIV.remove();
    conversationHistory.push("USER: " + prompt);
    conversationHistory.push("AI Agent: " + data.reply);
    document.getElementById("askbutton").disabled = false;
    CreateBubble(data.reply, false)
    
}