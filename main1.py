from flask import Flask, render_template, request
import google.generativeai as genai
import textwrap
import os
import cv2
from PIL import Image
import random
import librosa
import tensorflow as tf

# Load pre-trained models (adjust paths as needed)
image_model = tf.keras.models.load_model('your_image_analysis_model.h5')
audio_model = tf.keras.models.load_model('your_audio_analysis_model.h5')

api_key = os.getenv("GEMINI_API_KEY")
app = Flask(__name__)

# Model configuration (place outside routes)
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)
history = []

@app.route('/')
def index():
    return render_template("main.html", comments=[])

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['text_input']
    image_file = request.files.get('image_file')
    audio_file = request.files.get('audio_file')

    # Send the message to the model
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text

    # Handle image analysis
    if image_file:
        # Load the image
        img = Image.open(image_file.stream.read())

        # Preprocess the image (adjust as needed)
        img = img.resize((224, 224))  # Assuming your model expects 224x224 images
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = img / 255.0  # Normalize pixel values

        # Make a prediction using the pre-trained image model
        prediction = image_model.predict(tf.expand_dims(img, axis=0))

        # Interpret the prediction (adjust based on your model's output)
        predicted_class = tf.argmax(prediction, axis=-1)
        class_labels = ["class1", "class2", ...]  # Replace with your class labels
        predicted_label = class_labels[predicted_class.numpy()[0]]

        # Generate a text response based on the prediction
        image_analysis_result = f"The image is likely classified as: {predicted_label}"
        model_response += "\n" + image_analysis_result

    # Handle audio analysis
    if audio_file:
        # Load the audio
        audio_data, sample_rate = librosa.load(audio_file.stream.read())

        # Preprocess the audio (adjust as needed)
        mfcc = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=40)
        mfcc = mfcc.T  # Transpose to match model input shape

        # Make a prediction using the pre-trained audio model
        prediction = audio_model.predict(mfcc[None, :, :])

        # Interpret the prediction (adjust based on your model's output)
        predicted_class = tf.argmax(prediction, axis=-1)
        class_labels = ["class1", "class2", ...]  # Replace with your class labels
        predicted_label = class_labels[predicted_class.numpy()[0]]

        # Generate a text response based on the prediction
        audio_analysis_result = f"The audio is likely classified as: {predicted_label}"
        model_response += "\n" + audio_analysis_result

    # Update history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})

    # Format the model response into points using textwrap
    # ...

    return render_template("main.html", comments=history)

if __name__=="__main__":
    app.run(debug=True)
    