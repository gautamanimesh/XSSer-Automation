import json

with open('/home/kali/Desktop/whp/intermediate_reports/extracted_data.json') as f:
  data = json.load(f)

final_list = []

def prepare_query(queries):
	new_str = ""
	for i in queries:
		new_str = new_str + i["name"] + "=XSS&"
	if len(new_str)>0:
		new_str = new_str[0:len(new_str)-1:1]
	return new_str

def prepare_cookie(queries):
	new_str = ""
	for i in queries:
		new_str = new_str + i["name"] +"=" + i["value"]+";"
	if len(new_str)>0:
		new_str = new_str[0:len(new_str)-1:1]
	return new_str


temp_list=[]
count=0
for k,v in data.items():
	str1 = "xsser -u "
	url = v["url"].split('?')[0]
	ip_parameters = prepare_query(v["queryString"])
	cookie = prepare_cookie(v["cookies"])
	if v["queryString"]:
		if v["method"]=="GET":
			ip_parameters = "?" + ip_parameters
			#print(str, "hello1", ip_parameters, len(ip_parameters))
			str1 = str1 + "\""+ url + "\" -g \""+ ip_parameters +"\""
		elif v["method"] == "POST":
			str1 = str1 + "\""+ url + "\" -p \""+ ip_parameters +"\""
		if v["cookies"]:
			str1 = str1 + " --cookie \"" + cookie + "\""
		str1 = str1 + " --auto --xml \"/home/kali/Desktop/whp/results/Report"+str(count)+".xml\""
		final_list.append(str1)
		temp_list.append({"derived_command" : str1,"additional_info" : v})
		count = count + 1

print("Printing final array: ")
for i in final_list:
	print(i, "\n\n")


with open('/home/kali/Desktop/whp/intermediate_reports/list_of_commands.txt', 'w') as file_writer:
    file_writer.writelines("%s\n" % i for i in final_list)

outfile = open('/home/kali/Desktop/whp/intermediate_reports/temporary_list.json', "w")
json.dump(temp_list, outfile, indent = 4)
outfile.close()

filename = '/home/kali/Desktop/whp/scripts/command_to_tool.py'
exec(compile(open(filename, "rb").read(), filename, 'exec'))