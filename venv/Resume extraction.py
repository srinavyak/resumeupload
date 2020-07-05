import os
from flask import Flask, render_template, request
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")
#app.config["pydb_pdffiles"]="C:\Users\User\PycharmProjects\pydb\pdffiles"
@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, '\images')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for upload in request.files.getlist("file"):
        print(upload)
        filename = upload.filename
        destination = "/".join([target, filename])
        print(destination)
        upload.save(destination)

    return render_template("fileupld.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)
