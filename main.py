from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url_received = request.form.get("url")
        if not url_received or not url_received.startswith("https://"):
            return render_template("form.html", new_url=None, old_url=None, error="Invalid URL.")
        try:
            short_url = pyshorteners.Shortener().tinyurl.short(url_received)
            return render_template("form.html", new_url=short_url, old_url=url_received)
        except Exception as e:
            return render_template("form.html", new_url=None, old_url=None, error="Error shortening the URL.")
    return render_template("form.html", new_url=None, old_url=None, error=None)

if __name__ == "__main__":
    app.run(debug=True)
