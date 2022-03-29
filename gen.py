import random
import string
import os
import sys
import time

os.system('figlet "pass gen" | lolcat')
print(" ")
os.system("  cowsay -f tux 'Alligators rock more than Linux!'     ")


os.system('echo "--created by jerome"  ')


def Writertext(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

				
time.sleep(2)
ask = """  
\033[1;36;40mhow many strings you want
"""

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_random_password():
	## length of password from the user
	length = int(input("? "))
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	print("  ")
	print("\033[1;36;32mpasswords is")
	print(" ")
	
	print("".join(password))
	
print(" ")
Writertext(ask)
generate_random_password()
