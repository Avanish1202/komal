import streamlit as st
from textblob import TextBlob

def sentiment_analysis():
    st.title("Sentiment Analysis Tool")
    st.write("### Analyze the sentiment of your text easily!")
    
    # Accept input from the user
    user_input = st.text_area("Enter text for sentiment analysis:", "")

    if st.button("Analyze Sentiment"):
        if user_input.strip() == "":
            st.warning("Please enter some text before analyzing.")
            return

        # Analyze sentiment using TextBlob
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity  # Polarity ranges from -1 to 1

        # Determine sentiment category
        if sentiment_score > 0:
            sentiment = "Positive 😊"
            st.success(f"Sentiment Score: {sentiment_score:.2f}")
        elif sentiment_score < 0:
            sentiment = "Negative 😟"
            st.error(f"Sentiment Score: {sentiment_score:.2f}")
        else:
            sentiment = "Neutral 😐"
            st.info(f"Sentiment Score: {sentiment_score:.2f}")

        # Display the sentiment
        st.subheader(f"Sentiment: {sentiment}")

# Run the sentiment analysis tool
if __name__ == "__main__":
    sentiment_analysis()
