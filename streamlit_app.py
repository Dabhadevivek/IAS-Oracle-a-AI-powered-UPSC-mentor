import streamlit as st
from src.pdf_extraction import extract_pdf_text
from src.rag_model import generate_summary
from src.audio_summary import generate_audio_gtts

st.title("IAS Oracle - AI Assistant")

# Upload PDF for Summarization
uploaded_pdf = st.file_uploader("Upload a newspaper PDF", type="pdf")
if uploaded_pdf:
    pdf_text = extract_pdf_text(uploaded_pdf)
    st.write("Extracted Text:")
    st.write(pdf_text[:500])  # Display first 500 characters

    if st.button("Generate Summary"):
        summary = generate_summary(pdf_text)
        st.write("Generated Summary:")
        st.write(summary)

        # Audio Summary
        if st.button("Generate Audio Summary"):
            audio_filename = "summary_audio.mp3"
            generate_audio_gtts(summary, audio_filename)
            st.audio(audio_filename)

# Submit UPSC Answer for Evaluation
user_answer = st.text_area("Enter your UPSC Answer:")
if st.button("Evaluate Answer"):
    topper_answer = "The government plays a crucial role in fiscal management..."
    feedback = evaluate_answer(user_answer, topper_answer)
    st.write("Evaluation Feedback:")
    st.write(feedback)
