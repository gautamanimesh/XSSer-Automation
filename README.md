XSSer
Cross Site "Scripter" (aka XSSer) is an automatic -framework- to detect, exploit and report XSS vulnerabilities in web-based applications.
It provides several options to try to bypass certain filters and various special techniques for code injection.
XSSer has pre-installed [ > 1300 XSS ] attacking vectors and can bypass-exploit code on several browsers/WAFs.
XSSer runs on many platforms. It requires Python (3.x) and has many libraries.
Check out: https://github.com/epsylon/xsser

On Debian-based systems (ex: Ubuntu), run:
sudo apt-get install python3-pycurl python3-bs4 python3-geoip python3-gi python3-cairocffi python3-selenium firefoxdriver

On other systems such as: Kali, Ubuntu, ArchLinux, ParrotSec, Fedora, etc... also run:
sudo pip3 install pycurl bs4 pygeoip gobject cairocffi selenium
 
 
Automation Explanation:
Earlier, what we had to do was: we had to prepare our own input string each time we needed to perform vulnerability testing on any url (Uniform Resource Locator). 
This was a tedious job.
We needed to analyse the HAR file first.
Then we needed to search for the attack vectors and the sorts of payloads we wanted to test for.
This required us to have sufficient knowledge in the cyber security domain.
Also it was a time taking process.
What does our automation help with?
In layman terms, it basically prepares the input string that can be fed to XSSer.
Due to automation, all the required input strings will be prepared using some python scripts and fed to XSSer directly in the CLI (Command Line Interface).
This would help us save time and also the extra hard-work that we used to put in earlier.
The basic requirement for this automation is a HAR file (.har).
Check out: Generating a .HAR File on Chrome Browser
These can be easily exported from the Developer Options Tab present in Google Chrome or any other browser.
 
What is a HAR file (.har) ?
HAR, short for HTTP Archive, is a format used for tracking information between a web browser and a website. 
A HAR file is primarily used for identifying performance issues, such as bottlenecks and slow load times, and page rendering problems. 
The HAR file keeps track of each resource loaded by the browser along with timing information for each resource.
 
Installation: Tool + Automation Part
Pre-requisites:
First of all, you need to install XSSer in your Virtual Machine. (However in Kali Linux, XSSer comes pre-installed.)
Check out: https://github.com/epsylon/xsser
Now download the whp.zip file from 
https://github.com/Shashank2808/XSSer-Automation
In CLI, install haralyzer package after cloning from 
GitHub: https://github.com/haralyzer/haralyzer.git
Use command in CLI:
git clone https://github.com/haralyzer/haralyzer.git
Also visit: https://pypi.org/project/haralyzer/ for help!

After steps 1, 2 and 3 now  extract the [whp folder] from the whp.zip file.
Open the python files present in the extracted whp folder.
In all the python files, change the path of the required files to your desired path wherever needed. (Note: Paths that are pre-written in the code won’t work for you.) [Compulsory]
Change all the paths accordingly and Save the changes.
Once you are done with this, all you require is a HAR file (.har) and a starting input string.
 
Example (Starting input String) : 
python3 /home/kali/Desktop/whp/scripts/taking_input.py /home/kali/Downloads/y1.har
This command needs to be entered in the CLI with the modifications mentioned below.
Here if we break down the command, we have, 
python3 /home/kali/Desktop/whp/scripts/taking_input.py
This is the command to run the taking_input.py script.
Here, change the path for the [taking_input.py file] to the path where this file is located in your VM.
/home/kali/Downloads/y1.har
This is the file path for the HAR file.
In this place, provide the path for your HAR file.
 
That’s it. Now all the python files will run one by one automatically as they are interlinked.
After all the scripts have finished running, an input string will be provided to XSSer directly from the python file (command_to_tool.py) which is responsible for providing input to XSSer.
Once XSSer gets its input, it’ll start scanning. It will use around 1300+ different payloads for vulnerability testing. (this takes time).
Some intermediate files will also be created in the process, these are:
extracted_data.json
temporary_list.json
list_of_commands.txt
compiler_report.json
And some pen-ultimate Report.xml files in a results folder.
After XSSer completes it’s scan, the final report will be available in (final_report.json file) which will be at the location you mentioned in the (final_report_work.py file).
The final report will consist of all the information that XSSer gathered while scanning.
 
Conclusion:
The final report will consist of the [url, vectors(attack locations), method(GET/POST), headers, and payloads that were successfully injected by XSSer] in a proper well defined url and vector-wise manner. 
Since we wanted to completely automate the tool, we got rid of the menu-driven aspect as it was unnecessarily tedious.
After automation, we need to feed the CLI with just one input string to initialize our python script and the location of the HAR file (.har).
Because of the automation, we will be able to save a lot of time apart from the time XSSer takes to completely scan a url.
