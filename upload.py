from flask import Flask, render_template, request, jsonify
#from werkzeug import secure_filename

#################################
# From command line:
# 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def post_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save((f.filename))
        result = {'status': 'OK', 'filename': f.filename,
            'points': [(0,0), (1,1)]}
        return jsonify(result)

    return 'Request not processed.'
