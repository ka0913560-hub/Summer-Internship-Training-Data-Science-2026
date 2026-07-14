# 📅 Day-12: Logistic Regression & Model Evaluation

## 📌 Overview

Today I learned Logistic Regression for binary classification using Scikit-learn. I performed complete data preprocessing, trained Logistic Regression models on two datasets, evaluated the models using different metrics, and deployed the Iris model with Streamlit.

---

# 📚 Topics Covered

- Introduction to Logistic Regression
- Binary Classification
- Sigmoid Function
- Data Cleaning
- Handling Missing Values
- Label Encoding
- Feature Selection
- Train-Test Split
- Logistic Regression Model
- Model Prediction
- Pickle Model Saving
- Streamlit Deployment
- Confusion Matrix
- Accuracy
- Precision
- Recall
- F1-Score

---

# 🚀 Projects Completed

## 1️⃣ Car Price Classification

### Objective

Classify whether a car belongs to a High Price or Low Price category using Logistic Regression.

### Steps Performed

- Imported dataset
- Checked missing values
- Removed null values
- Dropped unnecessary columns
- Converted categorical columns using Label Encoding
- Converted numerical columns
- Created target variable (Price Category)
- Train-Test Split
- Trained Logistic Regression Model
- Model Evaluation
- Saved Model using Pickle

---

## 2️⃣ Iris Flower Prediction

### Objective

Predict the flower species (Versicolor or Virginica) using Logistic Regression.

### Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Deployment

- Streamlit GUI
- Pickle Model
- Real-time Prediction

---

# 📖 Logistic Regression

Logistic Regression is a Supervised Machine Learning Classification Algorithm used to predict categorical outputs.

Instead of predicting continuous values, it predicts the probability of a class using the Sigmoid Function.

### Sigmoid Function

```
P = 1 / (1 + e^-x)
```

Output Range

```
0 → 1
```

If Probability ≥ 0.5 → Class = 1

Else → Class = 0

---

# 📊 Evaluation Metrics

## Accuracy

Overall kitni predictions sahi hui.

Formula

```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

---

## Precision

Positive predictions me se kitni correct thi.

Formula

```
Precision = TP / (TP + FP)
```

---

## Recall

Actual positive values me se kitni correctly identify hui.

Formula

```
Recall = TP / (TP + FN)
```

---

## F1 Score

Precision aur Recall ka harmonic mean.

Formula

```
F1 Score = 2 × (Precision × Recall) / (Precision + Recall)
```

---

# 📊 Confusion Matrix

| Actual \ Predicted | Positive | Negative |
|--------------------|----------|----------|
| Positive           | TP       | FN       |
| Negative           | FP       | TN       |

### Terms

- TP → True Positive
- TN → True Negative
- FP → False Positive
- FN → False Negative

---

# 🛠️ Libraries Used

- Pandas
- NumPy
- Scikit-learn
- Pickle
- Streamlit

---

# 📂 Files

```
Day-12/
│
├── ds day12(logistic_regression).ipynb
├── README.md
├── model.pkl
├── app.py
├── requirements.txt
└── cardekho.csv
```

---

# 🎯 Learning Outcome

✔ Understood Logistic Regression

✔ Learned Binary Classification

✔ Performed Data Preprocessing

✔ Created Classification Models

✔ Evaluated Model Performance

✔ Learned Confusion Matrix

✔ Learned Accuracy, Precision, Recall & F1 Score

✔ Saved ML Models using Pickle

✔ Built and Deployed a Streamlit Application

---

⭐ Day 12 completed successfully as part of the Data Science Summer Internship 2026.
