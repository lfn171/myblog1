from flask_login import login_required

from forms.article_form import ArticleForm
from models.article import Article
from routes import app
from flask import render_template, request, redirect, url_for, flash, abort

from services.article_service import ArticleService


#文章发布页面
@app.route('/create_article.html', methods=['GET', 'POST'])
@login_required
def create_article():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article =Article()
        new_article.title = form.title.data
        new_article.content= form.content.data
        try:
            article, error_msg = ArticleService().create_article(new_article)
            if error_msg:
                flash(f'发布文章错误: {error_msg}', category='danger')
            else:
                flash(f'发布文章完成', category='success')
                return redirect(url_for('home_page'))
        except Exception as error:
            flash(f'发布文章失败: {error}', category='danger')
    return render_template('edit_article.html', form=form, is_edit=False)

@app.route('/edit_article/<article_id>.html', methods=['GET', 'POST'])
@login_required
def edit_article(article_id:str):
    form = ArticleForm()
    if request.method == 'GET':
        try:
            article = ArticleService().get_article(int(article_id))
            if not article:
                flash('要找的文章没有找到', category='danger')
                return redirect(url_for('home_page'))
            else:
                form.title.data = article.title
                form.content.data = article.content
        except Exception as error:
            flash(f'提取文章失败: {error}', category='danger')
            return redirect(url_for('home_page'))
    if form.validate_on_submit():
        try:
            updated_article = Article()
            updated_article.id = int(article_id)
            updated_article.title = form.title.data
            updated_article.content = form.content.data

            article, error_msg = ArticleService().update_article(updated_article)
            if error_msg:
                flash(f'修改文章失败: {error_msg}', category='danger')
            else:
                flash(f'修改文章完成', category='success')
                return redirect(url_for('home_page'))
        except Exception as error:
            flash(f'修改文章失败: {error}', category='danger')

    return render_template('edit_article.html', form=form, is_edit=True)


#管理员登录
@app.route('/admin“')
def admin():
    return "admin"

@app.route('/lo', methods=['GET', 'POST'])
def login():
    return render_template("login.html")