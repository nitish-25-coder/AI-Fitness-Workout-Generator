import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# Sample dataset (Can be replaced with a real dataset)
data = {
    'age': [25, 30, 35, 40, 22],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'height_cm': [175, 160, 180, 165, 170],
    'weight_kg': [70, 55, 85, 60, 68],
    'body_type': ['Ectomorph', 'Mesomorph', 'Endomorph', 'Ectomorph', 'Mesomorph'],
    'fitness_goal': ['Muscle Gain', 'Weight Loss', 'Endurance', 'Muscle Gain', 'Weight Loss'],
    'current_fitness_level': ['Beginner', 'Intermediate', 'Advanced', 'Beginner', 'Intermediate'],
    'suggested_workout': ['Strength Training', 'HIIT', 'Cycling', 'Strength Training', 'HIIT']
}

df = pd.DataFrame(data)

# Label Encoding categorical columns
label_encoders = {}
for column in ['gender', 'body_type', 'fitness_goal', 'current_fitness_level', 'suggested_workout']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le  # Save encoders for later decoding

# Save processed data and encoders
df.to_csv("processed_workout_data.csv", index=False)
pickle.dump(label_encoders, open("label_encoders.pkl", "wb"))

print("Data preprocessing completed!")
