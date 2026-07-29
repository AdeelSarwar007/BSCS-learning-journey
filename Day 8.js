const myNotes = `
University fee per semester: 80,000 PKR.
Library timing: 8 AM to 8 PM.
FYP submission deadline: Week 15 of 7th semester.
`;

async function askWithContext(question) {
    const prompt = `Yahan kuch information hai:\n${myNotes}\n\nIs information ke base par jawab dein: ${question}`;

    const response = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "x-api-key": "YOUR_API_KEY"
        },
        body: JSON.stringify({
            model: "claude-sonnet-4-6",
            max_tokens: 100,
            messages: [{ role: "user", content: prompt }]
        })
    });

    const data = await response.json();
    console.log("AI Ka Jawab:");
    console.log(data.content[0].text);
}

askWithContext("FYP submission kab hai?");