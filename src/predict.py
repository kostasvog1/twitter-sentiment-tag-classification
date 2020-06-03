import os
import time
import pickle
from keras.preprocessing.sequence import pad_sequences
os.chdir('C:\\Users\\kosta\\Desktop\\projects\\twitter\src')
from decode_sentiment import decode_sentiment


def predict(text,SEQUENCE_LENGTH, saved_tokenizer=None,saved_model=None,include_neutral=True):

    start_at = time.time()
    # Tokenize text
    x_test = pad_sequences(saved_tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    # Predict
    score = saved_model.predict([x_test])[0]
    # Decode sentiment
    label = decode_sentiment(score, include_neutral=include_neutral)

    return {"label": label, "score": float(score),
       "elapsed_time": time.time()-start_at}  