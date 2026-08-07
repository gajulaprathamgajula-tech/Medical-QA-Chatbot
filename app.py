# app.py
# Medical Q&A Chatbot using MedQuAD Dataset

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Medical Q&A Chatbot",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Medical Q&A Chatbot")
st.markdown("Ask any medical question. This bot uses the **MedQuAD** dataset.")
st.info("⚠️ This is for educational purposes only. Not a real doctor.")

# ---------------- Load Dataset ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("medquad.csv")   # Make sure the file name matches
    df = df.dropna(subset=["question", "answer"])
    df = df.reset_index(drop=True)
    return df

df = load_data()

# ---------------- TF-IDF Retrieval ----------------
@st.cache_resource
def build_vectorizer(data):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(data["question"])
    return vectorizer, tfidf_matrix

vectorizer, tfidf_matrix = build_vectorizer(df)

def retrieve_answer(user_question, top_k=1):
    user_vec = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]
    
    results = []
    for idx in top_indices:
        results.append({
            "question": df.loc[idx, "question"],
            "answer": df.loc[idx, "answer"],
            "score": similarities[idx]
        })
    return results

# ---------------- Simple Medical Entity Recognition ----------------
def extract_entities(text):
    text = text.lower()
    
    diseases = ["diabetes", "cancer", "asthma", "hypertension", "covid", "flu", 
                "migraine", "arthritis", "depression", "anxiety", "glaucoma", "anemia"]
    symptoms = ["fever", "cough", "headache", "pain", "fatigue", "nausea", 
                "vomiting", "dizziness", "rash", "swelling", "shortness of breath"]
    treatments = ["medicine", "surgery", "therapy", "insulin", "antibiotic", 
                  "vaccine", "chemotherapy", "physiotherapy"]
    
    found_diseases = [d for d in diseases if d in text]
    found_symptoms = [s for s in symptoms if s in text]
    found_treatments = [t for t in treatments if t in text]
    
    return found_diseases, found_symptoms, found_treatments

# ---------------- Streamlit UI ----------------
user_question = st.text_input("Enter your medical question here:")

if st.button("Get Answer") or user_question:
    if user_question.strip() == "":
        st.warning("Please type a question.")
    else:
        with st.spinner("Searching medical knowledge..."):
            results = retrieve_answer(user_question)
            best = results[0]
            
            # Entity Recognition
            diseases, symptoms, treatments = extract_entities(user_question)
            
            st.subheader("Answer")
            st.write(best["answer"])
            
            st.markdown("---")
            st.subheader("Detected Medical Entities")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("**Diseases:**")
                st.write(", ".join(diseases) if diseases else "None")
            with col2:
                st.write("**Symptoms:**")
                st.write(", ".join(symptoms) if symptoms else "None")
            with col3:
                st.write("**Treatments:**")
                st.write(", ".join(treatments) if treatments else "None")
            
            st.markdown("---")
            st.caption(f"Matched Question: {best['question']}")
            st.caption(f"Similarity Score: {best['score']:.2f}")

st.markdown("---")
st.markdown("**Dataset:** MedQuAD (Medical Question Answering Dataset)")