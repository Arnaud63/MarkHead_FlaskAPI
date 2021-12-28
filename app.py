from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "/home/arnaud/Documents/Markhead_FlaskAPI/static/img/uploads"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            imagestr = image.stream
            app.logger.debug(imagestr)

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            return redirect(request.url)
            
    return render_template("upload_image.html", title="Uploading an image")