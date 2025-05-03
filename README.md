# Car Evaluation Machine Learning Project

## Overview

The Car Evaluation Machine Learning Project aims to predict the evaluation class of a car based on various features such as buying price, maintenance cost, number of doors, capacity, luggage boot size, and safety rating. This project utilizes a machine learning model built with Python and Flask to create a web application for user interaction.

## Technologies Used

- **Python**: Programming language used for the project.
- **Flask**: Web framework for building the web application.
- **Scikit-learn**: Machine learning library for model training and evaluation.
- **Pandas**: Data manipulation library for handling the dataset.
- **Joblib**: Library for saving and loading the trained model.
- **HTML/CSS**: Frontend technologies for creating the user interface.

## Dataset

The project uses the Car Evaluation dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/car+evaluation).

## Project Structure
/CarEvaluationProject ├── app.py # Flask application ├── train_model.py # Model training script ├── car_evaluation_model.pkl # Trained model file ├── encoder.pkl # Encoder file ├── favicon.ico # Favicon file └── /templates ├── index.html # Input form HTML └── result.html # Prediction result HTML


## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/CarEvaluationProject.git
   cd CarEvaluationProject

   Install Required Packages: Make sure you have Python installed, then install the required packages using pip:
   pip install -r requirements.txt

   Run the Model Training Script: Before running the application, train the model by executing:
   python train_model.py

   Run the Flask Application: Start the Flask application with:
   python app.py

   Access the Application: Open your web browser and go to http://127.0.0.1:5000/.
  
   
   Usage
On the home page, fill in the car features in the provided form.
Click the "Predict" button to see the predicted evaluation class of the car.
The result will be displayed on a new page.
Future Work
Improve the user interface with CSS or frameworks like Bootstrap.
Implement error handling for invalid inputs.
Deploy the application on platforms like Heroku or AWS.
Create comprehensive documentation for users.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to the UCI Machine Learning Repository for providing the dataset.
Thanks to the open-source community for the libraries and frameworks used in this project.
