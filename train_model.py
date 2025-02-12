import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle

# Load the synthetic dataset
df = pd.read_csv('synthetic_bmi_data.csv')

# Encode the 'Fitness Goal' column into numerical values
le = LabelEncoder()
df['Fitness Goal'] = le.fit_transform(df['Fitness Goal'])

# Split the data into features (X) and target (y)
X = df[['Age', 'Weight', 'Height', 'BMI']]  # Features
y = df['Fitness Goal']  # Target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForestClassifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set and calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model for later use
with open('fitness_goal_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Save the label encoder for fitness goal
with open('fitness_goal_label_encoder.pkl', 'wb') as le_file:
    pickle.dump(le, le_file)

print("Model and label encoder saved.")
