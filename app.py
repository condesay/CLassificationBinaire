import openai
import streamlit as st

openai.api_key = "YOUR_API_KEY_HERE"

def classify_document(prompt, engine,temperature, max_tokens, top_p, frequency_penalty, presence_penalty):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
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
    st.title("Classification en Spam et non SPam GPT3 App")

    # Set up sidebar options
    engine_options = {
        "Davinci": {
            "Sentiment Analysis": "text-davinci-002"
        }
    }

    # Set up initial settings
    settings = {
        "engine": "Davinci",
        "mode": "Sentiment Analysis",
        "temperature": 0.7,
        "max_tokens": 190,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }
    # get user API key
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    
    if api_key:
        openai.api_key = api_key

        # get user input
        user_input = st.text_input("Enter the document to classify:")

        # classify input text
        if user_input:
            engine_id = engine_options[settings["engine"]][settings["mode"]]
            label = classify_document(user_input,engine_id , settings["temperature"], settings["max_tokens"], settings["top_p"], settings["frequency_penalty"], settings["presence_penalty"])
            st.write("The document is:", label)


        # Display chat settings sidebar
        st.sidebar.title("Paramètres")
        settings["engine"] = st.sidebar.selectbox("Engine", list(engine_options.keys()))
        settings["temperature"] = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, step=0.1, value=settings["temperature"])
        settings["max_tokens"] = st.sidebar.slider("Max Tokens", min_value=1, max_value=2048, step=1, value=settings["max_tokens"])
        settings["mode"] = st.sidebar.selectbox("Mode", list(engine_options[settings["engine"]].keys()))
        settings["top_p"] = st.sidebar.slider("Top P", min_value=0.0, max_value=1.0, step=0.1, value=settings["top_p"])
        settings["frequency_penalty"] = st.sidebar.slider("Frequency Penalty", min_value=0.0, max_value=1.0, step=0.1, value=settings["frequency_penalty"])
        settings["presence_penalty"] = st.sidebar.slider("Presence Penalty", min_value=0.0, max_value=1.0, step=0.1, value=settings["presence_penalty"])
                                                              # Display current settings
        st.sidebar.markdown("### Paramètres Actuels")
        st.sidebar.write(f"Engine: {settings['engine']}")
        st.sidebar.write(f"Temperature: {settings['temperature']}")
        st.sidebar.write(f"Mode: {settings['mode']}")
        st.sidebar.write(f"Max Tokens: {settings['max_tokens']}")
        st.sidebar.write(f"Top P: {settings['top_p']}")
        st.sidebar.write(f"Frequency Penalty: {settings['frequency_penalty']}")
        st.sidebar.write(f"Presence Penalty: {settings['presence_penalty']}")             
if __name__ == '__main__':
    main()
