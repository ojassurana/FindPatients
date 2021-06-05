from flask import Flask, redirect, url_for, render_template, request
import pymongo
import os


client = pymongo.MongoClient("mongodb+srv://ojas:Ojulala02@cluster0.kfpcm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('UserData')
Information_Collection = db.get_collection("Information")
Items = [ "Oxygen Cylinder", "Hospital Bed",  "Plasma",  "Remedisvir",  "Fabiflu", "Tocilizumbad", "Oxygen Refill","All Items"]
application = Flask(__name__)

@application.route("/", methods = ["POST","GET"])
def home():
	return render_template("index.html")
	
@application.route("/find",methods =  ["POST","GET"])
def find():
	recipients = []
	donations = request.form["Donation"] 
	location = request.form["Location"]

	if donations == "All Items" and location =="All Locations":
		out = Information_Collection.find()
		for i in out:
			if len(i) == 5:
				recipients.append(i)
		if recipients == []:
			return render_template("nil.html")
		return render_template("results.html",recipients = recipients, donation = 8 ,location="All Locations",items = Items)
	
	if donations == "All Items":
		out = Information_Collection.find({"Location":{"$eq":location}})
		for i in out:
			if len(i) == 5:
				recipients.append(i)
		if recipients == []:
			return render_template("nil.html")
		return render_template("results.html",recipients = recipients, donation = 8 ,location=location,items = Items)
	
	if location == "All Locations":
		donation = Items.index(donations) +1
		out = Information_Collection.find({"Item":{"$eq":donation}})
		for i in out:
			if len(i) == 5:
				recipients.append(i)
		if recipients == []:
			return render_template("nil.html")
		return render_template("results.html",recipients = recipients, donation = donation ,location="All Locations",items = Items)

	donation = Items.index(donations)+1
	out = Information_Collection.find( {"$and":[{"Item":{"$eq":donation}},{"Location":{"$eq":location}}]}   )           

	for i in out:
		if len(i) == 5:
				recipients.append(i)
	if recipients == []:
		return render_template("nil.html")
	return render_template("results.html",recipients = recipients, donation = donation ,location=location,items = Items)
	
	
if __name__ == "__main__":


	application.run(debug=True)
