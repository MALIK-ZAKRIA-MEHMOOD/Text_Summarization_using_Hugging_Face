import streamlit as st

# Set up the Streamlit app layout
st.title("Text Summarization Using Hugging Face")
st.markdown("### Enter the text you want to summarize:")

# Input text area for the user to enter text
input_text = st.text_area("Text Input", height=200)

# Button to generate the summary
if st.button("Generate Summary"):
    if input_text:
        # Generate summary
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        st.markdown("### Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")

# Optionally, you can add more features or customizations here.
