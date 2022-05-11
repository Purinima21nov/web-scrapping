import requests
import json
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/m/incredibles"
# response=requests.get(url)
# bs=bs4.BeautifulSoup(response.text,"html.parser")
# text=bs.prettify()

def movie(link):
    response=requests.get(link)
    a = BeautifulSoup(response.text,"html.parser")
    text=a.prettify()
    list = []
    # a=link
    div = a.find("div",class_ = "body_main container")
    tbody = div.find("div",class_ = "media-body")
    li = tbody.find_all("li")
    
    dict={}
    movie_name=div.find("h1", slot="title").get_text()
    dict["movie_name"]=movie_name
    for i in li:
        i=i.text
        i=i.split()
        if "Rating:" in i:
            dict["rating"] = i[1]
        if "Language:" in i:
            dict["language"]=i[2:]
        if "Runtime:" in i:
            x=i[1:]
            for j in range(len(x)):
                if "h" in x[j]:
                    hour=int(x[j][:-1])*60
                elif "m" in x[j]:
                    min=int(x[j][:-1])
            time=hour+min
            dict["Runtime"] = time
            # dict["Runtime"]=i[1:]
        if "Director:" in i:
            a=i[1:] 
            d=""
            for k in a:
                d=d+k
            d=d.split(",")
            # print(d)
            dict["Director"] = d
        if "Genre:" in i:
            c=i[1:]
            s=" "
            for l in c:
                s+=l
            s=s.strip()
            s=s.split(",")
            dict["genre"] = s
    with open("task4.json","w+") as file:
        json.dump(dict , file, indent=4)
    return dict
movie(url)

        
           