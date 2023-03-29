import openai
import streamlit as st

openai.api_key = "YOUR_API_KEY_HERE"

def classify_document(prompt, engine):
    # Define keywords for spam classification
    spam_keywords = ["free", "discount", "offer", "limited time", "money-back guarantee", "win", "prize", "cash", "credit", "card"]

    # Check if any spam keywords are present in the text
    is_spam = any(keyword in prompt.lower() for keyword in spam_keywords)

    # Return label based on spam classification
    if is_spam:
        label = "Spam"
    else:
        label = "Non-Spam"
    return label

def main():
    # Set page title
    st.title("Document Classifier")

    # Set up initial settings
    settings = {
        "engine": "text-davinci-002"
    }

    # get user API key
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    
    if api_key:
        openai.api_key = api_key

        # get user input
        user_input = st.text_input("Enter the document to classify:")

        # classify input text
        if user_input:
            label = classify_document(user_input, settings["engine"])
            st.write("The document is:", label)


if __name__ == '__main__':
    main()
