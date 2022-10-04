from flask import Flask, render_template
from post import Post
import requests
import datetime


app = Flask(__name__)

posts = requests.get("https://api.npoint.io/86470bbc427d79dc9b1f").json()
all_post = []
for post in posts:
    post_data = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_post.append(post_data)

current_date = datetime.datetime.now()
current_year = current_date.strftime("%Y")


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_post, CURRENT_YEAR=current_year)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_post:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, CURRENT_YEAR=current_year)


if __name__ == "__main__":
    app.run(debug=True)
