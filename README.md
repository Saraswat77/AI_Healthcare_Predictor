
# 🧠 AI Health Assistant

An AI-powered healthcare prediction app built using **Python**, **Streamlit**, **Machine Learning**, and **Data Visualization** tools. This app helps predict:

- ❤️ Heart Disease
- 🩺 Diabetes

---

## 📁 Folder Structure
```
AI_for_HealthCare/
├── app/
│   ├── main.py              # Streamlit UI app
│   └── utils.py             # Model loading & prediction logic
├── models/
│   ├── heart_model.pkl      # Trained heart disease model
│   └── diabetes_model.pkl   # Trained diabetes model
├── data/
│   ├── heart.csv            # Dataset used for training (heart)
│   └── diabetes.csv         # Dataset used for training (diabetes)
├── notebooks/               # Jupyter notebooks for training
├── README.md
└── requirements.txt         # Dependencies
```

---

## 🚀 How to Run

1. **Clone or Download** the project

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app/main.py
```

4. It will open in your browser automatically ✅

---

## 💡 Features
- Clean UI with Streamlit
- Predicts heart disease and diabetes
- Trained ML models using Logistic Regression / Random Forest
- Modular structure (easy to expand)

---

## 🧪 Datasets Used
- Heart Disease: `heart.csv`
- Diabetes: `diabetes.csv`

> Source: [Kaggle UCI Heart Dataset](https://www.kaggle.com/ronitf/heart-disease-uci) and [Pima Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## 📦 Requirements
Example contents of `requirements.txt`:
```
streamlit
pandas
scikit-learn
```

---

## 👨‍🎓 Author
**Shivam Saraswat**  
B.Tech, Data Science Student  
[LinkedIn](https://www.linkedin.com/in/saraswat77) | [GitHub](https://github.com/Saraswat77)

---

## 📌 Note
This is a student project for learning purposes and is **not intended for real-world diagnosis**.
