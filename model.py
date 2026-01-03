import tensorflow as tf
import numpy as np

def train_model(text):

    if len(text) < 200:
        raise ValueError("Please add more text to handwritten.txt (min 200 characters)")
        
    vocab = sorted(set(text))
    char2idx = {u: i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab)

    text_as_int = np.array([char2idx[c] for c in text]
                           
    seq_length = 40

    X = []
    y = []

    for i in range(len(text_as_int) - seq_length):
        X.append(text_as_int[i:i+seq_length])
        y.append(text_as_int[i+1:i+seq_length+1])

    X = np.array(X)
    y = np.array(y)

    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(len(vocab), 128),
        tf.keras.layers.SimpleRNN(256, return_sequences=True),
        tf.keras.layers.Dense(len(vocab))
    ])

    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    )

    model.fit(X, y, epochs=10, batch_size=16, verbose=1)

    return model, char2idx, idx2char

