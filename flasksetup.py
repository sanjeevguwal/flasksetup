from flask import Flask
app = Flask(flasksetup)
@app.route("https://github.com/sanjeevguwal/flasksetup/new/main")#URL leading to method
def hello(): # Name of the method
 	return("Hello World!") #indent this line
  if flasksetup == "__main__":
	app.run(host='0.0.0.0', port='8080') # indent this line
