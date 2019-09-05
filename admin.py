#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Masukkan Nama Situs Target \n(contoh : thenextlevel.com atau www.thenextlevel.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(0); print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	Space(0); print "   +-++-++--++-++-++-++++-++-++-+ +-++-++-++-++-++-++-++-++    "
	Space(0); print "          The Next Level AdminFinder Version 1 (Beta)          "
	Space(0); print "                         @bell_attcker                         "
	Space(0); print "                        Coded By Mr.Bell                       "
	Space(0); print "                       THE NEXT LEVEL TEAM                     "
	Space(0); print "                 website:http://tnlofficial.6te.net/           "
	Space(0); print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	

	
Credit()
findAdmin()
