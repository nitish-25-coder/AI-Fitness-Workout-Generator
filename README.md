# AI-Fitness-Workout-Generator

## Overview
This is a Flask-based web application that predicts a user's fitness goal (Gain Weight, Maintain Weight, or Lose Weight) based on their age, weight, and height. Based on the predicted goal, the application generates a personalized workout and diet plan.

## Features
- Accepts user input (age, weight, height) through a web form.
- Computes BMI from the provided data.
- Uses a trained machine learning model to predict the user's fitness goal.
- Provides a recommended workout and diet plan based on the predicted goal.
- Interactive web interface for easy user interaction.
- Model can be retrained with custom datasets.

## Prerequisites
Ensure you have the following installed before running the application:
- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Pickle

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/fitness-goal-prediction.git
   cd fitness-goal-prediction
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Ensure that the trained machine learning model (`fitness_goal_model.pkl`) and label encoder (`fitness_goal_label_encoder.pkl`) are present in the project directory.

## Usage
1. Run the Flask application:
   ```sh
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000/`.
3. Enter your age, weight, and height, then click "Generate Workout Plan" to receive personalized workout and diet recommendations.

## Project Structure
```
project/
│-- static/                         # Static assets (CSS, JS, Images)
│-- templates/                      # HTML templates
│   │-- index.html                  # Home page form for user input
│   │-- workout_plan.html           # Displays the workout and diet plan
│-- venv/                           # Virtual environment (if used)
│-- app.py                          # Main Flask application
│-- data_preprocessing.py           # Data preprocessing script
│-- generate_data.py                # Data generation script
│-- train_model.py                  # Model training script
│-- fitness_goal_model.pkl          # Trained ML model for fitness goal prediction
│-- fitness_goal_label_encoder.pkl  # Label encoder for decoding predictions
│-- label_encoders.pkl              # Additional label encoders
│-- processed_workout_data.xlsx     # Processed workout data file
│-- synthetic_bmi_data.xlsx         # Synthetic BMI data file
│-- requirements.txt                # Required dependencies
│-- README.md                       # Project documentation
```

## Model Training
If you need to retrain the model, follow these steps:
1. Collect a dataset with age, weight, height, BMI, and corresponding fitness goals.
2. Run `generate_data.py` to create synthetic training data.
3. Train a machine learning model (e.g., Decision Tree, Random Forest, or any classifier of choice) using `train_model.py`:
   ```sh
   python train_model.py
   ```
4. Save the trained model and label encoder:
   ```python
   import pickle
   pickle.dump(model, open("fitness_goal_model.pkl", "wb"))
   pickle.dump(label_encoder, open("fitness_goal_label_encoder.pkl", "wb"))
   ```
5. Ensure the files are placed in the project directory before running the application.

## License
This project is licensed under the MIT License.


