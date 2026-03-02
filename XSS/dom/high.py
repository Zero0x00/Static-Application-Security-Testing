from flask import Flask
app = Flask(__name__)

@app.get("/dom3")
def dom3():
    return """
    <div id="out"></div>
    <script>
      // imagine DOMPurify is loaded (CDN or bundled)
      const p = new URLSearchParams(location.search);
      const html = p.get("html") || "";

      // better: sanitize
      const clean = DOMPurify.sanitize(html, { ALLOW_UNKNOWN_PROTOCOLS: true });

      // still risky: allowing unknown protocols can reintroduce dangerous URL behaviors
      document.getElementById("out").innerHTML = clean;
    </script>
    """
