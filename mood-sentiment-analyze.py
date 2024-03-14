from flask import Flask, request, jsonify
from flask_cors import CORS


import numpy as np # linear algebra
import pandas as pd 





import pandas as pd
import numpy as np
import keras
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense


app = Flask(__name__)
CORS(app)


df = pd.read_csv('train[1].txt',sep=';')
df.head()

df.columns = ["Text", "Emotions"]









texts=df["Text"].tolist()
labels=df["Emotions"].tolist()





tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)





sequences = tokenizer.texts_to_sequences(texts)
max_length = max([len(seq) for seq in sequences])
padded_sequences = pad_sequences(sequences, maxlen=max_length)







label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)





one_hot_labels = keras.utils.to_categorical(labels)





xtrain, xtest, ytrain, ytest = train_test_split(padded_sequences, one_hot_labels, test_size=0.2)




model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=128))
model.add(Flatten())
model.add(Dense(units=128, activation="relu"))
model.add(Dense(units=len(one_hot_labels[0]), activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(xtrain, ytrain, epochs=10, batch_size=60, validation_data=(xtest, ytest))






















import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Define the classifying emotions function
def classify_emotion(input_text, model, tokenizer, max_length):
    # Process the input text using the tokenizer
    input_sequence = tokenizer.texts_to_sequences([input_text])
    padded_input_sequence = pad_sequences(input_sequence, maxlen=max_length)

    # Make a prediction using the model
    prediction = model.predict(padded_input_sequence)

    # Map the prediction to the corresponding emotion label
    emotion_labels = ['anger', 'fear', 'joy', 'love', 'sad', 'surprise']
    predicted_emotion = emotion_labels[np.argmax(prediction)]

    return predicted_emotion

# Assuming predicted_emotion contains the predicted emotion# Replace with the actual predicted emotion


def response(predicted_emotion):
    if predicted_emotion == "sad":
        return [165,
            "You seem to be feeling sad. It's ok to feel this way. It's important to acknowledge your emotions and seek support from friends, family, or professionals if needed. Sadness is a natural emotion, and it's important to give yourself the time and space to process and address what's causing your sadness. Consider engaging in activities that bring comfort and help you navigate through this emotion. It may be beneficial to engage in self-care practices, such as going for a walk, reading, or listening to music, to help uplift your spirits during this time.",
            
        ]

    elif predicted_emotion == "joy":
        return[15,
               "Your joy is evident! It's wonderful to experience joy. Celebrating joy can bring a sense of fulfillment and positivity into your life. Consider sharing your joyful moments with others, as sharing joy often amplifies its impact and spreads happiness.Engage in activities that bring you joy, whether it's pursuing a hobby, spending time with loved ones, or simply taking a moment to appreciate the small victories and moments of happiness in your day."]
        

    elif predicted_emotion == "anger":
        return[135,
               "It seems like you're experiencing anger. Anger is a natural emotion, and it's important to find healthy ways to manage and express it. Recognize the triggers that lead to your anger and consider seeking professional guidance to channel it constructively.Engaging in relaxation techniques such as deep breathing, meditation, or physical exercise can provide a constructive outlet for managing and alleviating feelings of anger."]
        

    elif predicted_emotion == "fear":
        return[100,
               "It sounds like you are feeling fearful. Fear is a common emotion, and it's okay to seek support and reassurance when feeling afraid. Identify the sources of your fear and take steps to address or minimize them.Consider reaching out to trusted individuals or professionals to help alleviate your fears. Engaging in activities that promote a sense of security and tranquility can be beneficial in managing feelings of fear."]
        

    elif predicted_emotion == "love":
        return[45,
               "You seem to be feeling love. Embracing and nurturing this emotion can bring warmth and fulfillment to your life and relationships. Expressing your love and gratitude towards others can create a positive and supportive environment.Reflect on the sources of love in your life, whether it's relationships, personal passions, or acts of kindness. Nurturing and celebrating love can contribute to an enriched and meaningful lifestyle."]
        

    elif predicted_emotion == "surprise":
        return[75,
               "It seems like you're feeling surprised. Embrace this unexpected emotion, and take a moment to reflect on its impact and significance. Explore the reasons behind your surprise and consider how it fits into your current experiences and perceptions.Embracing surprises can lead to new experiences and perspectives, potentially bringing a sense of excitement and wonder. Open yourself to the possibilities that come with embracing the unexpected."]
          

# In[ ]:

@app.route('/process_commute2', methods=['POST'])
def process_transcript():
    user_input = request.form['response']
    print("Transcript: ",user_input)
    predicted_emotion = classify_emotion(user_input, model, tokenizer, max_length)
    data = response(predicted_emotion)
    print("Response: ", data)
    return data

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)




