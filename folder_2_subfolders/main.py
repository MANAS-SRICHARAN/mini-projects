import os
import glob
import shutil
import sys


if __name__=="__main__":
	if len(sys.argv)<3:
		print("enter proper parameters required")
	else:
		print(sys.argv[1],"**",sys.argv[2])

