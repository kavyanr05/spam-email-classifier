
import streamlit as st
import joblib

# Load saved machine learning files
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Application title
st.title("📧 Spam Email Classifier")
st.write("Enter a message to check whether it is spam or legitimate.")

# Message input
message = st.text_area("Enter your message:")

# Prediction button
if st.button("Check Message"):

    if message.strip():

        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)[0]

        if prediction == "spam":
            st.error("🚨 This message is SPAM!")
        else:
            st.success("✅ This message is NOT SPAM!")

    else:
        st.warning("Please enter a message.")
