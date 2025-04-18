import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

MYSQL_HOST =os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_USER =os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD =os.getenv("MYSQL_PASSWORD", "YQYyqy171171")
MYSQL_DB =os.getenv("MYSQL_DB", "my_blog_db")


app = Flask(__name__,
            template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets'
            )
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
app.config['SECRET_KEY'] = 'YQYyqy171171'
db =SQLAlchemy(app)
login_manager = LoginManager(app)





from routes  import user_routes
from routes import admin_routes
