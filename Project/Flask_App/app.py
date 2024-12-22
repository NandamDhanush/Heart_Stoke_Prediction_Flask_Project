from flask import Flask, request, render_template 
import joblib 
import numpy as np
app = Flask(__name__)
model = joblib.load("E:\\12c7\Heart_Stoke_Prediction_Flask_Project-master\Project\Training\model")
label1 = joblib.load ("E:\\12c7\Heart_Stoke_Prediction_Flask_Project-master\Project\Training\mar_transform")
label2 = joblib.load("E:\\12c7\Heart_Stoke_Prediction_Flask_Project-master\Project\Training\\res_transform")
column=joblib.load ("E:\\12c7\Heart_Stoke_Prediction_Flask_Project-master\Project\Training\column")
app = Flask(__name__)
@app.route('/')
def predict():
    return render_template("Manual_Predict.html")

@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test = [[(x) for x in request.form.values()]]
    print('actual',x_test)
    x_test=np.array(x_test)
    x_test[:,4]=label1.transform(x_test[:,4])
    x_test[:,6]=label2.transform(x_test[:,6])
    x_test=column.transform(x_test)
    pred = model.predict (x_test)
    print(pred)
    if(pred[0]==0):
        result="no chances of stroke"
    else:result="chances of stroke"
    return render_template('Manual_Predict.html', \
    prediction_text=('There are \
        ',result))
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)