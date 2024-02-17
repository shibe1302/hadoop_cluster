# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template,request,redirect,url_for
import csv
import db
import sqlite3

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# data1=[]
# with open('cao_anh\link.csv', newline='') as csvfile:
# 	data1 = list(csv.reader(csvfile, delimiter=','))
# 	csvfile.close

conn1=sqlite3.connect("data_img.db",check_same_thread=False)

cc=conn1.cursor()	
aa=db.top(conn1,cc,20)


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/',methods=["POST","GET"])
def hello_world():
	if request.method=="POST":
		search=request.form["input1"]
		print(type(search))
		bb=db.search(conn1,cc,search)
		return render_template("home.html",link_img=bb)

	else:
		return render_template("home.html",link_img=aa)

@app.route('/result')
def result(link_img):
	return render_template("home.html",link_img=link_img)
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run(debug=True)
