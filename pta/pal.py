import math

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

n = input('')
output=[]

for i in range(pow(2,n)):
	binary=bin(i)[2:].zfill(n)
	if(is_palindrome(binary)):
		st = ''
		for s in binary:
			st += (str(s) + ' ')
		print (st + '1')
	else:
		st = ''
		for s in binary:
			st += (str(s) + ' ')
		print (st + '0')
