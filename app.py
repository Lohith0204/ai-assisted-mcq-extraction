import streamlit as st
import tempfile
import json
import os

from input_handlers.text_loader import load_text
from input_handlers.pdf_loader import load_pdf
from input_handlers.docx_loader import load_docx
from llm_engine.extractor import extract_mcqs
from llm_engine.client import get_llm_client


def load_input(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        return load_text(file_path)
    elif ext == ".pdf":
        return load_pdf(file_path)
    elif ext == ".docx":
        return load_docx(file_path)
    else:
        raise ValueError("Unsupported file format")


st.set_page_config(page_title="AI MCQ Extractor", layout="centered")
st.title("AI-Assisted MCQ Extraction")

uploaded_file = st.file_uploader(
    "Upload a document (TXT, PDF, DOCX)",
    type=["txt", "pdf", "docx"]
)

if uploaded_file:
    suffix = os.path.splitext(uploaded_file.name)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.success("File uploaded successfully")

    if st.button("Extract MCQs"):
        with st.spinner("Extracting MCQs using AI..."):
            try:
                text = load_input(temp_path)

                if not text.strip():
                    raise ValueError("No readable text found in the uploaded document")

                llm_client = get_llm_client()
                mcqs = extract_mcqs(llm_client, text)

                st.success("MCQs extracted successfully!")
                st.json(mcqs)

                st.download_button(
                    label="Download JSON",
                    data=json.dumps(mcqs, indent=2),
                    file_name="mcqs.json",
                    mime="application/json"
                )

            except Exception as e:
                st.error(str(e))

            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
