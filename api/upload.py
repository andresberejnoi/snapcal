from everything import *
import time

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods = ["GET", "POST"])
def profile():
  if request.method == "POST":
    file = request.files['file']
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print("here")
      data = {"pizza": "500", "brocolli":"50"}
      #return "worked"
      return render_template("display.html", data=data)
    return "did not work"
  return render_template ("upload.html")
  