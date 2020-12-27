# Laptop Service
import os
import pymongo
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

# Instantiate the app
app = Flask(__name__)
api = Api(app)
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
#client = MongoClient('172.18.0.2', 27017)
db = client.tododb
db.tododb.delete_many({})

class Laptop(Resource):
    def get(self):
        return {
            'Laptops': ['Mac OS', 'Dell', 
            'Windozzee',
	    'Yet another laptop!',
	    'Yet yet another laptop!'
            ]
        }

class listAll(Resource):
	def get(self):
		datalist = []
		ot=[]
		ct=[]
		data = db.tododb.find()

		for datum in data:
			datalist.append(datum)
		for datum in datalist:
			ot.append(datum['open_data'])
			ct.append(datum['close_data'])

		ret = {
		        'open_time': ot,
		        'close_time': ct,
		}
		app.logger.debug("PRINTING")
		app.logger.debug("data={}".format(data))

		return ret

class listAllCSV(Resource):
	def get(self):
		data = db.tododb.find()
		csv = ""
		app.logger.debug("PRINTING1")
		app.logger.debug("data={}".format(data))
		for datum in data:
			csv += datum['open_data'] + ", " + datum['close_data'] + ", "
		return csv

class listAllJSON(Resource):
	def get(self):
		datalist = []
		ot=[]
		ct=[]
		data = db.tododb.find()

		for datum in data:
			datalist.append(datum)
		for datum in datalist:
			ot.append(datum['open_data'])
			ct.append(datum['close_data'])

		ret = {
		        'open_time': ot,
		        'close_time': ct,
		}

		return ret

class listOpenOnly(Resource):
	def get(self):
		datalist = []
		ot=[]

		for datum in data:
			datalist.append(datum)
		for datum in datalist:
			ot.append(datum['open_data'])

		ret = {
		        'open_time': ot,
		}
		return ret

class listCloseOnly(Resource):
	def get(self):
		datalist = []
		ct=[]

		for datum in data:
			datalist.append(datum)
		for datum in datalist:
			ct.append(datum['close_data'])

		ret = {
		        'close_time': ct,
		}
		return ret

class listOpenOnlyCSV(Resource):
	def get(self):
		top = request.args.get("top", type = int)
		if not top:
			data = db.tododb.find().sort("open_data", pymongo.ASCENDING).limit(len("open_data"))
		else:
			data = db.tododb.find().sort("open_data", pymongo.ASCENDING).limit(top)
		csv = ""

		for datum in data:
			csv += datum['open_data'] + ", "
		return csv

class listCloseOnlyCSV(Resource):
	def get(self):
		top = request.args.get("top", type = int)
		if not top:
			data = db.tododb.find().sort("close_data", pymongo.ASCENDING).limit(len("close_data"))
		else:
			data = db.tododb.find().sort("close_data", pymongo.ASCENDING).limit(top)
		csv = ""

		for datum in data:
			csv += datum['close_data'] + ", "
		return csv

class listOpenOnlyJSON(Resource):
	def get(self):
		top = request.args.get("top", type = int)
		if not top:
			data = db.tododb.find().sort("open_data", pymongo.ASCENDING).limit(len("open_data"))
		else:
			data = db.tododb.find().sort("open_data", pymongo.ASCENDING).limit(top)

		datalist = []
		ot=[]

		for datum in data:
			datalist.append(datum)
		for datum in datalist:
			ot.append(datum['open_data'])

		ret = {
		        'open_time': ot,
		}
		return ret

class listCloseOnlyJSON(Resource):
	def get(self):
		top = request.args.get("top", type = int)
		if not top:
			data = db.tododb.find().sort("close_data", pymongo.ASCENDING).limit(len("close_data"))
		else:
			data = db.tododb.find().sort("close_data", pymongo.ASCENDING).limit(top)

		datalist = []
		ct=[]

		for datum in data:
			datalist.append(datum)
		for datum in datalist:
			ct.append(datum['close_data'])

		ret = {
		        'close_time': ct,
		}
		return ret

# Create routes
# Another way, without decorators
api.add_resource(listAll, '/listAll')
api.add_resource(listAllCSV, '/listAll/csv')
api.add_resource(listAllJSON, '/listAll/json')
api.add_resource(listOpenOnly, '/listOpenOnly')
api.add_resource(listOpenOnlyCSV, '/listOpenOnly/csv')
api.add_resource(listOpenOnlyJSON, '/listOpenOnly/json')
api.add_resource(listCloseOnly, '/listCloseOnly')
api.add_resource(listCloseOnlyCSV, '/listCloseOnly/csv')
api.add_resource(listCloseOnlyJSON, '/listCloseOnly/json')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
