import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Load the pickled model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))
            
    return " ".join(y)        
                

# Streamlit app
def main():
    st.title("SMS/E-Mail Spam Classifier")

    # User input
    user_input = st.text_area("Enter a text message:", "")

    if st.button("Predict"):
        if user_input.strip() == "":
            st.warning("Please enter a text message.")
        else:
            #pre-process the user input
            user_input_preprocessed = transform_text(user_input)
            # Vectorize the user input
            user_input_vectorized = vectorizer.transform([user_input_preprocessed])
            
            # Make prediction
            prediction = model.predict(user_input_vectorized)
            predicted_label = "Spam" if prediction[0] == 1 else "Ham"
            
            st.success(f"The message is classified as: {predicted_label}")

# Run the app
if __name__ == "__main__":
    main()
