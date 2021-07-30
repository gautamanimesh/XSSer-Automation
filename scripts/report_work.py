import xml.etree.ElementTree as ET
import json
import os, os.path
from ast import literal_eval

file_path = "/home/kali/Desktop/whp/results/"

data = []

with open("/home/kali/Desktop/whp/intermediate_reports/list_of_commands.txt") as inp:
	data = inp.read().splitlines()
length_of_dir = len([name for name in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, name))])


info = []
with open('/home/kali/Desktop/whp/intermediate_reports/temporary_list.json') as f:
  info = json.load(f)


class report_dict(dict):
    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key] = value

new_dict = report_dict()
count = 0
count1 = 0
for i in os.listdir(file_path):
	XML_tree = ET.parse(file_path+i)
	root = XML_tree.getroot()
	if root[1][0][0].text==root[1][0][1].text:
		print(root[1][0][0].text)
	else:
		for k in root[2]:
			data1 = data[count1].split()
			url = data1[2]
			url = r"{}".format(url).strip("\"")
			method = data1[3]
			if method=="-g":
				method = "GET"
			elif method=="-p":
				method = "POST"
			new_dict.add(count,{
				"payload" : k[0].text,
				"vulnerable" : k[1].text,
				"vector" : k[2].text,
				"url" : url,
				"method" : info[count1]["additional_info"]["method"],
				"headers" : info[count1]["additional_info"]["headers"]
				})
			count = count + 1
	count1 = count1 + 1

outfile = open("/home/kali/Desktop/whp/intermediate_reports/compiled_report.json", "w")
json.dump(new_dict, outfile, indent = 4)
outfile.close()

filename = '/home/kali/Desktop/whp/scripts/final_report_work.py'
exec(compile(open(filename, "rb").read(), filename, 'exec'))
