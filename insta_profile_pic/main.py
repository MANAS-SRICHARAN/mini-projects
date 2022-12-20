import requests
from lxml import html
import re
import sys
import pprint

def banner():
	print("\t\t*****************************************************")
	print("\t\t*********************Grab your profile***************")
	print("\t""""""""""""""""""""""""""""""""""""""""***************")


def main(user_name):
	banner()
	url= "https://www.instagram.com/{}/?hl=en".format(user_name)
	page = requests.get(url)
	if page.status_code==200:
		page_content = page.content
		html_content = html.fromstring(page-content)
		data = tree.xpath('//meta[starts-with(@name,"description")]/@content')	
		if data:
			data=data[0].split(,)
			followers = data[0][:-9].strip()
			following = data[1][:-9].strip()
			posts = "".join(re.findall(r'\d+[,]*'),data[2])
			name = re.findall(r'@.*',data[2])[0]
			aboutinfo = re.findall(r"")
	
if __name__=="__main__":
	if len(sys.argv)==2:
	main(sys.argv[-1])# passing the user_name 
	else:
		print("enter valid parameters for downlaoding the profile pic")

