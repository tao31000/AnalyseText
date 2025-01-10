import re
import pandas

vides=["the","to","of","we","and","have","it","is","our","in","which","i","be","for","sir","not","are","a","that","been","shall","us","no","as","but","this","so","if","what","those","my","by","with","may","there","has","ourselves","they","who","or","can","all","let","any","at","an","last","these","must","long","on","from","when","next","me","mr","man","than","do","very"]

f = open("disc.txt", "r")
discours=f.readlines()
f.close()


mots=[]
for ligne in discours:
  m=re.split(r'\W+',ligne)
  mots.extend(m)

m=[v.strip().lower() for v in mots if v.strip()!='']
mots=m

for m in mots:
  if(m in vides):
    print("removal of",m)
    print(len(mots),"",end="")
    mots.remove(m)
    print(len(mots))


histo={m:mots.count(m) for m in mots}


mots=list(histo.keys())
freq=list(histo.values())
for i in range(len(freq)):
  m=i
  for j in range(i+1,len(freq)):
    if freq[j]>freq[m]:
      m=j
    aux=freq[m]
    freq[m]=freq[i]
    freq[i]=aux
    aux=mots[m]
    mots[m]=mots[i]
    mots[i]=aux

df = pandas.DataFrame({'freque': freq}, index=mots)

ax = df.plot.bar(rot=75)

