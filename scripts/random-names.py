import configparser
import random

namesToGenerate = 5

nameconfig = configparser.ConfigParser(strict=False)
nameconfig.read('names.ini')
companyNames=[]
for key in nameconfig['companynames']:
    companyNames.append(key.capitalize())
companySuffixes=[]
for key in nameconfig['companysuffix']:
    companySuffixes.append(key.capitalize())
    
firstNames=[]
for key in nameconfig['firstnames']:
    firstNames.append(key.capitalize())
lastNames=[]
for key in nameconfig['lastnames']:
    lastNames.append(key.capitalize())


print(f"{namesToGenerate} names:")
pythonList=[]
for i in range(namesToGenerate):
    first=random.choice(firstNames)
    last=random.choice(lastNames)
    pythonList.append(f"\"{first} {last}\"")
    print(f"{first} {last}")
l = ",".join(pythonList)
print(f"[{l}]")
print(f"{namesToGenerate} company names:")
pythonList=[]
for i in range(namesToGenerate):
    companyName=random.choice(companyNames)
    companySuffix=random.choice(companySuffixes)
    pythonList.append(f"\"{companyName} {companySuffix}\"")
    print(f"{companyName} {companySuffix}")
l = ",".join(pythonList)
print(f"[{l}]")
