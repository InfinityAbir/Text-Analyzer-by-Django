# Text-Analyzer-by-Django (Text Utils)

**Text Utils** is a simple yet effective Django web application designed to analyze and manipulate text inputs. Users can perform common operations like stripping punctuation, converting case, and cleaning up new lines through a clean, responsive interface powered by Bootstrap.

---

## ✨ Features

* **Remove Punctuation:** Strip all common punctuation marks from your text.
* **Convert to Uppercase:** Transform the text into all capital letters.
* **Remove New Lines:** Merge your text into a single block by removing newline characters.
* **Word Count:** Count the number of words in the text.
* **Estimated Reading Time:** Approximate the time it will take to read the text.
* **Keyword Density:** Identify the top keywords and their frequency, ignoring common stopwords.
* **Text Summary:** Generate a short summary of the input text.
* **Sentiment Analysis:** Detect the overall sentiment as Positive, Negative, or Neutral.
* **Responsive Design:** Works well on desktop and mobile devices using **Bootstrap 5**.
* **Simple Navigation:** Includes a basic navbar for Home, GitHub, and Contact links.

---

## 🛠️ Technologies Used

| Category | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | **Django** | Python-based web framework for robust server-side development. |
| **Language** | **Python** | The core programming language driving the application logic. |
| **Frontend** | **Bootstrap 5** | CSS framework used for responsive, pre-styled UI components. |
| **Markup/Style** | **HTML/CSS** | Standard technologies for structuring and styling the web pages. |

---

## 🚀 Installation

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8+
- pip
- Virtual environment tool such as `venv`

---

### Install and run

    ```bash
# 1) Clone the repository
    git clone https://github.com/InfinityAbir/Text-Analyzer-by-Django.git
    cd Text-Analyzer-by-Django

# 2) Create virtual environment
    python -m venv venv

# 3) Activate the virtual environment
# Linux / macOS:
    source venv/bin/activate
# Windows:
    venv\Scripts\activate

# 4) Install required packages
# If requirements.txt exists:
    pip install -r requirements.txt

# If requirements.txt is not available, run:
    pip install django textblob

# 5) Download TextBlob data (required for sentiment analysis)
    python -m textblob.download_corpora

# 6) Run the development server
    python manage.py runserver

# Open in your browser:
    http://127.0.0.1:8000

---

# Text-Analyzer-by-Django (Text Utils)

**Text Utils** is a simple yet effective Django web application designed to analyze and manipulate text inputs. Users can perform common operations like stripping punctuation, converting case, and cleaning up new lines through a clean, responsive interface powered by Bootstrap.

---

## ✨ Features

* **Remove Punctuation:** Easily strip all common punctuation marks from the text.
* **Convert to Uppercase:** Transform the entire input text to all capital letters.
* **Remove New Lines:** Eliminate newline characters (`\n`) to merge the text into a single block.
* **Responsive Design:** Built with **Bootstrap 5** for seamless viewing on desktop and mobile devices.
* **Simple Navigation:** Includes a basic navbar with placeholders for Home, About Us, and Contact Us pages.

---

## 🛠️ Technologies Used

| Category | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | **Django** | Python-based web framework for robust server-side development. |
| **Language** | **Python** | The core programming language driving the application logic. |
| **Frontend** | **Bootstrap 5** | CSS framework used for responsive, pre-styled UI components. |
| **Markup/Style** | **HTML/CSS** | Standard technologies for structuring and styling the web pages. |

---

## 🚀 Installation

Follow these steps to set up and run the project locally.

### Prerequisites

* **Python 3.8+**
* **pip** (Python package manager)
* **Virtualenv** (Highly recommended for dependency isolation)

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/InfinityAbir/Text-Analyzer-by-Django](https://github.com/InfinityAbir/Text-Analyzer-by-Django)
    cd text-utils
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    # For Linux/macOS
    source venv/bin/activate
    # For Windows
    # venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install django
    ```

4.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

5.  **Access the Application:**
    Open your browser and navigate to: **`http://127.0.0.1:8000`**
---

## 📝 Usage

1.  Open the application's homepage (`/`).
2.  Enter your desired text into the **textarea**.
3.  Select one or more manipulation options (e.g., **Remove Punctuation**, **Uppercase**).
4.  Click the **"Analyze Text"** button.
5.  The processed output will be displayed on the result page.

---

## 🔮 Future Improvements

We plan to enhance Text Utils with the following features:

* **Expanded Toolset:** Adding more text analysis options (e.g., word count, character count, lowercase conversion).
* **User Authentication:** Implementing personalized features requiring user login.
* **UI/UX Refinement:** Enhancing the design with custom CSS and advanced Bootstrap components.
* **Content Pages:** Completing the functional **About Us** and **Contact Us** pages.

---

## 🤝 Contributing

We welcome contributions to Text Utils! To contribute:

1.  **Fork** the repository.
2.  Create a new feature branch: `git checkout -b feature-branch`.
3.  Commit your changes: `git commit -m "Add descriptive feature name"`.
4.  Push to the branch: `git push origin feature-branch`.
5.  Open a **Pull Request**.
