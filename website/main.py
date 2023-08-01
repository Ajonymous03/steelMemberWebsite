from flask import Flask, render_template, request
from aisc import wide_flange_database

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])

def calculations():
    member_list = []

    for member in wide_flange_database:
        member_list.append(member)

    return render_template('base.html', member_list = member_list)

if __name__ == '__main__':
    app.run(debug=True)
