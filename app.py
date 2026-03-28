# Import the Flask class from the flask module
from flask import Flask, render_template, request

# Create an instance of the Flask class, passing the name of the module as an argument
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # Define a route for the root URL
def index():
    if request.method == 'POST':
        # Handle form submission here (e.g., save data, send email, etc.)
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        date = request.form.get('date')
        occupation = request.form.get('occupation')
    # Render the index.html template when the root URL is accessed
    return render_template('index.html')


# Run the Flask app on port 50001 with debug mode enabled
app.run(debug=True, port=50001)
