import re
from flask import Flask, request
app = Flask(__name__)

def strip_script_tags(s: str) -> str:
    # weak: blacklist-style removal (misses many vectors/contexts)
    return re.sub(r"(?is)<\s*script.*?>.*?<\s*/\s*script\s*>", "", s)

@app.get("/search")
def search():
    q = strip_script_tags(request.args.get("q", ""))
    return f"<p>Results for: {q}</p>"
