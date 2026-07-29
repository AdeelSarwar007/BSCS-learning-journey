async function askAI() {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "x-api-key": "YOUR_API_KEY"
        },
        body: JSON.stringify({
            model: "claude-sonnet-4-6",
            max_tokens: 100,
            messages: [{ role: "user", content: "Hello, kaise ho?" }]
        })
    });

    const data = await response.json();
    console.log(data);
}

askAI();