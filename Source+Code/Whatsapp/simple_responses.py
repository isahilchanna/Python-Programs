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
    return str(response)


if __name__ == "__main__":
    app.run(port=5000)
