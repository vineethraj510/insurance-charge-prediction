from flask import Flask,render_template,request
import pickle
from sklearn.ensemble import RandomForestRegressor
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method =='POST':
        
        #pickle_in = open("corona.pkl","rb")
        
        #
        
        age = request.form['age']
        BMI = request.form['BMI']
        Children = request.form['Children']
        Smoker = request.form['Smoker']
        Female = request.form['Female']
        NorthEast = request.form['NorthEast']
        NorthWest = request.form['NorthWest']
        SouthEast = request.form['SouthEast']
       

        #print('#-------------------------------data is here-------------------------------------#')
        #print(age,body,fever,cold,breath)
        
        rfr = pickle.load(open("insurance.pkl", "rb"))
        #columns  -- Age,	Fever,	BodyPains,	RunnyNose,	Difficulty_in_Breath
        data = [[int(age),float(BMI),int(Children),int(Smoker),int(Female),int(NorthEast),int(NorthWest),int(SouthEast)]]
        prediction = rfr.predict(data)[0]
        
        return render_template('index.html',prediction=round(prediction))
    else:
        
        return render_template('index.html',message='Something went wrong please check again and try')
              

if __name__ == '__main__':
    app.run(debug=True)