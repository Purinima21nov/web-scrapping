import requests
import os
from task1 import top_list
k=top_list()
def scrape_movie_details():
    for i in k:
        path="/home/admin123/Desktop/web_scrapping/task8/"+i["Name"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/web_scrapping/task8/"+i["Name"]+".text","w")
            url=requests.get(i["Url"])
            bs=create.write(url.text)
            create.close()
scrape_movie_details()
