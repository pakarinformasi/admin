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
	print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	print "   +-++-++--++-++-++-++++-++-++-+ +-++-++-++-++-++-++-++-++    "
	print "          The Next Level AdminFinder Version 1 (Beta)          "
	print"                          @bell_attcker                         "
	print "                        Coded By Mr.Bell                       "
	print "                       THE NEXT LEVEL TEAM                     "
	print "                 website:http://tnlofficial.6te.net/           "
	print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	

	
Credit()
findAdmin()
