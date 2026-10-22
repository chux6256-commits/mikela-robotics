from flask import Flask, render_template, request, jsonify
from notify import send_lead_email

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit-form", methods=["POST"])
def submit():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    print(f"Contact from {name} - {email}")
    
    # EMAIL PIPELINE - This sends you email!
    send_lead_email(name, email, message)
    
    return jsonify({"status":"success"})

if __name__ == "__main__":
    app.run(debug=True)