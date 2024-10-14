import sys
import time

try:
    from googlesearch import search
except ImportError: 
	print("googlesearch-python module does not seem to be installed.")
	print("Try 'pip install googlesearch-python', then re-execute the script.")

# Defining colors used in the script
class colors:
	HEADER = '\033[94m'
	SUBHEADER = '\033[0;95m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m' 
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'

# Banner printing
def banner():
	"""
	- when called, banner() prints the banner in the terminal.
	
	- return : does not return anything, it only prints the banner.
	"""

	print(colors.HEADER  + """
╔─────────────────────────────────────────────────────────────╗
│        ___         __         ___              __           │
│       / _ | __ __ / /_ ___   / _ \\ ___   ____ / /__ ___     │
│      / __ |/ // // __// _ \\ / // // _ \\ / __//  '_/(_-<     │
│     /_/ |_|\\_,_/ \\__/ \\___//____/ \\___//_/  /_/\\_\\/___/     │
╚─────────────────────────────────────────────────────────────╝
""" + colors.ENDC)
	print(colors.SUBHEADER + "Autodorks - Automating Google Dorks")
	print(colors.OKGREEN + "Author: " + colors.WARNING + "K1ng-Ph1sh3r | " + colors.OKGREEN + "Repo : " + colors.WARNING + "[Github_repo]\n" + colors.ENDC)

def getUrls(dork,number_webs,filename):
	"""
	- getUrl first finds the google dork, the number of results wanted, the name of the output file (defined in the main function), then starts the Google dorks, and writes the results in the terminal and the specified file.
	
	- dork : variable that contains the Google Dork
	- number_webs : variable that contains the number of results that we want (For istance, if N = 4, AUtodorks will return only the 4 first results of the dorks).
	- filename : The name of the file inwhich the Google Dorks' result will be sent.
	
	- return : Does not return anything, it only prints results in the terminal, and the specified file
	"""
	# Printing the launch of Autodorks
	pages = 0
	results = ""

	print(colors.OKCYAN + "Starting Autodorks with the following Google Dorks : ")
	print(colors.FAIL + dork + colors.ENDC)
	print("")

	# Printing results in the terminal and writing them in the specified file
	file = open(filename, "w")

	print("Résultats :")
	for results in search(dork):
		print (results)
		file.write(str(results))
		file.write("\n")
		time.sleep(0.2)
		
		pages += 1
			
		if pages >= number_webs:
			break
		
	if results == "":
		print("")
		print("No results for current Dorks")
		file.write("No results for current Dorks")
	file.close()	
				

def main():
	"""
	- main is the principal function, it defines script's arguments, which file should be used to write results, and in some cases, the choice of the Google dorks (depending on the argument given to script)

	- return : Does not return anything, it only initialize the script.
	"""
	# Printing the banner (ASCII art name)
	banner()
	
	# Defining arguments
	if len(sys.argv) == 2:
		arg = sys.argv[1]
		
		# Help section
		if arg == "-h" or arg == "--help" :
			print (colors.BOLD + "HELP SECTION:" + colors.ENDC)
			print ("Usage :" + colors.OKCYAN + '\t \tautodorks.py -d [Google dork] [Number_of_sites]' + colors.ENDC)
			print ("Example :" + colors.OKCYAN + '\t> autodorks.py -d "inurl:example" 5' + colors.ENDC)
			print(colors.OKCYAN + '\t \t> autodorks.py FTG-01 -w "google.com" 5' + colors.ENDC)
			print("")
			print ("-d,--dork" + colors.OKCYAN + "\tSpecify the google dorks wanted" + colors.ENDC)
			print ("-w,--website" + colors.OKCYAN + '\tSpecify the domain name of the website that you want to use the Google Dorks on (for instance, "youtube", or "twitch")' + colors.ENDC)
			print ("-l,--list" + colors.OKCYAN + "\tprint the list of all configured Google dorks in the script" + colors.ENDC)
			print ("-h,--help" + colors.OKCYAN + "\tThis help" + colors.ENDC)
			print ("-v,--version" + colors.OKCYAN + "\tSee version (for testing process)" + colors.ENDC)
			print("")
			print(colors.BOLD + "You can have more informations by visiting Autodorks' repo :" + colors.ENDC)
			print(colors.WARNING + "[Github_repo]" + colors.ENDC)
		# Version section
		elif arg == "-v" or arg == "--version":
			print (colors.WARNING + "Autodorks v.1 - It seems that the script runs ! You can now run your dorks :D" + colors.ENDC)
		# List section
		elif arg == "-l" or arg == "--list":
			print (colors.WARNING + "List of configured Google Dorks :" + colors.ENDC)
			print ("- FTPG-01" + colors.OKCYAN + '\tVerifies every FTP shares accessible from the specified website on Google.' + colors.ENDC)
			print ("- FTPG-02" + colors.OKCYAN + '\tVerifies every FTP share accessible that contains the name of the specified compagny.' + colors.ENDC)
			print ("- GGLD-01" + colors.OKCYAN + "\tLooks for the website's name in a lot of different temporary text storage websites (pastebin, codepad...)." + colors.ENDC)
			print ("- GGLD-02" + colors.OKCYAN + "\tLooks for several types of files accessible (.pdf, .pptx, .csv, .log, .conf...), from Google." + colors.ENDC)
			print ("- GGLD-03" + colors.OKCYAN + "\tLooks if it is possible to  l'arborescence des fichiers dans tous les domaines appartenant à RENATER." + colors.ENDC)
		# Fail section
		else:
			print (colors.FAIL + "ERROR : Argument or incorrect syntaxis." + colors.ENDC)
			
	elif len(sys.argv) > 1 and len(sys.argv) <= 7:
		# Custom Google dorks 
		if sys.argv[1] == "-d" or sys.argv[1] == "--dork":
			dork = sys.argv[2]
			number_webs = int(sys.argv[3])
			filename = "Custom_GGLD.txt"
			getUrls(dork,number_webs,filename)

		# Google dorks FTPG-01
		elif sys.argv[1] == "FTPG-01":
			website = sys.argv[3]
			number_webs = int(sys.argv[4])
			filename = "FTPG-01.txt"
			dork = str("inurl:ftp -inurl:http -inurl:https inurl:"+ website)
			getUrls(dork,number_webs,filename)

		# Google dorks FTPG-02
		elif sys.argv[1] == "FTPG-02":
			website = sys.argv[3]
			number_webs = int(sys.argv[4])
			filename = "FTPG-02.txt"
			dork = str('inurl:ftp -inurl:http -inurl:https "' + website + '"')
			getUrls(dork,number_webs,filename)

		# Google dorks GGLD-01
		elif sys.argv[1] == "GGLD-01":
			website = sys.argv[3]
			number_webs = int(sys.argv[4])
			filename = "GGLD-01.txt"
			dork = str('site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com "'+ website + '"')
			getUrls(dork,number_webs,filename)

		# Google dorks GGLD-02
		elif sys.argv[1] == "GGLD-02":
			website = sys.argv[3]
			number_webs = int(sys.argv[4])
			filename = "GGLD-02.txt"
			dork = str('site:*.'+ website +' site:' + website +' ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:log | ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env | ext:sql | ext:dbf | ext:mdb')
			getUrls(dork,number_webs,filename)

		# Google dorks GGLD-03
		elif sys.argv[1] == "GGLD-03":
			website = sys.argv[3]
			number_webs = int(sys.argv[4])
			filename = "GGLD-03.txt"
			dork = str('site:*.'+ website +' intitle:index.of')
			getUrls(dork,number_webs,filename)

# Starting the main() function
main()