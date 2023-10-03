from flask import Blueprint
from models.auth_models import register_user, login_user, logout

auth = Blueprint("userAuth", __name__)


auth.add_url_rule('/register', "register", register_user, methods=["POST"])

auth.add_url_rule("/login", "login", login_user, methods=["POST"])

auth.add_url_rule("/logout", "logout", logout)
