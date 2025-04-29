from flask import Flask, render_template,request, redirect, url_for

app=Flask(__name__)


@app.route("/")
def index():
    return ("welcome to the user")

    

@app.route("/login",methods=["POST","GET"])
def login():
    return render_template("login.html")


@app.route('/<usr>')
def main(usr):
    return f"<h1>{usr}</h1>"






if __name__=="__main__":
    app.run(debug=True)
 


 #chat that excutes the text 
#  def chat():
#     user_input = request.form['text_input']

#     # Send the message to the model
#     chat_session = model.start_chat(history=history)
#     response = chat_session.send_message(user_input)
#     model_response = response.text,response.image

#     # Update history
#     history.append({"role": "You", "parts": [user_input]})
#     history.append({"role": "Aisha", "parts": [model_response]})

#     return render_template("main.html", comments=history)