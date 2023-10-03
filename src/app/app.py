from flask import Flask, make_response
from flask_cors import CORS
from .routers import routers

app = Flask(__name__)

# Initialize CORS with your app
CORS(app)

# Routers
routers(app, url_prefix="/api/v1")


@app.route('/')
def index():
    return "Server on running.."


def pindex():
    res = make_response("<h1>cookie is set</h1>")
    res.set_cookie('foo', 'bar')
    return res


app.add_url_rule("/hello", "hello", pindex)
