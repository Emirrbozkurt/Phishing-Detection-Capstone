# 🛡️ Phishing Detection System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange)
![Status](https://img.shields.io/badge/Status-Capstone%20I%20Completed-success)

## 📌 Overview
This repository contains the source code and documentation for the **Phishing Detection System**, developed as part of the **COE401 - Capstone Project I** at **Istinye University**.

The project aims to detect phishing URLs using machine learning techniques. It analyzes various lexical and domain-based features of a URL to classify it as either **Legitimate** or **Phishing**.

## 🚀 Key Features
* **Machine Learning Model:** Uses Random Forest/Decision Tree algorithms to predict URL legitimacy.
* **Feature Extraction:** Analyzes URL length, special characters (@, //), domain age, and more.
* **Web Interface:** A user-friendly web application built with **Flask** for real-time testing.
* **Data Visualization:** Includes scripts to visualize the dataset distribution (Legitimate vs. Phishing).

## 📂 Project Structure
Here is an overview of the files in this repository:

| File Name | Description |
| :--- | :--- |
| `app.py` | The main Flask application script for the web interface. |
| `train_model.py` | Script to preprocess the dataset and train the ML model. |
| `predict.py` | Inference engine that loads the saved model and predicts new URLs. |
| `phishing.csv` | The dataset used for training and testing. |
| `model.pkl` | The trained and serialized machine learning model. |
| `Phishing Websites Features.docx` | Documentation explaining the features extracted from URLs. |

## 🛠️ Installation & Usage

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Phishing-Detection-Capstone.git](https://github.com/YOUR_USERNAME/Phishing-Detection-Capstone.git)
cd Phishing-Detection-Capstone
2. Install Dependencies
Make sure you have Python installed. Then, install the required libraries:

Bash

pip install pandas flask scikit-learn numpy
3. Run the Application
Start the Flask web server:

Bash

python app.py
4. Access the Interface
Open your web browser and go to: http://127.0.0.1:5000

📊 Model Performance (Preliminary)
Current Algorithm: Random Forest Classifier

Accuracy: ~71.87% (Baseline for Capstone I)

Future Goal: Improve accuracy to >95% using Hyperparameter Tuning and XGBoost in Capstone II.

🔜 Future Work (Capstone II)
[ ] Integration of WHOIS API for dynamic domain age extraction.

[ ] Development of a Chrome/Edge Browser Extension.

[ ] Implementation of Deep Learning models (CNN/LSTM) for better accuracy.

[ ] Enhanced UI/UX with detailed threat reports.

👤 Author
Emre GÜLEN

Department of Computer Engineering

Istinye University, Istanbul

This project is submitted to Dr. Ali Asghar POUR HAJI KAZEM for the partial fulfillment of the Capstone Project I requirements.
