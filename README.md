🩺 Medical Q&A Chatbot

A specialized Medical Question Answering Chatbot built using the MedQuAD dataset. The chatbot retrieves relevant answers from a curated medical knowledge base and performs basic medical entity recognition (Diseases, Symptoms, Treatments) to help highlight key terms in both the user's question and the retrieved answer.

⚠️ Disclaimer: This chatbot is built strictly for educational and learning purposes. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

📋 Table of Contents
Project Overview
Features
Dataset
How It Works
Technologies Used
Project Structure
How to Run
Usage Example
Limitations
Future Improvements
Contributing
License
📖 Project Overview

This project implements a retrieval-based medical chatbot — meaning it does not generate free-form text like a large language model, but instead searches through a fixed dataset of real question-answer pairs and returns the answer that best matches the user's query.

The core matching engine uses TF-IDF (Term Frequency–Inverse Document Frequency) vectorization combined with Cosine Similarity to measure how closely a user's question resembles questions already present in the MedQuAD dataset. The closest match's corresponding answer is returned to the user.

On top of retrieval, the project includes a lightweight medical entity recognition layer that scans text for mentions of diseases, symptoms, and treatments, helping users quickly identify the key medical concepts involved.

The entire experience is wrapped in a simple, interactive Streamlit web interface, making it easy to run locally and query without any command-line interaction.

✨ Features
Retrieval-based Question Answering — matches user queries against thousands of real medical Q&A pairs from MedQuAD.
TF-IDF + Cosine Similarity — a classic, interpretable, and lightweight NLP technique for semantic-ish text matching without needing deep learning models.
Basic Medical Entity Recognition — detects and highlights:
Diseases (e.g., diabetes, asthma, hypertension)
Symptoms (e.g., fever, fatigue, nausea)
Treatments (e.g., medication names, therapies, procedures)
Simple, Clean Streamlit UI — minimal setup, runs directly in the browser.
Educational Purpose Only — designed as a learning project for NLP, information retrieval, and healthcare-adjacent applications, not for clinical use.
🗂️ Dataset

MedQuAD — Medical Question Answering Dataset

Contains thousands of real medical question-answer pairs.
Collected from trusted NIH (National Institutes of Health) websites and other authoritative U.S. government health sources (e.g., NIDDK, GARD, NINDS, SeniorHealth, MedlinePlus).
Each entry typically includes:
A question (e.g., "What are the symptoms of asthma?")
A question type/focus (e.g., Symptoms, Treatment, Causes)
An answer sourced from a trusted medical authority
Used here as the knowledge base that the chatbot searches against when answering user queries.

Note: You will need to obtain the MedQuAD dataset separately (it's publicly available on GitHub) and place it in your project directory before running the app.

⚙️ How It Works
Preprocessing — The MedQuAD questions are cleaned (lowercased, punctuation removed, stopwords optionally filtered) and converted into TF-IDF vectors.
Vectorization — A TF-IDF matrix is built from all questions in the dataset, representing each question as a weighted vector of important words.
User Query Matching — When a user types a question, it's transformed into the same TF-IDF vector space.
Similarity Scoring — Cosine similarity is computed between the user's query vector and every question vector in the dataset.
Answer Retrieval — The question with the highest similarity score is selected, and its associated answer is returned to the user.
Entity Highlighting — A rule-based or dictionary-based scan identifies disease, symptom, and treatment terms in the question/answer for extra context.
🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
Streamlit	Web User Interface
Pandas	Dataset loading & handling
Scikit-learn	TF-IDF Vectorizer & Cosine Similarity
MedQuAD Dataset	Medical knowledge base
📁 Project Structure

A typical layout for this kind of project looks like this (adjust to match your actual repo):

medical-qa-chatbot/
│
├── data/
│   └── medquad.csv              # MedQuAD dataset (questions, answers, focus)
│
├── app.py                       # Main Streamlit application
├── chatbot.py                   # Core retrieval logic (TF-IDF + cosine similarity)
├── entity_recognition.py        # Basic NER for diseases/symptoms/treatments
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
🚀 How to Run
1. Clone the repository
bash
git clone https://github.com/your-username/medical-qa-chatbot.git
cd medical-qa-chatbot
2. Create a virtual environment (recommended)
bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
3. Install required libraries
bash
pip install streamlit pandas scikit-learn
4. Add the dataset

Download the MedQuAD dataset and place the processed CSV file inside a data/ folder (or update the file path in the code accordingly).

5. Run the Streamlit app
bash
streamlit run app.py
6. Open in browser

Streamlit will automatically launch a local server, typically at:

http://localhost:8501
💬 Usage Example
Launch the app using the steps above.
Type a medical question into the input box, for example:

"What are the symptoms of type 2 diabetes?"

The chatbot will:
Search the MedQuAD dataset for the closest matching question
Return the most relevant answer
Highlight any recognized diseases, symptoms, or treatments in the response
⚠️ Limitations
Not a diagnostic tool — the chatbot cannot interpret personal symptoms or provide medical advice tailored to an individual.
Retrieval-only — it can only return answers that already exist in the dataset; it does not generate new explanations.
TF-IDF limitations — this method relies on word overlap and doesn't fully capture semantic meaning, so paraphrased or oddly-worded questions may not match well.
Entity recognition is rule/dictionary-based — it may miss uncommon terms or misclassify ambiguous words, unlike a trained clinical NER model.
Dataset scope — answers are limited to what MedQuAD covers; rare conditions or very recent medical developments may not be included.
🔮 Future Improvements
Replace TF-IDF with sentence embeddings (e.g., Sentence-BERT) for better semantic matching.
Integrate a trained biomedical NER model (e.g., spaCy's en_core_sci_md or scispaCy) for more accurate entity recognition.
Add confidence scores to show how certain the chatbot is about a retrieved answer.
Support follow-up questions with conversational context.
Add source citations/links back to the original NIH resource for each answer.
Deploy the app publicly (e.g., Streamlit Community Cloud) for easier access.
