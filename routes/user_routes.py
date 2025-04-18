from flask_login import logout_user, current_user
from unicodedata import category

from forms.delete_article_form import DeleteArticleForm
from forms.login_form import LoginForm
from routes import app
from flask import render_template, abort, url_for, flash,redirect
from services.article_service import ArticleService
from services.user_service import UserService


# @app.route('/')
# @app.route('/index')
# def home_page():
#     articles = ArticleService().get_all_articles()
#     return render_template('index.html', articles=articles)



@app.route("/about")
def about_page():
    return render_template('about.html')


#文章详情页面
@app.route("/article/<article_id>.html")
def article_page(article_id):
    article_service = ArticleService()
    # 调用实例方法
    article = article_service.get_article(article_id)
    if article :
        return render_template('article.html', article=article)
    abort(404)

@app.route('/login.html', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        result =UserService().do_login(username=form.username.data, password=form.password.data)
        if result :
            flash(f'欢迎{form.username.data}回来',category='success')
            return redirect(url_for('home_page'))
        else:
            flash('用户名或者密码错误，请重试',category='danger')
    return render_template('login.html', form=form)

@app.route('/logout.html')
def logout_page():
    logout_user()
    return redirect(url_for('home_page'))


@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def home_page():
    if current_user.is_authenticated:
        delete_article_form = DeleteArticleForm()
        if delete_article_form.validate_on_submit():
            if delete_article_form.validate_on_submit():
                result, error = ArticleService().delete_article(int(delete_article_form.article_id.data))
                if result:
                    flash(f'成功删除文章', category='success')
                    return redirect(url_for('home_page'))
                else:
                    flash(f'删除文章失败: {error}', category='danger')

    articles = ArticleService().get_articles()

    if current_user.is_authenticated:
        return render_template('index.html', articles=articles, delete_article_form=delete_article_form)

    return render_template('index.html', articles=articles)

