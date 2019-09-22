from flask import Flask, request, jsonify, render_template
from truthtable import *

app = Flask(__name__)
app.url_map.converters['list'] = ListConverter

@app.route('/result', methods=['GET','POST'])
def print_table():

	inputs = request.form.get("strs").split(",")
	if not inputs or len(inputs) == 0:
		return "input is empty!"
	#inputs = request.get("strs").split(",")
	return render_template("formResult.html", x = (print_multi_truth_table_results(inputs)))

