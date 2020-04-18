import sqlite3
import os
import sys
import time

def banner():
	logo = """\033[31;1m
       __  __ ___  ___   _ _ 
      |  \/  |   \| __|_| | |_
      | |\/| | |) |__ \_  .  _|\033[37;1m
      |_|  |_|___/|___/_     _|
     \033[32;1m     BRUTE FORCE   \033[37;1m|_|_|\033[0m
"""
	return logo

def runText(text, waktu):
	for kata in text+"\n":
		print (kata, end="", flush=True)
		time.sleep(waktu)

class md5:
	def __init__(self, hash):
		self.hash = hash
		self.data = []
		self.file = ["data.db", "data1.db", "data2.db"]
		self.found = 0

	def readDB(self):
		print ("\r\033[37;1m[\033[33;1m#\033[37;1m] \033[36;1mWhile reading the database, please wait", end="", flush=True)
		for file in self.file:
			konek = sqlite3.connect("/sdcard/"+file)
			cur = konek.cursor()
			cur.execute("SELECT * FROM wordlist")
#			print )
			for hasil in cur:
				self.data.append(hasil)
		print (" \033[37;1m| \033[32;1mdone")
		time.sleep(3)

	def check(self, pw):
		if self.hash == pw[1]:
			print ("\n\033[32;1m[√] Found: "+str(pw[2])+"\033[0m")
			self.found += 1
		else:
			pass

	def crack(self):
#		print (self.data)
		id = 0
		jml = len(self.data)
		for a in self.data:
			id += 1
			print ("\r\033[35;1m[#] \033[37;1mCracking \033[37;1m%s\033[37;1m/\033[33;1m%s" % (id, jml), end="", flush=True)
			self.check(a)
			if self.found > 0:
				sys.exit()

		print ("\n\033[33;1m[!] No results found")

	def CHash(self):
		if len(self.hash) == 32:
			pass
		else:
			print ("\033[31;1m[!] Please input hash md5")
			sys.exit()

runText(banner(), 0.01)
hash = input("\033[37;1m[\033[35;1m?\033[37;1m] Input Your Hash: \033[32;1m")
md = md5(hash)
md.CHash()
md.readDB()
md.crack()
