from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Use host='0.0.0.0' to make it accessible on local network
    app.run(host='0.0.0.0', port=5000, debug=True)
