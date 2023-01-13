from flask import Flask,render_template, request,json,flash,redirect,url_for
app =Flask(__name__)
messages = [{'contract': 'Message One'}
            ]
@app.route("/find", methods =('GET','POST'))
def find():
    if request.method == 'POST':
        contract = request.form['contract']
        startdate = request.form['start']
        enddate = request.form['end']
        time = request.form['time']
        timestamp = request.form['timestamp']
        amount = request.form['Amount']
        if not contract:
            flash('Contract is required')
        else:
            messages.append({'contract': contract})
            return redirect(url_for('index'))

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)