import requests
import os
import random
import time
import json
# from task1 import top_list
# k=top_list()
k=open("task5.json","r")
k=json.load(k)
def scrape_movie_details():
    a=random.randint(1, 3)
    for i in k:
        # print(i)
        path="/home/admin123/Desktop/web_scrapping/task9/"+i["movie_name"]+".json"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/web_scrapping/task9/"+i["movie_name"]+".json","w")
            json.dump(i,create,indent=4)
            # url=requests.get(i["Url"])
            # bs=create.write(url.text)
            create.close()
    time.sleep(a)
scrape_movie_details()
