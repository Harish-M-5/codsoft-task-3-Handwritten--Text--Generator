import streamlit as st
import tensorflow as tf
import numpy as np
from model import train_model

st.set_page_config(
    page_title="Handwritten Text Generator",
    page_icon="✍️",
    layout="centered"
)

st.markdown("""
<style>
body {
    background: linear-gradient(to right, #1e3c72, #2a5298);
}
.main {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("✍️ Handwritten Text Generator")
st.subheader("Character-level RNN using Machine Learning")

with open("handwritten.txt", "r", encoding="utf-8") as f:
    text = f.read()

with st.spinner("Training model... please wait ⏳"):
    model, char2idx, idx2char = train_model(text)

st.success("Model trained successfully ✅")

start_string = st.text_input("Enter starting text:", "Dear")
length = st.slider("Text length", 100, 500, 300)

def generate_text(model, start_string):
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []
    temperature = 0.8

    for i in range(length):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions / temperature

        predicted_id = tf.random.categorical(
            predictions[-1:], num_samples=1
        )[0][0].numpy()

        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char[predicted_id])

    return start_string + ''.join(text_generated)

if st.button("✨ Generate Handwritten Text"):
    output = generate_text(model, start_string)
    st.text_area("Generated Text", output, height=300)

