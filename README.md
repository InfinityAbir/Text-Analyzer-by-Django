# Text-Analyzer-by-Django
Text Utils
Text Utils is a simple Django web application that allows users to analyze and manipulate text. Users can input text and apply operations such as removing punctuation, converting to uppercase, and removing new lines. The application is built using Django for the backend, Bootstrap for the frontend, and provides a clean, user-friendly interface.
Features

Remove Punctuation: Strip punctuation marks from the input text.
Convert to Uppercase: Transform the input text to all uppercase letters.
Remove New Lines: Eliminate newline characters from the text.
Responsive Design: Built with Bootstrap for a mobile-friendly interface.
Simple Navigation: Includes a navigation bar with Home, About Us, and Contact Us links (placeholders for future expansion).

Technologies Used

Django: Python-based web framework for backend development.
Bootstrap 5: Frontend framework for responsive and styled UI.
HTML/CSS: For structuring and styling the web pages.
Python: Core programming language for the application logic.

Installation
Follow these steps to set up the project locally:
Prerequisites

Python 3.8 or higher
pip (Python package manager)
Virtualenv (recommended for isolated environments)

Steps

Clone the Repository:
git clone https://github.com/IndiniryAbir/text-utils.git
cd text-utils


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install django


Run the Development Server:
python manage.py runserver


Access the Application:Open your browser and navigate to http://127.0.0.1:8000.


Project Structure
text-utils/
├── textutils/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── templates/
│   ├── index.html
│   └── analyze.html
├── manage.py
└── README.md


urls.py: Defines URL routing for the application.
views.py: Contains the logic for handling requests and text processing.
index.html: The main page with the text input form.
analyze.html: Displays the analyzed text output.
manage.py: Django's command-line utility for administrative tasks.

Usage

Navigate to the homepage (/).
Enter text in the provided textarea.
Select one or more text operations (Remove Punctuation, Uppercase, Remove New Lines).
Click the "Analyze Text" button to see the processed text on the analyze page.

Future Improvements

Add more text manipulation features (e.g., word count, character count, lowercase conversion).
Implement user authentication for personalized features.
Enhance the UI with custom CSS and additional Bootstrap components.
Add functional About Us and Contact Us pages.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Create a pull request.
