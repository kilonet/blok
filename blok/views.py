# -*- coding: utf-8 -*-
from blok.models.Post import Post
from werkzeug import redirect
from datetime import datetime
from mongoengine.fields import DateTimeField
from blok.models.Comment import Comment


__author__ = 'kilonet'
from werkzeug import redirect, Response
from werkzeug.exceptions import NotFound
from utils import render_template
import math


PAGE_SIZE = 5

def comments (request):
    id = request.args['id']
    post = Post.objects (id = id).first ()
    return render_template('comments.html', comments=post.comments)

def comment (request):
    if request.method == 'POST':
        post = Post.objects(id = request.form.get ('id')).first ()
        comment = Comment (text = request.form.get ('text'), date = datetime.now ())
        post.comments.append (comment)
        post.save ()
        return Response ()
    raise NotFound ()


def index(request, page_id = 1):
    begin = (page_id-1) * PAGE_SIZE
    end = begin + PAGE_SIZE
    posts = Post.objects[begin:end].order_by ("-date")
    pages_total = int (math.ceil (float (Post.objects () .count ()) / PAGE_SIZE))
    return render_template('index.html', posts=posts, pages_total=pages_total, page_index=page_id)

def add (request):
    if request.method == 'GET':
        return render_template ('add.html')
    elif request.method == 'POST':
        post = Post (
                text=request.form.get ('message'),
                user_name=request.form.get ('name'),
                title=request.form.get ('title'),
                date = datetime.now())
        post.save ()
    return redirect ("/")

  