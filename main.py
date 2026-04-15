from flask import (
    get_flashed_messages,
    flash,
    Flask,
    redirect,
    render_template,
    request,
    url_for
)
from dotenv import load_dotenv

app = Flask(__name__)
@app.route('/ping')
def pong():
    return 'pong'