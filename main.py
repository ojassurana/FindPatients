from flask import Flask, redirect, url_for, render_template, request
import pymongo
import os




app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def home():
	if request.method == "POST":
		donations = request.form["Donation"] 
		donation = Items[donations]
		location = request.form["Location"]

		print(donation)

		out = Information_Collection.find( {"$and":[{"Item":{"$eq":donation}},{"Location":{"$eq":location}}]}   )           


		recipients = []
		for i in out:
			print(i)
			recipients.append(i)
			print(recipients)
		if recipients == []:
			return render_template("nil.html")
		return render_template("results.html",recipients = recipients, donation = donations ,location=location)


	return render_template("index.html")
	
	
	
	
if __name__ == "__main__":
	client = pymongo.MongoClient("mongodb+srv://ojas:Ojulala02@cluster0.kfpcm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	db = client.get_database('UserData')
	Information_Collection = db.get_collection("Information")
	Items = { "Oxygen Cylinder":1, "Hospital Bed":2,  "Plasma" : 3,  "Remedisvir":4,  "Fabiflu" : 5, "Tocilizumbad":6, "Oxygen Refill":7}

	app.run(debug=True)
