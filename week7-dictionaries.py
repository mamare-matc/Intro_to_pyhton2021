#!/usr/bin/env python3

# creat a mapping of FQDN to IP address mappings

address = {
   'server1.testlab.com': '192.168.1.10',
   'server2.testlab.com': '192.168.1.11',
   'server3.testlab.com': '192.168.1.12',
   'server4.testlab.com': '192.168.1.13',
   'server5.testlab.com': '192.168.1.14',
   'server6.testlab.com': '192.168.1.15'
}

# list all FQDN in your dictionary
dictkeys = list (address.keys())

print("List of all FQDN: ", dictkeys)

#list all IP addresss in your dictionary 
dictvalues = list (address.values())

print ("List of all the IP Addresses : ", dictvalues)

#list all of the full records
print("List of the full records: ")
for k, v in address.items():
    print(k, v)

#Add a few more name to address mappings
address['server7.testlab.com'] = ' ',
address['server8.testlab.com'] = ' '

print(address)

#test if server2.testlab.com is contained in your dictionary
key = 'server2.testlab.com'

if key in address.keys():
  print('key found')
else:
  print('key not found')

#test if server10.testlab.com is contained in your dictionary 
secondkey = 'server10.testlab.com'

if secondkey in address.keys():
   print('key found')
else:
  print('key not found')
