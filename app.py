"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
 


import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
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
print("Aisha:how can I help you ?")

while True:
    user_input = input("You: ")



    chat_session = model.start_chat(
      history=history
)

    response = chat_session.send_message(user_input)

    model_response =response.text

    print(model_response)
    print(f'Aisha:{model_response}')

    history.append({"role": "user" ,"parts":[user_input]})
    history.append({"role":"model","parts":[model_response]})



