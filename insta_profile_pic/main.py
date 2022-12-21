import requests
from lxml import html
import re
import sys
import pprint

def banner():
	print("\t\t*****************************************************")
	print("\t\t*********************Grab your profile***************")
	print('\t""""""""""""""""""""""""""""""""""""""""***************')


def main(user_name):
	banner()
	url= "https://www.instagram.com/{}/?hl=en".format(user_name)
	headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Versio			n/16.1 Safari/605.1.15'}
	page = requests.get(url,headers=headers)
	if page.status_code==200:
		page_content = page.content
		html_content = html.fromstring(page_content)
		data = html_content.xpath('//meta[starts-with(@name,"description")]/@content')	
		if data:
			data=data[0].split(',')
			followers = data[0][:-9].strip()
			following = data[1][:-9].strip()
			posts = "".join(re.findall(r'\d+[,]*',data[2]))
			name = re.findall(r'@.*',data[2])[0]
			profile_details ={
				'success':True,
				'name':name,
				'posts':posts,
				'followers':followers,
				'following':following
				}
		else:
			profile_details={
				'success':False
				}
		return profile_details
	else:
		return {'success':False}

	
if __name__=="__main__":
	print("welcome")	
	if len(sys.argv)==2:
		profile_details = main(sys.argv[-1])# passing the user_name 

	else:
		print("invalid parameters")
	print(profile_details)
