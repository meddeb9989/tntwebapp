#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template, url_for
from datetime import timedelta
import config

app = Flask(__name__)

app.config.from_object(config)


def split_value(string):
    return string.split(";")[0]

def split_id(string):
    return string.split(";")[1]

app.jinja_env.filters['split_value'] = split_value
app.jinja_env.filters['split_id'] = split_id

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found(error):
    print error
    return render_template('500.html'), 500

@app.context_processor
def inject_static_assets_url():
    return dict(STATIC_ASSETS_URL=url_for("static", filename="assets"))


@app.context_processor
def inject_static_media_url():
    return dict(STATIC_MEDIA_URL=url_for("static", filename="media"))

import webapp.views


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
