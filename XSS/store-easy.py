from flask import Flask, request, render_template_string

app = Flask(__name__)
COMMENTS = []  # imagine this is a DB

@app.post("/comment")
def add_comment():
    COMMENTS.append(request.form.get("text", ""))
    return "ok"

@app.get("/comments")
def show_comments():
    return render_template_string("""
        <ul>
        {% for c in comments %}
          <li>{{ c|safe }}</li>
        {% endfor %}
        </ul>
    """, comments=COMMENTS)
