import os

def find_file(input_val,path):
	found=False
	os.chdir(path)
	dir_elements = os.listdir()
	for element in dir_elements:
		path = os.path.abspath(element)
		if os.path.isfile(path):
			with open(element,'r') as f:
				if input_val in f.read():
					found=True
					print("*"*5+"found"+"*"*5)
					print("the path is :",path)
		if os.path.isdir(path):
			find_file(input_val,path)

	if found ==False:
		return False

if __name__=="__main__":
	input_val = input("enter the input you want to find\n")
	path = input("enter the path for file search\n")
	if os.path.exists(path):
		find_file(input_val,path)
	else:
		print("enter a valid directory path")

