#!C:\Python37\python.exe

import urllib.request
import urllib.error
import urllib.parse
from colorama import Style
import time
import sys
import os
from pathlib import Path

flag = 0 # a flag to verify if no backdoor was found
print("Abandon all hope, ye who enter here")
print(Style.RESET_ALL)
sap = "-" * 69
################GLOBALS########################
site = [] # initiation of site list
backdoor = [] # initiation of backdoor list
sitelen = '' #initalizing sites count
length = '' # initializing backdoor count
TTD = 0.4 # time delay
###############################################
ngentod = urllib.request.urlopen

path = "../init"

try:
	out = open('res','w')
except IOError:
	print("[Error] Failed to open file!")
	sys.exit("Exiting ...")
def urlFix(url): #Fix URL if http or https is missing
        if "http://" in url or "https://" in url:
                return url

        return "http://" + url
def SiteLists():
	global site # pylint:disable=global-statement
	
	sitelist = input("list init >> ")
	try:
		with open(str(path) + "/" + sitelist) as sites:
			for each in sites:
				grab2 = each.rstrip() # will remove end of line \n
				site.append(grab2)

	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

	except IOError:
		print(("[ Error ]: %s not found" % sitelist))
def BackdoorLists():
	global backdoor # pylint:disable=global-statement
	wordlist = input("word init >> ")
	try:
		with open(str(path) + "/" + wordlist) as adm: # default open is 'r'
			print("[Loading] : Loading backdoor & site list..")
			time.sleep(TTD)

			for backdoors in adm:
				grab = backdoors.rstrip() # will remove end of line \n
				backdoor.append(grab)
	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

	except IOError:
		print(("[Error]        : %s not found" % wordlist))
		sys.exit("Exiting... ")
def ListsValidity():
	global site,backdoor,sitelen,length,out # pylint:disable=global-statement
	tarlength = len(site)
	print(("[Sites] : %d sites loaded.." % tarlength))
	time.sleep(TTD)

	badlength = len(backdoor)
	print(("[Backdoors] : %d backdoor(s) loaded.." % badlength))
	time.sleep(TTD)
	backdoor = list(set(backdoor)) # this will remove duplicates [a set has no duplicates]
	site = list(set(site))

	sitelen = len(site)
	length = len(backdoor)
	print(("[Using Sites] :"), end=' ')
	print(("%d/%d Sites being used (%d duplicates).." % (sitelen, tarlength, tarlength - sitelen)))

	print(("[Using Backdoors] :"), end=' ')
	print(("%d/%d Backdoors being used (%d duplicates).." % (length, badlength, badlength - length)))
	output = '''
BackdoorFinder Results         
Total Sites    =  '''+str(sitelen)+'''
Total Payloads =  '''+str(length)+'''
	'''
	out.write(output)
def bdf(): # pylint:disable=redefined-builtin
	global flag,out # pylint:disable=global-statement
	counter = 0
	if sitelen > 0 and length >0:
		for a in site:
			tar = a
			counter +=1
			try:

				url = urlFix(tar)
				ua = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
				header = {'User-Agent' : ua}

				req = urllib.request.Request(url, None, header)
				resp = ngentod(req)

				out1 = "[Connecting] : %s..." % url
				print(out1)
				out.write("\n" + sap + "\n" + out1 + "\n")
				if resp.code == 200:
					time.sleep(TTD)
					out2 = "[Connected]  : %s is connected" % url
					print(out2)
					out.write(out2 + "\n")
					time.sleep(TTD)
					out3 = "[Checking %d/%d] : Checking %s \n" %(counter, sitelen, url)
					print(out3)
					out.write(out3 + "\n")

			except KeyboardInterrupt:
				sys.exit("\n[User Interrupt] : Exiting .. ")


			try:
				for x in backdoor:
					x = "/" + x
					payload = url + x
					try:
						#correction of duplication of http or https
						payload = payload.replace("//", "/")
						payload = payload.replace("http:/", "http://")
						payload = payload.replace("https:/", "https://")

						plreq = urllib.request.Request(payload, None, header)
						plresp = ngentod(plreq)

						if plresp.code == 200: #show pages with proper response
							flag = 1
							out6 = "[OK] : %s" % payload
							print(out6)
							out.write(out6 + "\n")

						elif plresp.code == 302: #show redirected pages
							flag = 1
							out7 = "[FOUND] : %s" % payload
							print(out7)
							out.write(out7 + "\n")

						elif plresp.code == 403: #show forbbiden pages
							flag = 1
							out8 = "[FORBBIDEN] : %s" % payload
							print(out8)
							out.write(out8 + "\n")


					except KeyboardInterrupt:
						sys.exit("\n[User Interrupt] : Exiting.. ")

					except IOError:
						continue
				if not flag:
					out9 = "[NO BACKDOOR] : No Backdoor Found.. "
					print(out9)
					out.write(out9)
				else:
					pass



			except KeyboardInterrupt:
				sys.exit("\n[User Interrupt] : Exiting.. ")
def Main():
	SiteLists()
	BackdoorLists()
	ListsValidity()
	bdf()
	out.close()
	print("[Done] : Results are saved into /bin/res")
if __name__ == "__main__":
	Main()

hooks = "bash ch.bash"
hook = "cat res | grep OK > tempres200 | tr -d '\r' < a.bash > aout.bash | bash aout.bash"
rem = "rm aout.bash"
os.system(hooks) # nosec
os.system(hook) # nosec
os.system(rem) # nosec