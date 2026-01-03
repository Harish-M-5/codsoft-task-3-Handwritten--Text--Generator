# ✍️ Handwritten Text Generation using Character-Level RNN
### CodSoft Machine Learning Internship – Task 3

---

## 📌 Description
This project implements a **character-level Recurrent Neural Network (RNN)** to generate handwritten-like text patterns.  
The model is trained on a handwritten text dataset and learns sequential character dependencies to generate new, realistic text outputs.

This project is developed as part of the **CodSoft Machine Learning Internship – Task 3**.

---

## 📖 Introduction
Handwriting is a unique human expression that reflects emotions, personality, and creativity.  
In this project, a Machine Learning model is trained to understand handwritten text patterns at the character level and generate new text that mimics handwritten writing style.

---

## 🔍 Overview
- Uses **character-level RNN**
- Trained on handwritten-style text dataset
- Generates new text based on learned character patterns
- Integrated with a **Streamlit frontend** for interactive and colorful UI
- Beginner-friendly and internship-ready implementation

---

## 🛠️ Technology Used

| Technology | Purpose |
|-----------|--------|
| Python | Core programming language |
| TensorFlow / Keras | Building and training RNN model |
| NumPy | Numerical operations |
| Streamlit | Frontend UI |
| VS Code | Development environment |

---

## 📄 handwritten.txt (Dataset Explanation)
The `handwritten.txt` file contains handwritten-style English text.  
This text acts as the training data for the RNN model.

- Data is **plain text**
- No images required
- Model learns **character-by-character patterns**
- More text → better generation quality

Example:
Dear friend,
This letter is written slowly with care and patience.
Handwriting reflects emotions and thoughts.

---

---

## 🔁 RNN Explanation
Recurrent Neural Networks (RNNs) are designed to process **sequential data**.

Why RNN?
- Maintains memory of previous characters
- Learns dependencies between characters
- Ideal for text generation tasks

In this project, RNN predicts the **next character** based on previous characters.

---

## Project Setup

Handwritten_Text_Generation/
│
├── app.py             
├── model.py               
├── handwritten.txt       
├── requirements.txt      
└── README.md              

---

## project setup

🖥️ Environment Setup

1️⃣ Install Python
Python version
Verify:

``Bash
python --version


2️⃣ Create Project Folder

``Bash
mkdir Handwritten_Text_Generation
cd Handwritten_Text_Generation

3️⃣ Create Virtual Environme

``Bash
python -m venv 

4️⃣ Install Dependencies
Create requirements.txt:
Txt
tensorflow
numpy
streamlit

Install:
``Bash
pip install -r requirements.txt


5️⃣ Dataset Setup
Create handwritten.txt and add handwritten-style text


6️⃣ Run Project
``Bash
streamlit run app.py


---


## 🧠 Model Architecture

1. **Embedding Layer**
   - Converts characters into dense vectors

2. **SimpleRNN Layer**
   - Learns sequential character dependencies

3. **Dense Layer**
   - Predicts the next character from vocabulary


---


## demo video


https://github.com/user-attachments/assets/f207cd26-2047-467d-b7db-02a733069749

---

## output
<img width="1920" height="1080" alt="Screenshot 2026-01-03 203221" src="https://github.com/user-attachments/assets/d3d8dad3-73fa-4534-8a33-716f416f3b7d" />


---
## 🙏 Acknowledgments

- CodSoft for providing the internship opportunity

- TensorFlow and Streamlit documentation

- Open-source ML community

---

## ✅ Result

The trained RNN successfully generates handwritten-style text based on the learned patterns from the dataset.
The Streamlit interface allows users to interactively generate text with a visually appealing UI.

This project fulfills CodSoft Machine Learning Internship – Task 3 requirements successfully.
