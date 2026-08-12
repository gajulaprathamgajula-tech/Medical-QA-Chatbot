# 🏥 Medical Q&A Chatbot

> **Internship Task #2 — Elevance Skills**  
> A domain-specific medical question-answering chatbot built using the **MedQuAD dataset**, **TF-IDF**, **Cosine Similarity**, basic **medical entity recognition**, and **Streamlit**.

---

## 📌 Overview

The **Medical Q&A Chatbot** is a domain-specific conversational application designed to answer medical questions by retrieving relevant information from the **MedQuAD dataset**.

Instead of generating arbitrary medical responses, the system uses a retrieval-based Natural Language Processing (NLP) approach. A user's question is compared against medical questions stored in the knowledge base, and the most relevant answer is retrieved based on textual similarity.

The project demonstrates how a general conversational chatbot can be extended into a specialized domain by integrating a structured knowledge base and information-retrieval pipeline.

The system also performs basic medical entity recognition to identify important medical terms such as diseases, symptoms, treatments, and medical conditions.

A **Streamlit** interface provides a simple way for users to interact with the chatbot.

---

# 🔗 Connection to the Training Project

This project was developed as an extension of the **Real-Time Gen-AI Customer Support Chatbot** completed during the Elevance Skills training program.

The training project established the basic conversational chatbot concept. This internship task extends that foundation by introducing a specialized medical knowledge domain.

```text
                 TRAINING PROJECT
                       │
                       ▼
          Real-Time Gen-AI Customer
             Support Chatbot
                       │
                       ▼
                INTERNSHIP TASK #2
                       │
                       ▼
             Medical Domain Extension
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     MedQuAD       Retrieval       Medical
     Dataset        System           NER
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                Streamlit Chatbot
