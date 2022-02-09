import time
#from predict import Predict
from flask import Flask, render_template, request, flash
from flask_cors import CORS, cross_origin
app = Flask(__name__)  # object

app.secret_key = "super secret key"

import numpy as np
from joblib import dump, load

model = load(open('pre_model.pkl', 'rb'))


def Predict(c):
	c = np.array(c).reshape(1, -1)
	return model.predict(c)

@app.route('/', methods=['GET'])
@app.route('/home')
@cross_origin()
def home_page():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@cross_origin()
def index():
    try:
        if request.method == 'POST':
            area_income = float(request.form['area_income'])
            area_house_age = float(request.form['area_house_age'])
            area_number_of_rooms = float(request.form['area_number_of_rooms'])
            area_number_of_bedrooms = float(request.form['area_number_of_bedrooms'])
            area_population = float(request.form['area_population'])
            price = Predict([area_income, area_house_age, area_number_of_rooms, area_number_of_bedrooms, area_population])
            flash('Prediction is done!', 'success')
            return render_template('results.html', price=price)
    except Exception as e:
        print('The Exception message is:', e)
        flash('There is problem in your input!', 'danger')
        time.sleep(1)
        return render_template('404.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
