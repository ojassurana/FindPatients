from flask import Flask, redirect, url_for, render_template, request
import pymongo
import os


client = pymongo.MongoClient("mongodb+srv://ojas:Ojulala02@cluster0.kfpcm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('UserData')
Information_Collection = db.get_collection("Information")
Items = { "Oxygen Cylinder":1, "Hospital Bed":2,  "Plasma" : 3,  "Remedisvir":4,  "Fabiflu" : 5, "Tocilizumbad":6, "Oxygen Refill":7}
application = Flask(__name__)

@application.route("/", methods = ["POST","GET"])
def home():
	return render_template("index.html")
	
@application.route("/find",methods =  ["POST","GET"])
def find():

	Items = { "Oxygen Cylinder":1, "Hospital Bed":2,  "Plasma" : 3,  "Remedisvir":4,  "Fabiflu" : 5, "Tocilizumbad":6, "Oxygen Refill":7}

	donations = request.form["Donation"] 
	donation = Items[donations]
	location = request.form["Location"]

	out = Information_Collection.find( {"$and":[{"Item":{"$eq":donation}},{"Location":{"$eq":location}}]}   )           



	recipients = []
	for i in out:
		recipients.append(i)
	if recipients == []:
		return render_template("nil.html")
	return render_template("results.html",recipients = recipients, donation = donations ,location=location)
	
	
if __name__ == "__main__":


	application.run(debug=True)
