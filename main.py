
# Main Python code for the Flask application, Smart Time, that generates a personalized planner
# Import the necessary modules
from flask import Flask, render_template, request

# Create a Flask application instance
app = Flask(__name__)

# Define the main route for the home page
@app.route('/')
def home():
    """Render the home page with the input form."""
    return render_template('index.html')

# Define the route for processing the user's input and displaying the calendar
@app.route('/process', methods=['POST'])
def process():
    """Process the input, generate a calendar, and display it."""
    # Extract the task and time slot information from the form
    tasks = request.form.getlist('task')  # Get all the tasks
    time_slots = request.form.getlist('time_slot')  # Get all the time slots

    # Create a dictionary to store the tasks and time slots
    schedule = dict(zip(tasks, time_slots))

    # Generate the personalized calendar using sample data
    calendar = [
        {'time': '9:00 AM - 10:00 AM', 'task': schedule.get('Task 1', '')},
        {'time': '10:00 AM - 11:00 AM', 'task': schedule.get('Task 2', '')},
        {'time': '11:00 AM - 12:00 PM', 'task': schedule.get('Task 3', '')},
        {'time': '1:00 PM - 2:00 PM', 'task': schedule.get('Task 4', '')},
        {'time': '2:00 PM - 3:00 PM', 'task': schedule.get('Task 5', '')},
    ]

    # Render the calendar page with the generated calendar
    return render_template('calendar.html', calendar=calendar)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
