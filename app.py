from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load the trained machine learning model
model_path = os.path.join(os.getcwd(), "fitness_goal_model.pkl")
label_encoder_path = os.path.join(os.getcwd(), "fitness_goal_label_encoder.pkl")

if not os.path.exists(model_path) or not os.path.exists(label_encoder_path):
    raise FileNotFoundError("Model or Label Encoder file is missing. Please generate them first.")

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(label_encoder_path, 'rb') as le_file:
    le = pickle.load(le_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_workout', methods=['POST'])
def generate_workout():
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = weight / (height / 100) ** 2
    
    input_data = pd.DataFrame([[age, weight, height, bmi]], columns=['Age', 'Weight', 'Height', 'BMI'])
    prediction = model.predict(input_data)
    fitness_goal = le.inverse_transform(prediction)[0]
    
    exercises = {
        "Gain Weight": {
            "Strength training": [
                "Push-ups", "Bench Press", "Squats", "Deadlifts", "Overhead Press", 
                "Pull-ups", "Dumbbell Rows", "Triceps Dips", "Barbell Rows", "Dumbbell Press",
                "Leg Press", "Bicep Curls", "Tricep Pushdowns", "Lunges", "Bulgarian Split Squats",
                "Seated Shoulder Press"
            ],
            "High-protein diet": [
                "Chicken", "Eggs", "Fish", "Greek Yogurt", "Tofu", "Lentils", "Nuts", 
                "Cottage Cheese", "Beef", "Salmon", "Chickpeas", "Quinoa", "Tofu Scramble", 
                "Peanut Butter", "Edamame"
            ]
        },
        "Maintain Weight": {
            "Cardio": [
                "Running", "Cycling", "Swimming", "Rowing", "Jump Rope", "Hiking", "Walking", 
                "Skating", "Dancing", "Stair Climbing", "Rowing Machine", "Kickboxing", 
                "Aerobics"
            ],
            "Balanced diet": [
                "Fruits", "Vegetables", "Whole Grains", "Lean Meats", "Nuts", "Avocados", 
                "Sweet Potatoes", "Almonds", "Eggs", "Brown Rice", "Salmon", "Beans", "Leafy Greens"
            ]
        },
        "Lose Weight": {
            "Cardio": [
                "Jogging", "HIIT", "Elliptical Trainer", "Kickboxing", "Sprints", "Stair Climbing", 
                "Jump Rope", "Running Intervals", "Cycling Intervals", "Walking at an Incline", 
                "Zumba", "CrossFit", "Hiking"
            ],
            "Low-calorie diet": [
                "Leafy greens", "Lean protein", "Berries", "Quinoa", "Oats", "Cucumbers", 
                "Asparagus", "Tomatoes", "Bell Peppers", "Spinach", "Cauliflower", "Chicken Breast", 
                "Shrimp"
            ]
        }
    }
    
    return render_template('workout_plan.html', fitness_goal=fitness_goal, exercises=exercises.get(fitness_goal, {}))

if __name__ == '__main__':
    app.run(debug=True)
