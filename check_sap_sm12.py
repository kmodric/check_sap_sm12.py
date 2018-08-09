#!/usr/bin/python

import os
os.chdir('/tmp')

import sapnwrfc
import sys
import json


if len(sys.argv) <> 2:
	print "Usage:" + sys.argv[0] +" <SID>"
  	sys.exit(3)
  
from datetime import date, timedelta
today = date.today()
yesterday = date.today() - timedelta(1)
if os.path.exists("/etc/sapmon/"+sys.argv[1]+".yml"):   
	sapnwrfc.base.config_location = "/etc/sapmon/"+sys.argv[1]+".yml"
else:
	print "File not found:" +"/etc/sapmon/"+sys.argv[1]+".yml"
  	sys.exit(3)
sapnwrfc.base.load_config()
 
#print "making a new connection:"
try:
        conn = sapnwrfc.base.rfc_connect()
        fd = conn.discover("ENQUE_READ")
        f = fd.create_function_call()
        f.GCLIENT('')
        f.GUNAME('')
        f.invoke()

        d = f.ENQ.value
        todo = {'results': d}
	number=0
	for i in d:
		if (not today.strftime('%Y%m%d') in i['GTDATE'] and not 'SAP_WSRT' in i['GUNAME'] and not 'ALEREMOTE' in i['GUNAME'] and not 'SAP_WS_SUPER' in i['GUNAME'] and not 'BGRFC_SUPERV' in i['GUNAME'] and not 'BGRFCSUPER' in i['GUNAME'] ) and not yesterday.strftime('%Y%m%d') in i['GTDATE']:		
			number += 1
	
	lock = str(number)
	if number  >= 1:
		print "CRITICAL - LockTable over 1 days: "+lock+" LockTable | LockTable="+lock
		sys.exit(2)
	else:
		print "OK - LockTable over 1 days: "+lock+" LockTable | LockTable="+lock
		sys.exit(0)


	conn.close()
	#print "closing..."

except sapnwrfc.RFCCommunicationError as e:
	if 'NO_DATA_FOUND' in e[0]:
		print "No data."
	else:
        	print "UKNOWN:" + e[0]
		sys.exit(3)
		
