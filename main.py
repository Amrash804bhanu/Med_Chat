from flask import Flask, render_template, request
import google.generativeai as genai
import textwrap
import os
import cv2
from PIL import Image

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

@app.route('/chat', methods=['POST','GET'])

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['text_input']

    # Send the message to the model
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text
 # Adjust width as needed

 # Format the text into points and structured paragraphs



    # Update history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})


    

    # Format the model response into points using textwrap
   
     # Adjust width as needed
    # Convert newlines to HTML breaks
    

    return render_template("main.html", comments=history)





if __name__=="__main__":
    app.run(debug=True)

