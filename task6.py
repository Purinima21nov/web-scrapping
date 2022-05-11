import requests
import json
import bs4
with open("task5.json","r") as file:
    k = json.load(file)

def analyse_movies_language():
    dict={}
    for i in k:
        for j in i :
            if j=="language":
                for x in i[j]:   
                    if x not in dict:
                        dict[x]=1
                    else:
                        dict[x]=dict[x]+1
    # return(dict)
    with open("task6.json","w+") as file:
        json.dump(dict , file, indent=4)
analyse_movies_language()

