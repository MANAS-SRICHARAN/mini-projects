from PIL import Image

import os
import re

def blender(img_path,watermark_path):
	img = Image.open(img_path)
	w_img = Image.open(watermark_path)
	#resining the watermark accoringly 
	img_size = img.size
	w_img = w_img.resize((int(img_size[0]*0.1),int(img_size[1]*0.1)))
	#paste it on the image
	img.paste(w_img,(img_size[0]-w_img.size[0]-20,img_size[1]-w_img.size[1]-	20),w_img)
	return img
if __name__=="__main__":
	folder_path = input("enter the image path")
	watermark_path = input("enter the watermark path")
	
	os.chdir(folder_path)	
	images = [element for element in os.listdir() if re.match(r'(.*\.png)|(.*\.jpg)',element)]
	print(images)
"""
	final_img = blender(img_path,watermark_path)
	#conver the final image to rgb as jpeg doesnt support rgba
	final_img = final_img.convert("RGB")
	print("saving the final image ")
	final_img.save("output.jpg")
	final_img.show()
"""
