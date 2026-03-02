from flask import Flask, request, render_template_string
app = Flask(__name__)

DB = []

@app.post("/post")
def post():
    DB.append(request.form.get("body", ""))
    return "ok"

@app.get("/feed")
def feed():
    return render_template_string("""
      <h1>Feed</h1>
      {% for p in posts %}
        <div class="post">{{ p|safe }}</div>   {# stronger system, but bypassed by forcing safe #}
      {% endfor %}
    """, posts=DB)
