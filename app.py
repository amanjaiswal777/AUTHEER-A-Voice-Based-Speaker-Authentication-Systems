import os
import sys

from train_audio import record_train
from test_audio import record_test
from flask import jsonify
from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from sklearn.externals import joblib
sys.path.append('../')
from main import get_id_result


import os
UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def hello_world():
    return render_template('default.html')

@app.route('/trainaudiosave',methods=['GET','POST'])
def trainaudiosave():
    print("\n\n\nRunning\n\n\n\n")
    record_train()
    return "done",200

@app.route('/testaudiosave',methods=['GET','POST'])
def testaudiosave():
    print("\n\n\nRunning\n\n\n\n")
    record_test()
    return "done",200
    
@app.route('/test',methods=['GET','POST'])
def trainaudio():
    print("\n\n\nRunning\n\n\n\n")
    a = get_id_result()
    data = {'status' : a}
    print(data)
    # response = app.response_class(
    #     response=data,
    #     status=200,
    #     mimetype='application/json'
    # )
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 3000);