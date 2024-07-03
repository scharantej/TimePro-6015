**Flask Application Design for Smart Time**

**HTML Files:**

* **index.html:**
    - Main page of the website
    - Contains a form for users to input their tasks and time slots
* **calendar.html:**
    - Displays a personalized planner based on the user's input
    - Allows users to manage their schedule and stay organized

**Routes:**

* **@app.route('/')**
    - Handles the home page display (index.html)
* **@app.route('/process', methods=['POST'])**
    - Processes the task and time slot input from the form
    - Generates and displays the customized calendar (calendar.html)