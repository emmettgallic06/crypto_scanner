from flask import Flask,render_template, request, json
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')