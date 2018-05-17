import os, sys
from threading import Thread
import argparse

class SearchThread(Thread):
	def __init__(self, listfolder, valuesearch, respectallstring):
		Thread.__init__(self)
		self.listfolder = listfolder
		self.valuesearch = valuesearch
		self.respectallstring = respectallstring

	def run(self):
		for currentfolder in self.listfolder:
			if currentfolder == "./data/":
				if not os.path.isfile(currentfolder+"symbols"):
					continue
				currentfile = open(currentfolder+"symbols")
				line = currentfile.readline()
				while line:
					if self.respectallstring == 1:
						if self.valuesearch == line.replace("\n", ""):
							print line
					else:
						if self.valuesearch in line:
							print line
					line = currentfile.readline()
				currentfile.close()
				continue
			for root, dirs, files in os.walk(currentfolder+"/"):
				for file in files:
					with open(os.path.join(root, file), "r") as subdir:
						line = subdir.readline()
						while line:
							if self.respectallstring == 1:
								if self.valuesearch == line.replace("\n", ""):
									print line
							else:
								if self.valuesearch in line:
									print line
							line = subdir.readline()
						subdir.close()

parser = argparse.ArgumentParser()
parser.add_argument("--wildcard", help="Search mail contains your argument")
parser.add_argument("--email", help="Search an email")
parser.add_argument("--thread", help="Number of thread [Default=2]", default=2, type=int)

args = parser.parse_args()

if not os.path.isdir('./data'):
	print "./data folder not found"

if (args.wildcard is None) and (args.email is None):
	print "Error argument: -h for help"
	sys.exit(0)

if args.wildcard != None:
	listfolder = ["./data/"+currentfolder for currentfolder in os.listdir("./data/")]

	listfolder.append("./data/")
	threadnumber = args.thread

	if threadnumber > len(listfolder):
		size = 1
	else:
		size = len(listfolder) / threadnumber

	newlist = [listfolder[i:i+size] for i  in range(0, len(listfolder), size)]
	i = 0
	for current in newlist:
		thread = SearchThread(current, args.wildcard, 0)
		thread.start()
		i += 1
if args.email != None:
	thread = SearchThread(["./data/"+args.email[:1]], args.email, 1)
	thread.start()