import json

def load_file(file):
	f = open(file, 'r')
	return json.load(f)
