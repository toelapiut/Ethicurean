from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db, photos
from flask_login import login_required,current_user
from ..models import User,Comment,Blog
from .forms import Comments,Bloger,UpdateProfile

@main.route('/')
def index():

    title="Ethicurean"
    all_blogs=Blog.query.all()

    print(len(all_blogs))
  
    return render_template('index.html',title=title,blog=all_blogs)


@main.route('/comment/<int:id>',methods=['GET','POST'])
@login_required
def add_comment(id):
    form_comment=Comments()
    blog=Blog.query.all()
    comment =Comment.query.filter_by(blog_id=id)
    if form_comment.validate_on_submit():
        feedback=form_comment.comments.data

        new_comment=Comment(review=feedback,user=current_user)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('comment.html',form=form_comment,comment=comment,blog=blog)

@main.route('/blog',methods=['GET','POST'])
@login_required
def add_blog():
    form_blog=Bloger()

    all_blogs=Blog.query.all()

    if form_blog.validate_on_submit():
        blog_title=form_blog.title.data
        blog_body=form_blog.blog.data
        print(blog_title)

        new_blog=Blog(title=blog_title,blog=blog_body,user=current_user)
        new_blog.save_blog()

    return render_template('blog.html',form=form_blog,blog=all_blogs)

@main.route('/user/<uname>')
def profile(uname):
    user =User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required

def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form=UpdateProfile()

    if form.validate_on_submit:
        user.bio=form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form=form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
