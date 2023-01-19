from flask import Flask, render_template, request, url_for, flash, redirect
import scan2
from datetime import datetime
import api_function

app =Flask(__name__)
app.config['SECRET KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'
messages = [{'contract': 'Message One'}]
def date_format(date):
    result = datetime.strptime(date, '%Y-%m-%dT%H:%M')
    return result

@app.route("/find", methods =('GET','POST'))
def find():
    if request.method == 'POST':
        contract = request.form.get('contract')
        if not contract:
            flash('Contract is required')
        else:
            messages.append({'contract': contract})
        return scan2.get_hash_time(contract)
    return render_template('find.html')
@app.route("/accounts", methods =('GET','POST'))
def accounts():
    return render_template('accounts.html')

@app.route("/", methods = ('GET','POST'))
def main():
    if request.method == 'POST':
        contract = request.form.get('contract')
        start = request.form.get('start')
        end = request.form.get('end')
        return api_function.normal_transactions_by_address(contract,start,end)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)