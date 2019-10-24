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
	print(''' \033[96m	
         _,met$$$$$gg.           
      ,g$$$$$$$$$$$$$$$P.        
    ,g$$P""       """Y$$.".      
   ,$$P'              `$$$.      
  ',$$P       ,ggs.     `$$b:    
  `d$$'     ,$P"'   .    $$$     
   $$P      d$'     ,    $$P     
   $$:      $$.   -    ,d$$'     
   $$\;      Y$b._   _,d$P'      
   Y$$.    `.`"Y$$$$P"'          
   `$$b      "-.__
    `Y$$
     `Y$$.
       `$$b.
         `Y$$b.
            `"Y$b._
                `""""
|Version   : V.1(Beta)      |
|Team      : THE NEXT LEVEL |
|Create    : Mr.Bell        |
|     ADMIN FINDER TOOLS    |
############################## \n \033[91m''')
	
Credit()
findAdmin()
