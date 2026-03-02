from flask import Flask, request
app = Flask(__name__)

DB = []

def strip_angles(s: str) -> str:
    # weak: destroys some tags but doesn't make output safe across contexts
    return s.replace("<", "").replace(">", "")

@app.post("/note")
def note():
    DB.append(strip_angles(request.form.get("note", "")))
    return "ok"

@app.get("/notes")
def notes():
    return "<br>".join(DB)  # still treating DB as safe HTML
