from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/search", response_class=HTMLResponse)
def search(q: str = Query("")):
    html = f"<p>Results for: {q}</p>"
    return HTMLResponse(content=html)
