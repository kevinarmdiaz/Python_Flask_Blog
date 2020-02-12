from flask import abort, render_template, current_app
from app.models import Post
from . import public_bp
from werkzeug.exceptions import NotFound
import logging

@public_bp.route("/")
def index():
    current_app.logger.info('Mostrando los posts del blog')
    posts = Post.get_all()
    print(posts)
    return render_template("public/index.html", posts=posts)

@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    current_app.logger.info('Mostrando un post')
    current_app.logger.info('Mostrando un post')
    current_app.logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if post is None:
        current_app.logger.info(f'El post {slug} no existe')
        abort(404)
    return render_template("public/post_view.html", post=post)

@public_bp.route("/error")
def show_error():
    res = 1/0
    posts = Post.get_all()
    return render_template("public/index.html",posts=posts)
