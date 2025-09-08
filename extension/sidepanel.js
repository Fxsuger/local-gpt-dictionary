document.addEventListener("DOMContentLoaded", () => {
  chrome.storage.local.get("selectedText", async (data) => {
    const queryDiv = document.getElementById("query");
    queryDiv.innerText = "Search: " + data.selectedText;

    const respDiv = document.getElementById("response");
    respDiv.innerText = "Waiting for GPT ...\n";

    const resp = await fetch("http://localhost:3030/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: data.selectedText })
    });

    const reader = resp.body.getReader();
    const decoder = new TextDecoder("utf-8");

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      const chunk = decoder.decode(value, { stream: true });
      try {
        const parsed = JSON.parse(chunk);
        const delta = parsed.choices[0].delta.content;
        if (delta) {
          respDiv.innerText += delta;
        }
      } catch (e) {
      }
    }
  });
});
