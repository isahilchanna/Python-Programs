from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=60
app.config['MAIL_USERNAME']='lucifer.ai.288@gmail.com'
app.config['MAIL_PASSWORD']='mfbjcjevynjezpaz'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route("/")
def index():
    msg=Message('Hello',sender="lucifer.ai.288@gmail.com",recipients=['sahilchanna14@gmail.com'])
    msg.body ='Hello Flask! This message is sent from Flask-Mail'
    mail.send(msg)
    return "Message sent"

if __name__=='__main__':
    app.run(debug=True)