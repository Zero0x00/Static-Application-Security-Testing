from flask import Flask, request
app = Flask(__name__)

@app.get("/hello")
def hello():
    name = request.args.get("name", "")
    return "<h1>Hello " + name + "</h1>"
