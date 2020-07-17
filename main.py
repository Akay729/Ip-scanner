import subprocess
import csv
from datetime import datetime 



def ip_scanner():
	addressList = []
	
	for ping in range(204,207):
	    print('\n+---------------------------------------------------+',
	    	'\n+----------------------NEW-IP-----------------------+',
	    	'\n+---------------------------------------------------+')

	    now_ = datetime.now()
	    address = "192.168.1." + str(ping)
	    res = subprocess.call(['ping', '-w', '3', address])

	    if res == 0:
	    	addressList.append([address, now_])
	    	print( "ping to", address, "OK",)

	    elif res == 1:
	        print("no reply from", address,)

	    elif res == 2:
	        print("ping to ", address, " failed!")

	return addressList

def to_csv(addressList):
	with open('ips.csv', 'w', newline='') as csvfile:
	    writer = csv.writer(csvfile, delimiter=' ', quotechar='|',)
	    for i, j in addressList:
	    	writer.writerow([i, j])
	   
	    csvfile.close()
	
if __name__ == '__main__':
	ipsArray = ip_scanner()
	to_csv(ipsArrays)
