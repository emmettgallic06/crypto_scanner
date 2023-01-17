from flask import Flask, render_template, request, url_for, flash, redirect
import scan2
app =Flask(__name__)
app.config['SECRET KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'
messages = [{'contract': 'Message One'}]
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

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)