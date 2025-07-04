# utils.py - Helper functions for the app
import pickle

# Load a trained model from a given file path
def load_model(path):
    with open(path, "rb") as f:
        return pickle.load(f)

# Predict heart disease based on input features
def predict_heart_disease(model, data):
    prediction = model.predict(data)
    return prediction[0]

# Predict diabetes based on input features
def predict_diabetes(model, data):
    prediction = model.predict(data)
    return prediction[0]
