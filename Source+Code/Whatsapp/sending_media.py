from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    response = MessagingResponse()
    msg = response.message(f"Thanks for contacting me. You have sent '{text}' from {number[:-2]}")
    msg.media("https://images.unsplash.com/photo-1609220136506-e592262f2376?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max")
    return str(response)


if __name__ == "__main__":
    app.run(port=5000)
