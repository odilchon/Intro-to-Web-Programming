# Lab 1
# Part 1
from flask import Flask, render_template

app = Flask(__name__)

BOOK_DATA = [
    {"id": 101, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 102, "title": "Brave New World", "author": "Aldous Huxley"},
    {"id": 103, "title": "Moby-Dick", "author": "Herman Melville"}
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        books=BOOK_DATA,
        title="Book Collection"
    )

if __name__ == "__main__":
    app.run(debug=True)