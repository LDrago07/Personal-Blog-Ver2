from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route("/")
def home():
    blog = "https://api.npoint.io/25087c5de55ee4339eff"
    response = requests.get(blog)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post/<blog_id>")
def get_blog(blog_id):
    post = Post(blog_id)
    return render_template("post.html", post=post.blog_post, blog_id=post.blog_id)

if __name__ == "__main__":
    app.run(debug=True)