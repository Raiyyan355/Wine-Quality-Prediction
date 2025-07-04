from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load your pre-trained stacked classifier
with open('stacked_model.joblib', 'rb') as f:
    model = joblib.load(f)

# Home page route (GET)
@app.route('/')
def index():
    return render_template('index.html', prediction=None)

# Prediction route (POST)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [
            float(request.form['fixed_acidity']),
            float(request.form['volatile_acidity']),
            float(request.form['citric_acid']),
            float(request.form['residual_sugar']),
            float(request.form['chlorides']),
            float(request.form['free_sulfur_dioxide']),
            float(request.form['total_sulfur_dioxide']),
            float(request.form['density']),
            float(request.form['pH']),
            float(request.form['sulphates']),
            float(request.form['alcohol'])
        ]
        arr = np.array(features).reshape(1, -1)
        pred = model.predict(arr)[0]
        prediction = f"Predicted Wine Quality: {pred}"
    except Exception as e:
        prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

