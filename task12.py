import requests
import json
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/m/toy_story_4"

def movie_caste_url():
    response=requests.get(url)
    a = BeautifulSoup(response.text,"html.parser")
    # text=a.prettify()
    
    list = []
    
    div = a.find("div",class_ = "media-body")
    t1 = div.find_all("span",class_ = "title")
    # t2 = div.find_all("div",class_ = "cast-item media inlineBlock moreCasts")

    for i in t1:
        print(i)
        # dic={}
        # a=i.find("a")["href"][:11]
        # dic["actor_name"]=a
        # list.append(dic)   
       
    # for i in t2:
    #     dic={}
    #     a2=i.find("a")["href"][:11]  
    #     dic["actor_name"]=a2
    #     list.append(dic)   
    # print(list) 
    # with open("task12.json","w+") as file:
    #     json.dump(list , file, indent=4)
movie_caste_url()

