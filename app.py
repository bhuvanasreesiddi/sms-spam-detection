from flask import Flask, render_template, request

app = Flask(__name__)

# Simple spam detection logic (no ML for now)
def predict_spam(message):
    spam_words = ["win", "free", "offer", "click", "buy now", "urgent", "lottery"]
    message = message.lower()

    for word in spam_words:
        if word in message:
            return "🚨 Spam Message"

    return "✅ Not Spam"


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        message = request.form["message"]
        prediction = predict_spam(message)

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
