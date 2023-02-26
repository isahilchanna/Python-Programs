from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime
cluster = MongoClient("mongodb+srv://jai:jai@cluster0.pskcruw.mongodb.net/?retryWrites=true&w=majority")
db = cluster ["bakery"]
users = db["users"]
orders = db["orders"]
app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:","")
    res = MessagingResponse()
    user = users.find_one({"number" :number})

    if bool(user) == False:
        res.message("Hi,Thanks for contacting *The Red Velvet.*\n you can choose from one of the options below:" "\n\n *Type*\n\n 1️⃣ *Contact* us\n 2️⃣️ To                       *Orders*\n 3️⃣ To know our *working hours*\n 4️⃣ To get our *Address*")
        users.insert_one({"number": number, "status": "main", "Messages":[]})
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            res.message("please enter a valid response")
            return str(res)
        if option == 1:
            res.message("You can contact us through phone or email.\n\n*Phone*: +98 991 33700 *E-Mail*:ccmgurgaon@gmail.com")
        elif option == 2:
            res.message("You have *Ordering Mode*")
            users.update_one({"number":number}, {"$set": {"status": "Ordering"}})
            res.message("You can select one of the following cakes to Order:\n\n 1️⃣ Red Velvet \n 2️⃣ Dark Foresst \n 3️⃣ ICE Creame\n 4️⃣ Plum Cake \n 5️⃣ Sponge Cake \n 6️⃣ Genoise Cake \n 7️⃣ Carrot Cake \n 8️⃣ ButterScoch Cake \n 0️⃣ GoBack")
        elif option == 3:
            res.message("Weare working from *9 AM to 6 PM*")
        elif option == 4:
            res.message("We have multiple stores across the city.Our Main Centre is at *4/54, New Delhi*")
        else:
            res.message("please enter a valid response")
            return str(res)
    users.update_one({"number": number}, {"$push": {"text":text, "date":datetime.now()}})
    return str(res)
if __name__ == "__main__":
    app.run(port=5000)