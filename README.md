# 🏥 Medical Q&A Chatbot

A specialized **Medical Question Answering Chatbot** built using the **MedQuAD (Medical Question Answering Dataset)**. The chatbot uses a **retrieval-based Natural Language Processing (NLP) approach** to find the most relevant medical answer for a user's question.

The system combines **TF-IDF vectorization**, **Cosine Similarity**, and **basic medical entity recognition** to provide relevant answers related to diseases, symptoms, and treatments.

> ⚠️ **Disclaimer:** This chatbot is developed for educational and research purposes only. It is not a replacement for a qualified medical professional and should not be used for medical diagnosis or treatment decisions.

---

## 📌 Project Overview

Medical information is available in large amounts on the internet, but finding relevant and reliable answers can sometimes be difficult.

This project develops a simple medical chatbot that allows users to enter questions in natural language. The chatbot searches through the **MedQuAD dataset** and identifies the most relevant question-answer pair using **TF-IDF and Cosine Similarity**.

For example, a user can ask:

```text
What are the symptoms of diabetes?
```

The chatbot analyzes the question, compares it with medical questions in the dataset, and retrieves the answer associated with the most similar question.

The application also performs basic medical entity recognition to identify entities such as:

* 🦠 Diseases
* 🤒 Symptoms
* 💊 Treatments

A **Streamlit-based web interface** provides a simple and interactive way for users to communicate with the chatbot.

---

## 🎯 Objectives

The main objectives of this project are:

1. Build a retrieval-based medical question-answering system.
2. Use the MedQuAD dataset as the medical knowledge base.
3. Convert medical questions into numerical vectors using TF-IDF.
4. Calculate similarity between the user's question and dataset questions.
5. Retrieve the most relevant medical answer.
6. Identify basic medical entities such as diseases, symptoms, and treatments.
7. Develop a simple and user-friendly Streamlit interface.
8. Demonstrate the use of NLP techniques in the healthcare domain.

---

## ✨ Features

### 1. Medical Question Answering

Users can enter medical questions and receive relevant answers from the MedQuAD dataset.

Example:

```text
User:
What are the symptoms of asthma?

Chatbot:
[Relevant answer retrieved from MedQuAD]
```

---

### 2. TF-IDF Based Retrieval

The chatbot uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text into numerical vectors.

TF-IDF gives importance to words based on how frequently they appear in a document while reducing the importance of commonly occurring words.

The user's question is converted into a TF-IDF vector and compared with the questions in the dataset.

---

### 3. Cosine Similarity

After converting the questions into vectors, **Cosine Similarity** is used to determine how similar the user's question is to questions in the dataset.

The question with the highest similarity score is selected, and its corresponding answer is returned.

Conceptually:

```text
User Question
      ↓
Text Processing
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Find Most Similar Question
      ↓
Retrieve Answer
      ↓
Display Response
```

---

### 4. Medical Entity Recognition

The chatbot performs basic recognition of medical entities.

It can identify categories such as:

```text
Disease
Symptoms
Treatment
```

For example:

```text
Input:
What are the symptoms and treatment options for diabetes?

Detected Entities:
Disease: Diabetes
Symptoms: Symptoms
Treatment: Treatment
```

> Note: The entity recognition component is a basic implementation and is not intended to replace advanced medical NER systems.

---

### 5. Streamlit Web Interface

The chatbot uses **Streamlit** to provide a simple web-based interface.

Users can:

* Enter their medical question
* Submit the question
* View the retrieved answer
* View detected medical entities
* Interact with the chatbot without using the command line

---

## 📊 Dataset

### MedQuAD

The project uses the **MedQuAD (Medical Question Answering Dataset)**.

MedQuAD contains medical question-answer pairs collected from trusted sources, including information originating from **NIH/National Library of Medicine resources**.

Dataset repository:

**MedQuAD GitHub Repository:**
https://github.com/abachaa/MedQuAD

The dataset contains information related to various medical topics, including:

* Diseases
* Symptoms
* Diagnosis
* Treatments
* Prevention
* Medical conditions
* Health-related questions

The dataset acts as the chatbot's **knowledge base**.

---

## 🧠 System Architecture

The overall architecture of the project is:

```text
                 ┌─────────────────────┐
                 │      User           │
                 │ Medical Question    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Streamlit UI      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Text Preprocessing  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   TF-IDF Vectorizer │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Cosine Similarity   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Relevant Question   │
                 │     Retrieval       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Retrieve Medical    │
                 │      Answer         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Medical Entity      │
                 │ Recognition         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Display Answer      │
                 │ + Entities          │
                 └─────────────────────┘
```

---

## 🔄 How the Chatbot Works

### Step 1: Load Dataset

The MedQuAD dataset is loaded using Pandas.

```python
import pandas as pd

data = pd.read_csv("medquad.csv")
```

The dataset contains medical questions and their corresponding answers.

---

### Step 2: Preprocess the Data

The questions are cleaned and prepared for vectorization.

Typical preprocessing may include:

* Converting text to lowercase
* Removing unnecessary spaces
* Handling missing values
* Removing unwanted characters

---

### Step 3: Create TF-IDF Vectors

The questions are converted into numerical representations using Scikit-learn's `TfidfVectorizer`.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(data["question"])
```

---

### Step 4: Process User Question

When the user enters a question, the chatbot converts it into the same TF-IDF representation.

```python
user_vector = vectorizer.transform([user_question])
```

---

### Step 5: Calculate Similarity

Cosine Similarity compares the user's question with all questions in the dataset.

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(
    user_vector,
    question_vectors
)
```

---

### Step 6: Find the Best Match

The chatbot identifies the question with the highest similarity score.

```python
best_match = similarity.argmax()
```

The corresponding answer is then retrieved from the dataset.

---

### Step 7: Display the Answer

The retrieved answer is displayed through the Streamlit interface.

The interface can also display the detected medical entities.

---

## 🧩 Technologies Used

| Technology       | Purpose                                       |
| ---------------- | --------------------------------------------- |
| **Python**       | Main programming language                     |
| **Pandas**       | Dataset loading and data processing           |
| **Scikit-learn** | TF-IDF and Cosine Similarity                  |
| **Streamlit**    | Web-based user interface                      |
| **MedQuAD**      | Medical question-answer knowledge base        |
| **NLP**          | Natural language processing and text analysis |

---

## 📁 Project Structure

A recommended project structure is:

```text
Medical-QA-Chatbot/
│
├── data/
│   └── medquad.csv
│
├── app.py
│
├── chatbot.py
│
├── entity_recognition.py
│
├── requirements.txt
│
├── README.md
│
└── screenshots/
    └── chatbot_interface.png
```

### File Description

| File/Folder             | Description                             |
| ----------------------- | --------------------------------------- |
| `data/`                 | Contains the MedQuAD dataset            |
| `app.py`                | Streamlit application                   |
| `chatbot.py`            | Question retrieval and similarity logic |
| `entity_recognition.py` | Medical entity recognition              |
| `requirements.txt`      | Required Python libraries               |
| `README.md`             | Project documentation                   |
| `screenshots/`          | Screenshots of the application          |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Medical-QA-Chatbot.git
```

Navigate into the project:

```bash
cd Medical-QA-Chatbot
```

---

### 2. Create a Virtual Environment

Creating a virtual environment is recommended.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

Or install the main dependencies directly:

```bash
pip install streamlit pandas scikit-learn
```

---

## 📦 requirements.txt

The `requirements.txt` file can contain:

```text
streamlit
pandas
scikit-learn
```

If additional NLP libraries are used in your implementation, they can also be added to this file.

---

## ▶️ How to Run the Project

After installing the required dependencies, run:

```bash
streamlit run app.py
```

Streamlit will start the application locally.

Open the URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

## 💻 Example Usage

### User Input

```text
What are the symptoms of diabetes?
```

### Chatbot Process

```text
User Question
      ↓
TF-IDF Transformation
      ↓
Compare with MedQuAD Questions
      ↓
Calculate Cosine Similarity
      ↓
Find Highest Similarity
      ↓
Retrieve Corresponding Answer
```

### Output

```text
Answer:
[Relevant answer retrieved from MedQuAD]

Medical Entities:
Disease: Diabetes
```

---

## 🔍 Retrieval Method

The chatbot follows a **retrieval-based approach** rather than generating new medical information.

This means that the system does not create an answer from scratch.

Instead:

```text
User Question
      ↓
Search MedQuAD
      ↓
Find Similar Question
      ↓
Retrieve Existing Answer
```

This approach is useful because the chatbot's responses are based on information available in the dataset rather than freely generated responses.

---

## 📐 Cosine Similarity

Cosine Similarity measures the similarity between two vectors.

It can be represented as:

```text
                    A · B
Cosine Similarity = ────────
                    ||A|| ||B||
```

Where:

* `A` = Vector representing the user's question
* `B` = Vector representing a dataset question
* `A · B` = Dot product
* `||A||` and `||B||` = Magnitudes of the vectors

A higher similarity score indicates that the questions are more similar.

---

## 🏥 Medical Entity Recognition

The project includes a basic medical entity recognition component.

The purpose is to identify important medical terms in the user's query.

### Example

Input:

```text
What are the symptoms and treatments for asthma?
```

Possible output:

```text
Disease:
Asthma

Symptoms:
Symptoms

Treatment:
Treatments
```

The entity recognition component can be further improved using advanced NLP libraries and medical terminology databases.

---

## 🖥️ User Interface

The Streamlit application provides:

* Application title
* Medical question input box
* Submit/search button
* Retrieved answer section
* Medical entity section
* Educational disclaimer

Example interface:

```text
╔══════════════════════════════════════╗
║       🏥 Medical Q&A Chatbot         ║
╠══════════════════════════════════════╣
║                                      ║
║  Ask your medical question:          ║
║  ┌────────────────────────────────┐  ║
║  │ What are symptoms of asthma?  │  ║
║  └────────────────────────────────┘  ║
║                                      ║
║           [ Get Answer ]             ║
║                                      ║
║  📖 Answer                            ║
║  Relevant answer from MedQuAD...     ║
║                                      ║
║  🔎 Medical Entities                 ║
║  Disease: Asthma                     ║
║                                      ║
╚══════════════════════════════════════╝
```

---

## 🚀 Future Improvements

The current chatbot can be improved in several ways.

### 1. Advanced NLP Models

Replace TF-IDF with modern sentence embeddings such as:

* Sentence Transformers
* BERT
* BioBERT
* ClinicalBERT

This can improve semantic understanding.

---

### 2. Better Medical Entity Recognition

Use specialized medical NLP models to identify:

* Diseases
* Symptoms
* Medicines
* Treatments
* Procedures
* Body parts
* Medical tests

---

### 3. Confidence Score

The chatbot can display a similarity score for the retrieved answer.

Example:

```text
Match Confidence: 87%
```

If the similarity score is too low, the chatbot can respond:

```text
I could not find a sufficiently relevant answer.
Please consult a qualified healthcare professional.
```

---

### 4. Conversation History

The chatbot can be improved to remember previous questions within a session.

Example:

```text
User:
What is diabetes?

Bot:
[Answer]

User:
What are its symptoms?

Bot:
[Answer related to diabetes]
```

---

### 5. Voice Input

Voice recognition can be added so users can ask questions using speech.

---

### 6. Multilingual Support

The chatbot can be extended to support multiple languages such as:

* English
* Hindi
* Kannada
* Telugu
* Tamil

---

### 7. Deployment

The Streamlit application can be deployed online using suitable cloud hosting services so that users can access the chatbot through a web browser.

---

## ⚠️ Limitations

This project has some important limitations:

* It is a retrieval-based system and does not generate original medical explanations.
* The quality of answers depends on the MedQuAD dataset.
* TF-IDF may not understand deeper semantic meaning.
* Basic entity recognition may produce incorrect or incomplete results.
* The chatbot cannot diagnose diseases.
* The chatbot cannot replace a doctor or healthcare professional.
* Medical emergencies should always be handled by qualified healthcare professionals.

---

## 🔐 Medical Safety Disclaimer

> **Important:** This chatbot is intended only for educational and informational purposes. The responses provided by the system should not be considered professional medical advice, diagnosis, or treatment. Users should consult a qualified doctor or healthcare professional for medical concerns, symptoms, diagnosis, or treatment decisions.

---

## 📈 Project Workflow

```text
MedQuAD Dataset
       │
       ▼
Data Cleaning & Preprocessing
       │
       ▼
Medical Questions
       │
       ▼
TF-IDF Vectorization
       │
       ▼
User Enters Question
       │
       ▼
User Question → TF-IDF
       │
       ▼
Cosine Similarity
       │
       ▼
Most Relevant Question
       │
       ▼
Retrieve Medical Answer
       │
       ├───────────────┐
       ▼               ▼
Medical Entity      Streamlit
Recognition            UI
       │               │
       └───────┬───────┘
               ▼
          Final Response
```

---

## 🎓 Learning Outcomes

Through this project, the following concepts can be learned:

* Natural Language Processing
* Text preprocessing
* TF-IDF vectorization
* Cosine Similarity
* Information retrieval
* Basic Named Entity Recognition
* Dataset handling using Pandas
* Building web applications using Streamlit
* Creating a retrieval-based chatbot
* Working with medical QA datasets
* Basic healthcare AI concepts

---

## 🧪 Testing

The chatbot can be tested using different types of medical questions.

Example test cases:

| User Question                         | Expected Result                   |
| ------------------------------------- | --------------------------------- |
| What are the symptoms of diabetes?    | Relevant diabetes information     |
| What causes asthma?                   | Relevant asthma information       |
| What are treatments for hypertension? | Relevant hypertension information |
| What is anemia?                       | Relevant anemia information       |
| What are the symptoms of flu?         | Relevant flu information          |

Testing different questions helps evaluate how effectively the retrieval system finds relevant answers.

---

## 🔮 Future Scope

This project can be developed into a more advanced **AI-powered medical information assistant** by integrating:

```text
Advanced Embeddings
       +
Vector Database
       +
Medical NLP Models
       +
RAG Architecture
       +
Medical Entity Recognition
       +
Conversation Memory
       +
Streamlit / Web Application
```

A future version could use **Retrieval-Augmented Generation (RAG)** to retrieve reliable medical information and generate easier-to-understand responses while maintaining references to the underlying medical sources.

---

## 👨‍💻 Project Information

**Project:** Medical Q&A Chatbot
**Domain:** Artificial Intelligence / Machine Learning / NLP
**Type:** Retrieval-Based Chatbot
**Dataset:** MedQuAD
**Interface:** Streamlit
**Language:** Python

---

## ⭐ Conclusion

The **Medical Q&A Chatbot** demonstrates how Natural Language Processing and information retrieval techniques can be used to build a simple healthcare-oriented question-answering system.

By combining the **MedQuAD dataset**, **TF-IDF**, **Cosine Similarity**, **basic medical entity recognition**, and **Streamlit**, the project provides an easy-to-use interface for retrieving relevant medical information.

The project also provides a foundation for future development using advanced NLP models, semantic search, medical Named Entity Recognition, and Retrieval-Augmented Generation.

---

## 📚 References

* MedQuAD Dataset: https://github.com/abachaa/MedQuAD
* Scikit-learn Documentation: https://scikit-learn.org/
* Streamlit Documentation: https://docs.streamlit.io/
* Pandas Documentation: https://pandas.pydata.org/

---



This project is intended for **educational and academic purposes**. Please check the licensing and usage terms of the MedQuAD dataset before redistributing the dataset or derived materials.
