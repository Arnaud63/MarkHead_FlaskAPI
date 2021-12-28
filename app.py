from flask import Flask, render_template, request, redirect
from deepface import DeepFace
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "/home/arnaud/Documents/MarkHead_FlaskAPI/static/img/uploads/"
app.config["ALIGNED_FACES"] = "/home/arnaud/Documents/MarkHead_FlaskAPI/static/img/aligned_faces/"

#Global variable for DeepFace : every detection algorithms
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']

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

@app.route("/analyse-image", methods=["GET", "POST"])
def analyse_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image :
                #app.logger.debug("image_name : ", image.filename)

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

                app.logger.debug("OK save")

                #img = cv2.imread(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

                #app.logger.debug("OK cv2")
                #app.logger.debug("type(img) :", type(img))
                #app.logger.debug("img.shape :", str(img.shape))

                #imagenp = np.fromstring(imagestr, np.uint8)

                try:
                    aligned_face=DeepFace.detectFace(os.path.join(app.config["IMAGE_UPLOADS"], image.filename), detector_backend=backends[1])
                    success=True
                except ValueError as e:
                    print(e)
                    print("No face found")
                    success=False

                if success:
                    print(type(aligned_face))
                    plt.imsave(os.path.join(app.config["ALIGNED_FACES"], image.filename), aligned_face)
                    #cv2.imwrite(os.path.join(app.config["ALIGNED_FACES"], image.filename), aligned_face)
                    return render_template("analyse_image.html", title="Analysing an image", img_path=os.path.join("static/img/aligned_faces", image.filename))
                else:
                    return redirect(request.url)
            
    return render_template("analyse_image.html", title="Analysing an image")