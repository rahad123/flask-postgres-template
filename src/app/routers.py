# from routes.common import common
# from routes.airport_routes import airport
# from routes.test import route
from src.auth.admin import admin_routes
# from auth.user import user_routes


def routers(app, url_prefix):
    app.register_blueprint(admin_routes, url_prefix=f"{url_prefix}/adminAuth")
    # app.register_blueprint(user_routes, url_prefix=f"{url_prefix}/auth")
    # app.register_blueprint(airport, url_prefix=f"{url_prefix}/airports")
    # app.register_blueprint(flight, url_prefix=f"{url_prefix}/flights")
    # app.register_blueprint(common, url_prefix=url_prefix)
    # app.register_blueprint(route, url_prefix=url_prefix)
