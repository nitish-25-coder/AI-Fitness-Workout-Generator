import pandas as pd
import numpy as np

# Function to categorize BMI and create corresponding fitness goal
def categorize_bmi(bmi):
    if bmi < 18.5:
        return 'Gain Weight'
    elif 18.5 <= bmi <= 24.9:
        return 'Maintain Weight'
    else:
        return 'Lose Weight'

# Generate synthetic data
data = []

# Generate data for different ages, weights, and heights
for age in range(18, 70):  # Age from 18 to 70 years
    for height in range(150, 200, 5):  # Height from 150 cm to 200 cm
        for weight in range(40, 150, 5):  # Weight from 40 kg to 150 kg
            bmi = weight / (height / 100) ** 2
            fitness_goal = categorize_bmi(bmi)
            data.append([age, weight, height, bmi, fitness_goal])

# Create a DataFrame from the generated data
df = pd.DataFrame(data, columns=['Age', 'Weight', 'Height', 'BMI', 'Fitness Goal'])

# Save the dataset to a CSV for use later
df.to_csv('synthetic_bmi_data.csv', index=False)
print("Synthetic data generated and saved to 'synthetic_bmi_data.csv'.")
