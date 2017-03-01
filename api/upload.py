from everything import *
from classify import run

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods = ["GET", "POST"])
def profile():
  if request.method == "POST":
    file = request.files['file']
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      file.save(image_path)
      data = run(image_path, cfg)
      os.remove(image_path)
      return render_template("display.html", data=data)
    return "did not work"
  return render_template ("upload.html")
  