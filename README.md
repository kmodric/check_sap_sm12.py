# check_sap_sm12.py
Nagios plugin for checking SAP lock tables - sm12

![](/images/check_sap_sm122.png)

![](/images/check_sap_sm12.png)


Usage:./check_sap_sm12.py \<SID\> 

Example:
root@:~/github# ./check_sap_sm12.py SBX

CRITICAL - LockTable over 1 days: 10 LockTable | LockTable=10

                                                                      
### Prerequisite:
https://github.com/piersharding/python-sapnwrfc

### Wiki:
Installation of sapnwrfc for python on Linux and Unix
https://wiki.scn.sap.com/wiki/display/EmTech/Installation+of+sapnwrfc+for+python+on+Linux+and+Unix






To prepare a script, you'll need a 'yml' file similar to the 'sap.yml' file included with the sapnwrfc download. The file looks 

like this:
#### Example of SID.yml file

ashost: gecko.local.net

sysnr: "01"

client: "001"

user: developer

passwd: developer

lang: EN

trace: 3

loglevel: warn
