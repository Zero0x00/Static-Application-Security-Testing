import html
from flask import Flask, request
app = Flask(__name__)

@app.get("/go")
def go():
    # better: HTML escaping
    url = html.escape(request.args.get("next", ""), quote=True)

    # but: putting user input into an attribute that influences navigation is risky,
    # and escaping doesn't validate that it's a safe URL
    return f'<a href="{url}">Continue</a>'
