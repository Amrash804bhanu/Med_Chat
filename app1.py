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

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    user_input = request.form['text_input']

    # Send the message to the model
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text

    # Format the text into points and structured paragraphs
    formatted_text = format_text(model_response)  # Call the new formatting function

    # Update history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [formatted_text]})

    return render_template("main.html", comments=history)


def format_text(text):
    """Formats text into points and structured paragraphs with headings and subheadings."""

    # Adjust width as needed
    formatted_text = textwrap.fill(text, width=70, subsequent_indent="  * ")

    # Split the formatted text into paragraphs based on blank lines
    paragraphs = formatted_text.split("\n\n")

    # Create a list to store the formatted paragraphs with headings and subheadings
    formatted_paragraphs = []

    # Iterate through the paragraphs and add headings and subheadings as needed
    for paragraph in paragraphs:
        if paragraph.startswith("**"):
            heading = paragraph.strip("**")
            formatted_paragraphs.append(f"<h3>{heading}</h3>")
        elif paragraph.startswith("*"):
            subheading = paragraph.strip("*")
            formatted_paragraphs.append(f"<p>{subheading}</p>")
        else:
            formatted_paragraphs.append(f"<p>{paragraph}</p>")

    # Join the formatted paragraphs into a single string
    formatted_text = "\n".join(formatted_paragraphs)

    return formatted_text


if __name__ == "__main__":
    app.run(debug=True)