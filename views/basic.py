from main import app

from flask import (
    render_template, send_from_directory,
)

import os


@app.route("/")
def main():
    return render_template('main.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

