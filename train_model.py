import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. LOCATE THE FILE (Automatic Check)
# Checking multiple locations to find the file
if os.path.exists("phishing.csv"):
    file_path = "phishing.csv"
elif os.path.exists("../data/phishing.csv"):
    file_path = "../data/phishing.csv"
elif os.path.exists("data/phishing.csv"):
    file_path = "data/phishing.csv"
else:
    print("❌ ERROR: 'phishing.csv' file not found!")
    print("Please move the CSV file to the same directory as this script.")
    exit()

print(f"✅ File found: {file_path}")
df = pd.read_csv(file_path)

# 2. CLEAN COLUMN NAMES
# Removing potential whitespace from column names (e.g., " URL_Length ")
df.columns = df.columns.str.strip()

# 3. SELECT FEATURES TO USE
# We are selecting only the features that can be extracted via Python code.
# These names must MATCH EXACTLY with the CSV column names.
cols_to_use = [
    'having_IP_Address',
    'URL_Length',
    'Shortining_Service',
    'having_At_Symbol',
    'double_slash_redirecting',
    'Prefix_Suffix',
    'having_Sub_Domain',
    'HTTPS_token'
]

# Check if columns exist in the CSV
missing_cols = [col for col in cols_to_use if col not in df.columns]
if missing_cols:
    print(f"❌ ERROR: The following columns were not found in CSV: {missing_cols}")
    print("Available columns:", df.columns.tolist())
    exit()

# 4. TRAINING
print("🚀 Training the model, please wait...")

X = df[cols_to_use]
y = df['Result'] # Target column

# Split data: 80% Training, 20% Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. TEST AND SAVE
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Trained Successfully! Accuracy: {acc*100:.2f}%")

joblib.dump(model, "phishing_model.pkl")
print("💾 Model saved as: phishing_model.pkl")