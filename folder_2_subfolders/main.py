import os
import glob
import shutil
import sys


def file_chopper(elements,count):
	total_elements = len(elements)
	print(total_elements,"te")
	for i in range(1,total_elements+1,count):
		diff = total_elements -i+1
		if i+count <= total_elements:  # to prevent index overflow
			start, end = i,i+count
		else:
			if diff >0:
				start,end = i, i+diff
		yield elements[start-1:end-1]

def splitter(source,count):
	#get the list of all elements in the directory
	os.chdir(source)
	elements = os.listdir()
	chopped_elements =file_chopper(elements,count)
	for i,j in enumerate(chopped_elements):
		print(i,j)


if __name__=="__main__":
	if len(sys.argv)<3:
		print("enter proper parameters required")
	else:
		source,count = sys.argv[1],int(sys.argv[2])
		if os.path.isdir(source):
			splitter(source,count)
		else:
			sys.exit(0)

