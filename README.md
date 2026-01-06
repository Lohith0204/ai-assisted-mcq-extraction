# AI-Assisted MCQ Extraction

## Live Demo
Try out the deployed application here:

🚀 **Streamlit App** → (paste the deployed streamlit link here)

## Overview
The AI-Assisted MCQ Extraction System is an artificial intelligence–based application that automatically extracts Multiple Choice Questions (MCQs) from unstructured educational documents.This project demonstrates the practical use of Large Language Models (LLMs) for structured information extraction. The system processes documents such as TXT, PDF, and DOCX, converts them into plain text, and intelligently extracts MCQs in a validated JSON format.The application avoids training models from scratch and instead leverages pre-trained LLMs, making it efficient, scalable, and suitable for real-world academic and internship use cases.

## Features
- Upload and process TXT, PDF, and DOCX documents
- Automatic extraction of MCQs with exactly four options (a, b, c, d)
- Schema-validated JSON output to ensure correctness
- Retry logic for reliable LLM responses
- Clean and modular project architecture
- Interactive and beginner-friendly Streamlit UI
- Download extracted MCQs as a JSON file
- Easily extendable for additional formats or deployment environments

## Tech Stack
- Python
- Streamlit
- Groq LLM API
- pdfplumber (PDF text extraction)
- python-docx (DOCX parsing)
- jsonschema (MCQ output validation)

## Project Structure
```text
AI-Assisted-MCQ-Extraction/
│
├── app.py                    # Streamlit UI and application logic
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
├── .gitignore                # Ignore files
│
├── input_handlers/
│   ├── __init__.py
│   ├── text_loader.py        # TXT file handler
│   ├── pdf_loader.py         # PDF file handler
│   └── docx_loader.py        # DOCX file handler
│
├── llm_engine/
│   ├── __init__.py
│   ├── client.py             # Groq LLM client
│   ├── extractor.py          # MCQ extraction logic
│   └── prompt.py             # System and user prompts
│
├── validation/
│   ├── __init__.py
│   └── schema.py             # JSON schema for MCQ validation
│
└── screenshots/              # Application screenshots
```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2026-01-03 163351.png>)

### Document Upload
![Document Upload](<screenshots/Screenshot 2026-01-03 163409.png>)

### Extracted MCQs Output
![Extracted MCQs Output](<screenshots/Screenshot 2026-01-03 163648.png>)

## How It Works
Once all required dependencies are installed, the application is launched using Streamlit. The user is presented with a simple and interactive web interface.The user uploads an educational document containing MCQs. Based on the file type, the system selects the appropriate loader to extract raw text from the document.

The extracted text is passed to a Large Language Model along with a carefully designed system prompt. The LLM identifies valid MCQs and returns structured output, which is then parsed and validated against a predefined JSON schema to ensure consistency and correctness.The validated MCQs are displayed in the UI and can be downloaded as a JSON file.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Set your Groq API key as an environment variable:
    ```powershell
    $env:GROQ_API_KEY="your_api_key_here"    
6. Run the application:
    streamlit run app.py

## Usage
This application is useful for automating the extraction of MCQs from educational content.

It can be applied in areas such as:
- Digitizing question banks
- Automating assessment creation
- Processing exam papers and study material
- Educational content analysis
- Demonstrating real-world LLM-based document processing
- Upload a supported document and click Extract MCQs to receive structured output within seconds.

## Future Improvements
- Add OCR-based image support using containerized deployments
- Support additional question formats
- Improve prompt engineering for higher extraction accuracy
- Export results to CSV or database storage
- Deploy as a REST API for integration with other platforms

## Learning Outcomes
This project provided practical experience in building a production-ready AI application using Large Language Models. It strengthened understanding of document ingestion pipelines, prompt engineering, schema validation, modular backend design, and Streamlit-based deployment.
The project demonstrates strong fundamentals in AI integration, backend engineering, and deployment awareness, making it suitable for internship submissions, academic evaluation, and portfolio presentation.