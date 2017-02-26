from everything import *
import pprint

@app.route("/", methods=["GET"])
def hello_world():
  return "Hello World!"

"""
@app.route("/post", methods=["POST"])
def test_post():
  file = request.files['file']
  print file
  return "Worked"
"""

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/post', methods=['GET', 'POST'])
def upload_file():
    print "here0"
    if request.method == 'POST':
      
        # check if the post request has the file part
        #if 'file' not in request.files:
        #    return "no file"
        
        file = request.files['file']
        print file
        
        # if user does not select file, browser also
        # submit a empty part without filename
        
        #if file.filename == '':
        #    return "no file name"
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print "here"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "worked"
        
        return "did not work"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''