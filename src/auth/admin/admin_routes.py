from flask import Blueprint
from .admin_controller import getBooks

adminAuth = Blueprint("admin_routes", __name__)


# auth.add_url_rule('/register', "register", register_user, methods=["POST"])

# auth.add_url_rule("/login", "login", login_user, methods=["POST"])

# auth.add_url_rule("/logout", "logout", logout)

# adminAuth.add_url_rule("/getAll", "getAll", getBooks, methods=["GET"])


@adminAuth.route('/admin')
def admin_route():
    return 'Admin Route'
