from flask import Flask, Response
app = Flask(__name__)

@app.get("/dom4")
def dom4():
    html = """
    <div id="out"></div>
    <script>
      const p = new URLSearchParams(location.search);
      const v = p.get("v") || "";
      document.getElementById("out").innerHTML = v; // dangerous
    </script>
    """
    resp = Response(html, mimetype="text/html")
    # "better" mitigation attempt, but weak: allows inline scripts
    resp.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self' 'unsafe-inline'"
    return resp
