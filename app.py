# Import the Flask class from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class, passing the name of the module as an argument
app = Flask(__name__)


@app.route('/')  # Define a route for the root URL
def index():
    # Render the index.html template when the root URL is accessed
    return render_template('index.html')


# Run the Flask app on port 50001 with debug mode enabled
app.run(debug=True, port=50001)
