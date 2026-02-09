from flask import Flask, render_template, request
from logic.calculator import calculate
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")

        try:
            result = calculate(float(num1), float(num2), operation)
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":      
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
