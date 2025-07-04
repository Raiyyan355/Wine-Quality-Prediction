# Wine Quality Prediction using Stacked Machine Learning Models

This project is a Flask-based web application that predicts the **quality of wine** based on its physicochemical features. It uses a **stacked machine learning model** trained on a wine dataset to classify wine quality into multiple categories (multi-class classification).

---

## 🧠 Project Overview

The wine quality prediction system accepts input values for several chemical properties of the wine and predicts its quality level using a pre-trained machine learning model. The goal is to assist winemakers, researchers, or wine enthusiasts in understanding the impact of different features on wine quality.

---

## 🚀 Live Demo

[C:\Users\Raiyyan LUCKY\OneDrive\Desktop\WineQT\WineQT_SS.jpeg]
---

## ⚙️ Tech Stack

| Component     | Technology Used        |
|---------------|------------------------|
| Frontend      | HTML, CSS (via Flask templates) |
| Backend       | Python, Flask          |
| ML Libraries  | scikit-learn, NumPy, joblib |
| Model         | Stacked Classifier (e.g., Logistic Regression + Random Forest, etc.) |
| Deployment    | Localhost using Flask  |

---

## 📊 Input Features

The model requires the following 11 physicochemical attributes as input:

1. Fixed Acidity  
2. Volatile Acidity  
3. Citric Acid  
4. Residual Sugar  
5. Chlorides  
6. Free Sulfur Dioxide  
7. Total Sulfur Dioxide  
8. Density  
9. pH  
10. Sulphates  
11. Alcohol  

These are standard chemical characteristics used in wine quality assessments.

---

## 🧪 Model Description

The backend uses a **stacked classification model**, trained and saved as `stacked_model.joblib`. It likely combines predictions from multiple classifiers to improve accuracy and generalization.

Model file is loaded during app initialization:
```python
with open('stacked_model.joblib', 'rb') as f:
    model = joblib.load(f)
```

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.7+
- Flask
- scikit-learn
- joblib
- NumPy

### Installation and Execution

1. **Clone the Repository**
```bash
git clone https://github.com/Raiyyan355/Wine-Quality-Prediction.git
cd Wine-Quality-Prediction
```

2. **Install the Dependencies**
```bash
pip install -r requirements.txt
```

3. **Ensure Model File Exists**
Place the `stacked_model.joblib` file in the root directory. (This file should be created from a separate model training script.)

4. **Run the Application**
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 🌐 Web Interface

- Simple and clean form interface to input 11 features.
- Submit button to get the predicted wine quality.
- Displays prediction result on the same page.

---

## 📁 Project Structure

```
├── app.py                  # Flask web app
├── stacked_model.joblib    # Pre-trained ML model (to be added)
├── templates/
│   └── index.html          # Frontend HTML form
├── static/
│   └── style.css           # (Optional) CSS styling
├── README.md               # Project documentation
└── requirements.txt        # Dependencies list
```

---

## 📌 Future Enhancements

- Add model training script and notebook to the repo
- Improve UI with Bootstrap or other styling
- Add data visualization for feature importance
- Deploy online using services like Heroku, Render, or AWS
