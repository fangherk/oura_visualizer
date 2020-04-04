import os

from flask import Flask, send_from_directory, url_for

app = Flask(__name__, template_folder="dist", static_folder="dist", static_url_path="")


@app.route("/")
def home():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(debug=True)
