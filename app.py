from flask import Flask, render_template, url_for, json, jsonify, Response, abort
from flask_cors import CORS
from models.employee import *

app = Flask(__name__)
CORS(app)

my_employee = employee()

# Landing page
@app.route("/")
def getSomeData():
    r = my_employee.globalData
    return Response(json.dumps(r), mimetype='application/json')

# Returns JSON of all employees
@app.route("/api/employee/")
def api_employee_list():
    return jsonify(my_employee.toJSON())

# Returns JSON of an employee based on their ID
@app.route('/api/employee/<int:index>')
def api_employee_detail(index):
    try:
        return my_employee[index]
    except IndexError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
