# server.py
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Local GPT Dictionary")

@app.get("/", include_in_schema=False)
def index():
    return HTMLResponse("""
        <html><head><title>Local GPT Dictionary</title></head>
        <body>
            <h1>Local GPT Dictionary</h1>
            <p>Try: <a href="/lookup?q=hello">/lookup?q=hello</a></p>
            <p>Open API docs: <a href="/docs">/docs</a></p>
        </body></html>
    """)

# example
@app.get("/lookup")
def lookup(q: str = Query(..., description="Word to look up")):
    # TODO: Call local dictionary/model logic
    return {"query": q, "definition": f"Definition of {q} (demo)"}

# 静态资源与 favicon
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    path = os.path.join("static", "favicon.ico")
    if os.path.exists(path):
        return FileResponse(path)
    return HTMLResponse("", status_code=204)
