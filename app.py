# app.py
from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('car_evaluation_model.pkl')
encoder = joblib.load('encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [request.form['buying'], request.form['maint'], request.form['doors'], 
                request.form['persons'], request.form['lug_boot'], request.form['safety']]
    
    # Transform the input features
    features_encoded = encoder.transform([features]).toarray()
    prediction = model.predict(features_encoded)
    
    # Map prediction to class labels
    class_labels = ['unacc', 'acc', 'good', 'vgood']
    result = class_labels[prediction[0]]
    
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)