import sys
import json
from haralyzer import HarParser, HarPage
import re

file_path = str(sys.argv[1])
		
with open(file_path, 'r') as f:
	har_text = HarParser(json.loads(f.read()))

data = har_text.har_data
count=0

class my_dictionary(dict):
    def __init__(self):
        self = dict()
          
    def add(self, key, value):
        self[key] = value

process_dict = my_dictionary()

li=[]

def get_post_keys(d):
    for k, v in d.items():
        li.append(k)
        if isinstance(v, dict):
            get_post_keys(v)
        elif isinstance(v,str):
            x = re.search("a*{b*",v)
            if x:
                v = json.loads(v)
                get_post_keys(v)
        elif isinstance(v,list):
            for i in v:
                get_post_keys(i)

query_string=[]
def get_queryString(arr):
	for i in arr:
		query_string.append({"name" : i})

l = len(har_text.har_data["entries"])
keys = range(l)
for i in keys:
	if har_text.har_data["entries"][i]["request"]["method"]=="POST":
		query_sring = []
		for j in data["entries"][i]["request"]["headers"]:
			if(j["name"].lower()=="content-type"):
				if(j["value"].split(';')[0]=="application/json"):
					dt=data["entries"][i]["request"]["postData"]
					get_post_keys(dt)
					get_queryString(li)
					process_dict.add(i,{
					"method" : data["entries"][i]["request"]["method"],
					"url" : data["entries"][i]["request"]["url"],
					"cookies" : data["entries"][i]["request"]["cookies"],
					"queryString" : query_string,
					"headers" : data["entries"][i]["request"]["headers"]
					})
				elif(j["value"].split(';')[0]=="application/x-www-form-urlencoded"):
					process_dict.add(i,{
					"method" : data["entries"][i]["request"]["method"],
					"url" : data["entries"][i]["request"]["url"],
					"cookies" : data["entries"][i]["request"]["cookies"],
					"queryString" : data["entries"][i]["request"]["postData"]["params"],
					"headers" : data["entries"][i]["request"]["headers"]
					})
	else:
		process_dict.add(i,{
			"method" : data["entries"][i]["request"]["method"],
			"url" : data["entries"][i]["request"]["url"],
			"cookies" : data["entries"][i]["request"]["cookies"],
			"queryString" : data["entries"][i]["request"]["queryString"],
			"headers" : data["entries"][i]["request"]["headers"]
			})


outfile = open("/home/kali/Desktop/whp/intermediate_reports/extracted_data.json", "w")
json.dump(process_dict, outfile, indent = 4)
outfile.close()

print("Completed copyng JSON data to new file")

filename = '/home/kali/Desktop/whp/scripts/prepare_input_for_tool.py'
exec(compile(open(filename, "rb").read(), filename, 'exec'))
