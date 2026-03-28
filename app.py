# Import the Flask class from the flask module
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import os

# Create an instance of the Flask class, passing the name of the module as an argument
app = Flask(__name__)

# Set the secret key for the Flask application and configure the SQLAlchemy database URI
app.config["SECRET_KEY"] = "myapp123"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config["MAIL_USERNAME"] = "hbbianalytics@gmail.com"
# The password is stored in environment variables, which we access via the os library
app.config["MAIL_PASSWORD"] = os.getenv("PASSWORD")
# Create an instance of the SQLAlchemy class, passing the Flask app as an argument
db = SQLAlchemy(app)

# Create an instance of the Mail class, passing the Flask app as an argument
mail = Mail(app)

# Define a model class for the form data, which will be stored in the database


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date = db.Column(db.Date, nullable=False)
    occupation = db.Column(db.String(100), nullable=False)


@app.route('/', methods=['GET', 'POST'])  # Define a route for the root URL
def index():
    if request.method == 'POST':
        # Handle form submission here (e.g., save data, send email, etc.)
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        date = request.form.get('date')
        # Convert string to date object
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        occupation = request.form.get('occupation')

        # Create a new Form instance with the submitted data and add it to the database
        form = Form(first_name=first_name, last_name=last_name,
                    email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message_body = f"Dear {first_name} {last_name},\n\nThank you for submitting the form."\
            f"Here are the details you provided:\n\n"\
            f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nDate: {date}\nOccupation: {occupation}\n\nBest regards,\nYour Company"
        message = Message(subject="Form Submission Confirmation",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)
        mail.send(message)

        # Flash a success message to the user
        flash(
            f"{first_name} {last_name}, your form was submitted successfully!", 'success')

    # Render the index.html template when the root URL is accessed
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
        # Run the Flask app on port 50001 with debug mode enabled
        app.run(debug=True, port=50001)
