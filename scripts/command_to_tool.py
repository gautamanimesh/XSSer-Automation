import subprocess
import os,os.path
args = []

file_path = "/home/kali/Desktop/whp/results/"
for i in os.listdir(file_path):
    os.remove(file_path+i)

with open('/home/kali/Desktop/whp/intermediate_reports/list_of_commands.txt', 'r') as file_reader:
    filecontents = file_reader.readlines()
    for line in filecontents:
        current_arg = line[:-1]
        args.append(current_arg)
        
print(args)
for i in args:
    p1 = subprocess.Popen(i, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines = True)
    out, err = p1.communicate()
    print("output: ", format(out))
    print("error: ", format(err))
    #print(p1.stdout.read())
    #p1.stdout.close()
    if p1.returncode == 0:
        print("Command : success")
    else:
        print("Command : failed")

print("Ran all the commands")

filename = '/home/kali/Desktop/whp/scripts/report_work.py'
exec(compile(open(filename, "rb").read(), filename, 'exec'))

