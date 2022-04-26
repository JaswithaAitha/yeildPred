from flask import Flask, request, render_template
from keras.models import load_model
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

file1 = open("=pickle file\\m5.pkl",'rb');
model1 = pickle.load(file1)
file1.close()
try:
    ct = pickle.load(open('pickle file\\ct10.pkl','rb'))
except Exception:
    pass

model = pickle.load(open('pickle file\\m5.pkl', 'rb'))

@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        
        Crop = (myDict['Crop'])

        Dist_id = int(myDict['Dist_id'])
        Year=int(myDict['Year'])
        Season=int(myDict['Season'])
        Season_yeild = int(myDict['Season_yeild'])
        X = np.array([[Crop,Dist_id,Year,Season,Season_yeild]])
        X_new = ct.transform(X)
        X_new
        X_perd = []
        y=1
        for i in X_new[0]:
            if y==1 or y==2 or y==3 :
                X_perd.append(float(i))
            else:
                X_perd.append(int(i))
                y+=1
        X_perd
        
        y = model.predict(np.array([X_perd]))
        return render_template('show1.html',inf=y) 
    return render_template('y-home.html')


@app.route('/index',methods=["GET","POST"])
def index():
  if request.method == "POST":
        myDict = request.form
        
        Crop = (myDict['Crop'])
        Dist_id = int(myDict['Dist_id'])
        Year=int(myDict['Year'])
        Season=int(myDict['Season'])
        Season_yeild = int(myDict['Season_yeild'])
        X = np.array([[Crop,Dist_id,Year,Season,Season_yeild]])
        X_new = ct.transform(X)
        X_new
        X_perd = []
        y=1
        for i in X_new[0]:
            if y==1 or y==2 or y==3 :
                X_perd.append(float(i))
            else:
                X_perd.append(int(i))
                y+=1
        X_perd
        
        y = model.predict(np.array([X_perd]))

        return render_template('show1.html',inf=y)
  return render_template('index.html')

if __name__ == "__main__":
     app.run(debug=True)