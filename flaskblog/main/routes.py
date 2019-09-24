from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home_page():
    page = request.args.get("page", 1, type=int)
    # order_by(Post.date_posted.desc()) reorders the posts from latest to oldest
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=7)
    return render_template("home.html", posts=posts)


@main.route("/contactus")
def contact_us():
    return render_template("contactus.html", title="Contact Us")
