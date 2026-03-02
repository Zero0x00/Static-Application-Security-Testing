from flask import Flask
app = Flask(__name__)

@app.get("/dom2")
def dom2():
    return """
    <div id="out"></div>
    <script>
      const p = new URLSearchParams(location.search);
      let msg = p.get("msg") || "";

      // weak: blacklist
      msg = msg.replace(/<\\s*script/gi, "");

      document.getElementById("out").innerHTML = msg; // still dangerous sink
    </script>
    """
