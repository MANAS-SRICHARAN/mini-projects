"""
Author: manas.v

plan of action:
1) get user input for total characters 
2) have a predefined list is numeric characters, usnig string package
3)alphabets 
4) specialcharacters
5) create a function, that generates the pawwsd depending on the length of passwd needed
6) using the random to shuffle all the passwoord charcaters 
"""
import random
import string
import math 

alphabets = string.ascii_lowercase+string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation


def generate_passwd(count):
	#50-30-20 rule
	alpha_count = count//2
	digits_count = math.ceil(count*0.3)
	special_count = count -(alpha_count+digits_count)
	passwd = random.sample(alphabets,alpha_count)+random.sample(digits,digits_count)+random.sample(special_characters,special_count) #shuffle accpes sequences and sets
	#passwd=list(passwd) # shuffle doesnt accept sequences but only list
	random.shuffle(passwd)
	return "".join(passwd)

if __name__=="__main__":
	no_letters = int(input("total number of characters needed \n"))
	print("your password"+":"+generate_passwd(no_letters))

	


