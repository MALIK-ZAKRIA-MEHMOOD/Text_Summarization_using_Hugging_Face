import streamlit as st
from transformers import pipeline

# Load the summarization pipeline from Hugging Face
summarizer = pipeline("summarization")

# Set up the Streamlit app layout
st.title("Text Summarization Using Hugging Face")
st.markdown("### Enter the text you want to summarize:")

# Input text area for the user to enter text
input_text = st.text_area("Text Input", height=200)

# Button to generate the summary
if st.button("Generate Summary"):
    if input_text:
        try:
            # Generate summary
            summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
            st.markdown("### Summary:")
            st.write(summary[0]['summary_text'])
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please enter some text to summarize.")
