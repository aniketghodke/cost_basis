import json
import os
from flask import Flask, request
from utils.util import Util

app = Flask(__name__)

output_file = 'current_cost_basis.json'

@app.route("/about")
def about():
	print("this is a small service for keep track of cost basis")
	return True
	
@app.route("/update", methods=["POST"])
def update():
	u = Util()
	print("Uptating cost basis")
	print(request.json)
	data = request.json
	print(data)
	if not u.validate_input(data['data']):
		raise AssertionError("Invalid Data")
	print("data valid")
	u.update_file(output_file, data['data'])
	return {'Updated'}

@app.route("/getcostbasis", methods=["GET"])
def getcostBasis():
	symbol = request.args.get('stock')
	with open(output_file) as fp:
		json_data = json.load(fp)
	if symbol in json_data:
		return json_data['stock']
	return {'No data found for {}'.format(symbol)}


if __name__=="__main__":
	app.run()
	#dt = '{"data":[{"stock":"cciv","operation":"BUY","cost":"42.00"}]}'
	#update(dt)
	#getcostBasis('CCIV')
