from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
import io

directory = "./scraped_images/"
if not os.path.exists(directory):
	os.makedirs(directory)

search = raw_input("Search for:")
params = {"q": search}
page = requests.get("https://www.bing.com/images/search/", params=params)

data = page.text
soup = BeautifulSoup(data, "html.parser")

for item in soup.find_all("a",{"class":"thumb"}, limit=10):
	img_obj = requests.get(item.attrs["href"])
	print('Getting', item.attrs["href"])
	title = item.attrs["href"].split("/")[-1]
	try:
		img = Image.open(io.BytesIO(img_obj.content))
		img.save("./scraped_images/" + title, img.format)
	except:
		pass
