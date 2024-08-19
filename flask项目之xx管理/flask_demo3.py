from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
