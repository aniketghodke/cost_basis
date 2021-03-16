import os
import json

class Util:
	def __init__(self):
		pass
	
	def validate_input(self, data):
		data_valid = True
		if not isinstance(data, list):
			print('3')
			return False
		for d in data:
			if "stock" in d and "cost" in d and "operation" in d:
				continue
			else:
				print("data invalid for {}".format(d))
				data_valid = False
		return data_valid
	
	def update_file(self, tracker_file, data):
		json_data = {}
		if os.path.exists(tracker_file):
			with open(tracker_file) as fp:
				json_data = json.load(fp)
		for d in data:
			stock_name = d['stock']
			if stock_name in json_data:
				if d['operation'].lower() == 'buy':
					json_data[stock_name] = json_data[stock_name] + float(d['cost'])
				if d['operation'].lower() == 'sell':
					json_data[stock_name] = json_data[stock_name] - float(d['cost'])
			else:
				# new stock found
				json_data[stock_name] = float(d['cost'])
		with open(tracker_file, 'w') as fp:
			json.dump(json_data, fp, indent=4)
			
	def get_price(self, tracker_file, stock):
		if os.path_exists(tracker_file):
			with open(tracker_file) as fp:
				json_data = json.load(fp)
		return json_data[stock]
			
		
		
					
					
		
		
		
