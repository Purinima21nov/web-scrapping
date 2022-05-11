import requests
import json
import bs4
from task7 import analyse_movies_directors
with open("task5.json","r") as file:
    k = json.load(file)
    
directors_dict={}
for i in analyse_movies_directors():
    if i not in directors_dict:
        directors_dict[i]={}
directors_lang=directors_dict
    
def analyse_language_and_directors():
    
    for i in range(len(k)):
        for director in directors_lang:
            if director in k[i]['Director']:
                if "language" in k[i]:
                    for language in k[i]["language"]:
                        directors_lang[director][language] = 0
        
    for i in range(len(k)):
        for director in directors_lang:
            if director in k[i]['Director']:
                if "language" in k[i]:
                    for language in k[i]["language"]:
                        directors_lang[director][language] += 1
    with open("task10.json","w+") as file:
        json.dump(directors_lang , file, indent=4)
    # print(directors_lang)
analyse_language_and_directors()

    