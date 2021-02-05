import os
z = []
with open('kickass1.txt','r',encoding="utf-8") as file:
    for line in file:
        if line.replace("\n", "") and not line.isspace():
            z.append(line)
counter=0
torr={}
j=0

for i in z:
    if "Posted by" in i:
        counter=counter+1
        if z[j-1].replace('\n','') and z[j+5].replace('\n','') and z[j+8].replace('\n','') and z[j+9].replace('\n',''):
            torr[counter]=[z[j-1].replace('\n','') ,z[j+5].replace('\n','') , z[j+8].replace('\n','') , z[j+9].replace('\n','')]

    j+=1
con=1
lis=[]
with open("torr.txt", 'w',encoding="utf-8") as f:
    for t in torr.values():
        lis.append(t)
        f.write(' '.join(t))
        f.write('\n')
        con+=1
print(len(lis))
result = sorted(set(map(tuple, lis)), reverse=True)
#lis=sorted(set(lis))
print(len(result))
print(len(lis))


with open("final.txt", "w",encoding="utf-8") as f:
    for i in result:
        f.write(str(i))
        f.write("\n")
