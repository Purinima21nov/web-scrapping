import json
with open("task1.json","r")as file:
    k=json.loads(file.read())
    
z=[]
a=[]
for i in k:
    for j in i:
        if j=="Year":
            z.append(i[j])
z.sort()
print(z)
for h in z:
    for i in k :
        for j in i:
            if j=="Year":
                print(i[j])
                if h==i[j]:
                    a.append(i)
print(a)
with open("task2.json","w") as file:
    json.dump(a,file,indent=4)

    