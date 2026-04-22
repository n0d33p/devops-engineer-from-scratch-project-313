import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import os
from flask import (
    Flask
)

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
app = Flask(__name__)
@app.route('/ping')
def pong():
    return 'pong'