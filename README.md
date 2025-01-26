# URL Shortener

This is a simple URL shortener web application built with Flask. The application takes a long URL as input and generates a shortened URL using the TinyURL service.

## Features
- Accepts any valid HTTPS URL as input.
- Generates a shortened URL.
- Displays both the original and the shortened URL on the same page.

---

## Project Structure
```
url_shortner/
├── main.py                 # The Flask application
├── templates/              # Folder containing HTML templates
│   └── form.html           # HTML template for the user interface
```

---

## Prerequisites
- Python 3.6 or later
- Flask library
- pyshorteners library

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/EmptyAd/URL-Shortener
   cd url_shortner
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install flask pyshorteners
   ```

4. **Run the Application:**
   ```bash
   python main.py
   ```

5. **Access the Application:**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage
1. Open the application in your browser.
2. Enter a valid HTTPS URL in the input box.
3. Click the "Submit" button.
4. View the generated shortened URL below the input form.

---

## File Descriptions

### `main.py`
The core of the application:
- Sets up the Flask application.
- Handles both `GET` and `POST` requests.
- Integrates with TinyURL using the `pyshorteners` library.

### `templates/form.html`
The HTML template for the user interface. Includes:
- A form for inputting the original URL.
- Fields to display the shortened URL and original URL.

---

## Example Output
### Input:
```
https://www.example.com
```

### Output:
```
Shortened URL: https://tinyurl.com/xxxxxxx
```

---
