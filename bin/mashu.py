#!/usr/bin/env python
import socket
import sys
from colorama import Fore, Style
from urllib.parse import urlparse
import urllib.request
import urllib.error
import urllib.parse
from urllib.request import Request, urlopen
from urllib.error import URLError

momok = urlopen
ngentod = urllib.request.urlopen
negative = '\033[91m'
positive = '\033[32m'
wait = '\033[94m'
final = '\033[93m'

total_scanned_global=0
found_scanned_global=0

if sys.platform == "linux2" or sys.platform == "linux":
        R = ("\033[31m")
        W = ("\033[0;1m")
        B = ("\033[35m")
        G = ("\033[34m")
        glp = ("\033[2m")
        Y = ("\033[33;1m")
else:
        R = ""
        W = ""
        Y = ""
        B = ""
        G = ""
        glp = ""
def OpenLog(log_file_name):
	try:
		f = open(log_file_name, 'r')
		return f.read()
	except IOError:
		return "File" + log_file_name + "does not exist."
print(Fore.GREEN)
print("""
  _                       _ _                 
 | |                     (_|_)                
 | |__   __ _ _ __   __ _ _ _ _ __ ___   __ _ 
 | '_ \ / _` | '_ \ / _` | | | '_ ` _ \ / _` |
 | | | | (_| | | | | (_| | | | | | | | | (_| |
 |_| |_|\__,_|_| |_|\__,_| |_|_| |_| |_|\__,_|
                        _/ |                  
                       |__/                   
                                -Shell finder based on python3
                                -selfinit .word with ur own wordlist                                                        
""")
print(Style.RESET_ALL)
# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
def main():
	socket.setdefaulttimeout(10)

	website_url = input("Abandon all hope\n>> ")
	parse_url=urlparse(website_url)
	log_file_name = "logs/"+parse_url.netloc+".log"
	global total_scanned_global # pylint:disable=global-statement
	global found_scanned_global # pylint:disable=global-statement
	try:
		try:
			open(log_file_name,"w")
		except: # pylint: disable=W0702
			print(negative+"\nInvalid args")
		print(wait+"\nconnection to "+website_url)
		ngentod(website_url)
		print(positive+"Connected")
	except(IOError):
		print("Invalid request")
		exit()
	try:
		dictionary = open("word","r")
	except(IOError):
		print(negative+"Dictionary file not found_scanned_global. Please download the latest dictionary from github link")
		exit()
	keywords = dictionary.readlines()
	for keys in keywords:
		keys=keys.replace("\n","") #To replace newline with empty
		New_URL = website_url+"/"+keys
		print(wait+">> "+New_URL)
		try:
			momok(Request(New_URL))
		except URLError as e:
			if hasattr(e,'reason'):
				print(negative+"404")
				total_scanned_global = total_scanned_global+1
			elif hasattr(e,'code'):
				print(negative+"404 ")
				total_scanned_global = total_scanned_global+1
		else:
			try:
				log_file=open(log_file_name,"+a") #Appending to it
			except(IOError):
				print(negative+"Invalid args")
			found_scanned_url=New_URL
			print(positive+"Possible found at ",found_scanned_url)
			log_file.writelines(found_scanned_url+"\n")
			found_scanned_global=found_scanned_global+1
			total_scanned_global=total_scanned_global+1
			log_file.close()
	print("\nTotal tries : ", total_scanned_global)
	print(positive+"\nPossible shells: ",found_scanned_global)
	print(final+"\nFollowing are the links to possible shells ")
	print(OpenLog(log_file_name))

if __name__ == '__main__':
        main()