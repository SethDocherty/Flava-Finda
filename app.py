from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# To run app, in terminal type:
# set FLASK_APP=app.py
# set FLASK_ENV=development
# flask run