# SMS Spam Detection Web App

## Project Overview

This project is a Machine Learning based web application built using **Flask** that detects whether a given SMS message is **Spam** or **Not Spam (Ham)**.

The model is trained using the **SMS Spam Collection Dataset** and uses **TF-IDF Vectorization** with a **Multinomial Naive Bayes** classifier.

---

## Features

- Spam / Not Spam detection
- Clean and responsive UI
- Machine Learning model integration
- Model trained on real dataset
- Easy to run locally

---

## Tech Stack

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML
- CSS

---

## Project Structure
sms-spam-detection

│

├── app.py

├── train.py

├── spam.csv

├── spam_model.pkl

├── vectorizer.pkl

├── requirements.txt

│

├── templates

│ └── index.html

│

└── static

  └── style.css

---
## Dataset

The project uses the **SMS Spam Collection Dataset**.

Dataset Columns:
- `v1` → Label (ham/spam)
- `v2` → Message text

Labels are converted to:
- 0 → Not Spam (Ham)
- 1 → Spam

---

## Installation & Setup

### 1️⃣ Download or Clone the Project Or download the ZIP file and extract it.

---

### 2️⃣ Install Required Libraries 
bash-
python -m pip install flask pandas scikit-learn joblib

### 3️⃣Train the Model

Before running the application, train the model:
bash-
python train.py


#This will generate:
--spam_model.pkl
--vectorizer.pkl

### 4️⃣ Run the Application
python app.py
### Open your browser and go to:
http://127.0.0.1:5000

### Sample testcases

## Spam Messages

-"Congratulations! You have won a free lottery ticket!"

-"URGENT! Claim your prize now!"

-"Buy now and get 50% discount!"

##  Not Spam Messages

-"Are we meeting tomorrow?"

-"Call me when you reach home."

-"Happy Birthday!"


