# Medical Q&A Chatbot

A specialized Medical Question Answering Chatbot built using the **MedQuAD** dataset.  
The chatbot retrieves relevant answers from medical knowledge and also performs basic medical entity recognition (Diseases, Symptoms, Treatments).

---

## Project Overview

This project creates a simple but effective medical chatbot that can answer health-related questions.  
It uses a retrieval-based approach with TF-IDF and Cosine Similarity to find the most relevant answer from the MedQuAD dataset.

A clean web interface is built using **Streamlit**.

---

## Features

- Retrieval-based Question Answering using MedQuAD dataset
- TF-IDF + Cosine Similarity for finding relevant answers
- Basic Medical Entity Recognition (Diseases, Symptoms, Treatments)
- Simple and clean Streamlit User Interface
- Educational purpose only (not a real doctor)

---

## Dataset

**MedQuAD – Medical Question Answering Dataset**

- Contains thousands of real medical question-answer pairs
- Collected from trusted NIH websites
- Used for retrieving accurate medical answers

---

## Technologies Used

| Technology       | Purpose                          |
|------------------|----------------------------------|
| Python           | Main programming language        |
| Streamlit        | Web User Interface               |
| Pandas           | Dataset handling                 |
| Scikit-learn     | TF-IDF & Cosine Similarity       |
| MedQuAD Dataset  | Medical knowledge base           |

---

## How to Run

### 1. Install required libraries

```bash
pip install streamlit pandas scikit-learn
