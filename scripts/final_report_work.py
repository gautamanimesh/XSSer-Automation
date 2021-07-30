import os
import json

file_name = "/home/kali/Desktop/whp/intermediate_reports/compiled_report.json"

with open(file_name) as inp:
	data = json.load(inp)

trial=[]

class report_dict(dict):
	def __init__(self):
		self = dict()
		  
	def add(self, key, value):
		self[key] = value

new_dic = report_dict()

new_dict=[]
for i in range(len(data)):
	new_dict.append(data[str(i)])

unique_list = {}

def unique(list1):
	for val in list1:
		key=(val["url"],val["vector"])
		if unique_list.get(key):
			unique_list[key]["payload"].add(val["payload"])
		else:
			obj={"method":val["method"],"headers":val["headers"],"payload":set([val["payload"]])}
			unique_list[key]=obj

unique(new_dict)

z = []
for i,v in unique_list.items():
	z.append({"url" : i[0], "vector" : i[1], "method" : v["method"], "headers" : v["headers"],"payload" : list(v["payload"])})


outfile = open("/home/kali/Desktop/whp/final_report.json", "w")
json.dump(z, outfile, indent = 4)
outfile.close()

print("Congratulations! Final report created. :)")