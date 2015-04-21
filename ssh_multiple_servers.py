##### Python program for running commands on multiple servers#####
#### Author Palavi

# importing ParallelSSHClient module 
from pssh import ParallelSSHClient
import sys
# Assigning command line arguments to a list
hos = sys.argv
print hos
print type(hos)
del hos[0]
print hos
client = ParallelSSHClient(hos)
while True:
	command= raw_input("\nEnter commands or type number to disconnect : ")
	if command.isalpha() == True:
		output = client.run_command(command, sudo=True)
		for host in output:
			for line in output[host]['stdout']:
				print "Host %s-output : %s" %(host,line)
	else:
		print "Disconnecting..."

		

