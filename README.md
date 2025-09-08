# Hi there!
I’m your Localized AI Language Learning Partner (LALLP for short… yeah, I know, not the coolest name yet 😅).

Think of me as your friendly sidekick while you’re surfing the web or working.
Whenever you stumble upon a mysterious word or puzzling sentence, just highlight it and ask me.
I’ll happily explain, translate, give you examples, or even make up a mini quiz if you need more challenge! 

One day I might get a cooler name, but until then — LALLP’s got your back!

## Features

- Right-click lookup: Select text on any webpage and send it to GPT. 
- Side panel chat: Interact with GPT about the word (examples, grammar, synonyms, etc.). 
- Safe API usage: Your API key is stored only in the local backend, not exposed to the extension. 
- Streaming response: Text appears progressively, just like ChatGPT. 
- Customizable prompt: You can adjust the system prompt to make GPT behave like a dictionary, a grammar tutor, or a vocabulary trainer.

## Setup Instructions
1. Backend (FastAPI Proxy)

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a .env file in the root folder:
```bash
OPENAI_API_KEY=your_api_key_here
```

Run the server:
```bash
uvicorn server:app --reload --port 3030
```

The backend runs at http://localhost:3030.
2. Chrome Extension
- Open Chrome and go to chrome://extensions/. 
- Enable Developer Mode (toggle in the top-right). 
- Click Load unpacked and select the extension/ folder. 
- Now the extension is active.

## Usage
- Open any webpage.
- Highlight a word or phrase. 
- Right-click → Look up with GPT Directory. 
- A side panel will open, showing GPT’s response in real time. 
- You can keep chatting with GPT in the side panel to learn more.

## Security
- Your OpenAI API key is never exposed to the browser extension. 
- All requests go through the local FastAPI server. 
- You can add caching or logging in server.py if needed.

## Customization
- Change the GPT model in **`server.py`**:
```bash
"model": "gpt-4o-mini"
```
- Modify the system prompt in **`server.py`** to make GPT more like:
  - A dictionary 
  - A grammar corrector 
  - A language tutor
