import requests
import json
import bs4
from task4 import movie
with open("task1.json","r") as file:
    k = json.load(file)
list1=[]
def list_details():
    for i in k:
        a=i["Url"]
        details = movie(a)
        list1.append(details)
    with open("task5.json","w+") as file:
        json.dump(list1, file, indent=4)
    print(list1)
list_details()
    