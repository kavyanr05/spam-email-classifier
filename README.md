# 📧 Spam Email Classifier

## Project Overview
This project uses Machine Learning and Natural Language Processing (NLP) to classify SMS messages as Spam or Ham (Not Spam).

The model learns from historical messages and predicts whether a new message is unwanted spam.

## Objectives
- Understand text preprocessing.
- Convert text into numerical features using TF-IDF.
- Train a machine learning classification model.
- Evaluate model performance.
- Predict whether messages are spam or legitimate.

## Technologies Used
- Python 3.12
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Google Colab
- Jupyter Notebook

## Dataset
SMS Spam Collection Dataset

- Total messages: 5,572
- Ham messages: 4,825
- Spam messages: 747

## Project Files
- `Spam_Email_Classifier.ipynb` – Complete project notebook.
- `spam_classifier_model.pkl` – Trained classification model.
- `tfidf_vectorizer.pkl` – Saved TF-IDF vectorizer.

## How It Works
1. Load the SMS dataset.
2. Clean and preprocess text.
3. Convert messages into TF-IDF features.
4. Train a machine learning model.
5. Evaluate the model.
6. Predict whether new messages are spam or ham.

## How to Run
1. Open the notebook in Google Colab.
2. Run the cells in sequence.
3. Load the dataset and train the model.
4. Test messages using the prediction function.

## Author
Kavya

## Disclaimer
This project is developed for educational and internship purposes. Predictions may not always be correct.
