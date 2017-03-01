from everything import *

@app.route("/display", methods = ["GET"])
def display():
  if request.method == "GET":
    data = {"pizza": "500", "brocolli":"50"}
    return render_template ("display.html", data=data)