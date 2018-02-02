from everything import *

@app.route("/", methods = ["GET"])
def main():
  return render_template ("start.html")