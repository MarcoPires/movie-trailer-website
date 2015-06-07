import json
import urllib

def load(path, local):
	#working the method how to access the data
	if local == 'true':
		#local
		movies_file = open(path)
	else:
		#external API
		movies_file = urllib.urlopen(path)
	#read file
	json_data   = movies_file.read();
	#json parse
	python_obj  = json.loads(json_data);
	#close file
	movies_file.close();
	#return object
	return python_obj;