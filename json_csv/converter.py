"""
Author: Manas v

"""
import json

with open("input.json") as file:
	data =json.loads(file.read()) # converting json string to python object
headers = ",".join([*data[0]]) #variable declared inside with is available outside

output = headers #+= doesnt work because output hasnt been initilised first to use it 
for obj in data:
	output+="\n"+",".join([str(i) for i in obj.values()])
with open("output.csv","w") as f:
	f.write(output)

	  
