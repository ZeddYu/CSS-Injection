import logging
from flask import Flask, request

# Turn off default logging by Flask.
l = logging.getLogger()
l.addHandler(logging.FileHandler("/dev/null"))

app: Flask = Flask(__name__)


@app.route('/')
def index():
    secret: str = request.args.get('secret', "")
    print("secret={}".format(secret))

    return "ok"


app.run(host="0.0.0.0", port=8081)