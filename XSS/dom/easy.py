from flask import Flask
app = Flask(__name__)

@app.get("/dom1")
def dom1():
    return """
    <div id="out"></div>
    <script>
      const p = new URLSearchParams(location.search);
      document.getElementById("out").innerHTML = p.get("msg"); // no mitigation
    </script>
    """
