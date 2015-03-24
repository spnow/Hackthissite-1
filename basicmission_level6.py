############################################################################################################
#	Hack This Site Baisc Mission Level 6
#
#	Developed with Python 2.7.6
#
#	An encryption system has been set up, which uses an unknown algorithm to change the text given.
#
#	The password is encrypted by incrementing each characters hex calue by its position on the password.
#	This script takes an encrypted password and reverses the encryption process. 
#
############################################################################################################

password = raw_input('Enter your encrypted password: ')
encrypted_password = []
count = 0

for i in password:
	char = (ord(i)) - count
	char = str(unichr(char))
	encrypted_password.append(char)
	count = count + 1

print "".join(encrypted_password)