from flask_login import login_user
from sqlalchemy import Select

from models.users import User
from routes import db


class UserService:
    def do_login(self, username:str, password:str) -> bool:
        query =Select(User).where(User.username == username)
        attempted_user =db.session.scalar(query)
        if attempted_user and attempted_user.check_password(password =password):
            login_user(attempted_user)
            return True
        return False