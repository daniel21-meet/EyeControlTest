from flask import Flask, jsonify, request, render_template
import random
import requests,json

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
url = "https://api.gazerecorder.com/GazeCloudAPI.js"
response = requests.request("GET", url)

print(response.text)


@app.route('/')  # '/' for the default page
def home():
  return render_template('index.html')


@app.route('/eyetest' , methods=["GET","POST"])
def eyetest():
		if request.method == 'GET':
			return render_template('home.html')
		else:
			url = "https://api.gazerecorder.com/GazeCloudAPI.js"
			response = requests.request("GET")

		print(response.text)
		return render_template('eyetest.html')


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)

