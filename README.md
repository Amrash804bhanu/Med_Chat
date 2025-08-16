# Med_Chat

Med_Chat is an intelligent chatbot application for medical conversations. It leverages Google's Gemini API for natural language understanding and generation, and is built using Flask for seamless web integration. The goal is to provide accurate, context-aware assistance for healthcare-related queries, illustrating modern AI integration skills in backend development.

---

## Table of Contents
- Features
- Installation
- Usage
- Technologies Used
- Project Structure
- API Documentation
- Testing
- License
- Contact

---

## Features

- Real-time medical chat powered by Gemini API
- RESTful integration using Flask
- Secure handling of user input
- Scalable modular backend
- Demonstrates prompt engineering and API orchestration
- Customizable for additional healthcare APIs

---

## Installation Instructions

**Prerequisites:**
- Python 3.8+
- Flask
- Gemini API access/key

**Steps:**

1. Clone the repository:
    ```
    git clone https://github.com/Amrash804bhanu/Med_Chat
    cd Med_Chat
    ```

2. Install required dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Set your Gemini API credentials in environment variables or within config as instructed.

4. Run the Flask app:
    ```
    python app.py
    ```
    The server will start on localhost. Access via your browser at `http://127.0.0.1:5000/`.

---

## Usage

- Enter medical queries in the chat interface.
- The chatbot processes input via Gemini API and responds with relevant medical information.
- Example interaction:
    ```
    User: What are the symptoms of flu?
    Chatbot: Common symptoms include fever, cough, sore throat, fatigue, and body aches.
    ```


---

## Technologies Used

- **Core Language & Framework:** Python, Flask
- **AI & NLP:** Google Gemini API
- **Methodology:** REST API integration, prompt engineering
- **Dev Tools:** GitHub, virtualenv

---

## API Documentation

- **Endpoint:** `/chat`
    - **Method:** POST
    - **Parameters:** `{ "message": "user input" }`
    - **Response:** `{ "reply": "chatbot response" }`
    - **Example:**
      ```
      curl -X POST -H "Content-Type: application/json" -d '{"message": "What is hypertension?"}' http://127.0.0.1:5000/chat
      ```

---

## Testing

- Test scripts provided in `/tests`
- Run tests using:
    ```
    python -m unittest discover tests
    ```
- Coverage includes correct route handling, API response integrity, error cases.

---




