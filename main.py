from flask import Flask,render_template,jsonify,request
import pickle
from joblib import dump, load

app = Flask(__name__)




@app.route('/', methods = ['POST','GET'])
def home():
    return render_template('index.html')




@app.route('/predict', methods=['POST'])  # This will be called from UI
def math_operation():
    result = ""
    if (request.method=='POST'):
        try:
            CRIM = float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            INDUS = float(request.form['INDUS'])
            CHAS = float(request.form['CHAS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            AGE = float(request.form['AGE'])
            DIS = float(request.form['DIS'])
            RAD = float(request.form['RAD'])
            TAX = float(request.form['TAX'])
            PTRATIO = float(request.form['PTRATIO'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])

            filename = 'Boston_Prediction_Linear_Regression_Algorithm123.pickle'
            load_model = load(open(filename, 'rb'))
            prediction = load_model.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])

            return render_template('results.html', prediction=round(prediction[0]))
        except Exception as e:
            print('the exception msg is : ' , e)
            return "Something Went Wrong"
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
