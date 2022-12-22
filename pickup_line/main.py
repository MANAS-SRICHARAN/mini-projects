import sys
import random
import os 


def pickup_line(file_path):
	line_numbers=[]
	try:
		with open(file_path,"r") as file:
			line_no=1
			for line in file:
				if line.strip():
					line_numbers.append(line_no)
				line_no=line_no+1
			random.shuffle(line_numbers)#for randomness shuffle the line numbers
			number=int(random.choice(line_numbers))
			file.seek(0,0) # set the pointer back to the file starting position
			line_no =1
			for line in file:
				if line_no == number: print(file.readline())
				line_no+=1
	except (FileNotFoundError,IOError) as e:
		print(e)

if __name__=="__main__":
	if len(sys.argv) == 2:
		file_path = sys.argv[1]
		if os.path.isfile(file_path):
			pickup_line(file_path)
		else:
			print("this is not a file :(")
			sys.exit(0)	
	
	else:
		print("enter correct parameters")
		sys.exit(0)
