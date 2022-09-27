from flask import Flask, render_template, request, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from PIL import Image
import cv2
#def run():

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcd"
app.config["UPLOADED_PHOTOS_DEST"] = "uploads"

photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators = [
            FileAllowed(photos, "Only images are allowed"),
            FileRequired("File should not be empty")
        ]
    )
    submit = SubmitField("Upload")

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOADED_PHOTOS_DEST"], filename)


@app.route("/", methods = ["GET", "POST"])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        output = request.form.to_dict()
        name = output["name"]
        age = output["age"]
        print("Name:", name)
        print("Age:", age)
        filename = photos.save(form.photo.data)
        file_url = url_for("get_file", filename = filename)
        directory = r"D:\VIBHAV\AIKYA\Detecting_dyslexia-main\Detecting_dyslexia-main"
        img = cv2.imread(directory + file_url)
        cv2.imwrite(r"D:\VIBHAV\AIKYA\Detecting_dyslexia-main\Detecting_dyslexia-main\uploads" + "\\" + filename, img)
    else:
        file_url = None
    return render_template("front.html", form = form, file_url = file_url)


if __name__ == "__main__":
    app.run(debug = True, port = 6969)