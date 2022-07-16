import requests
import json
import pandas

lotniska = pandas.read_json("lotniska.json")

tabelalotnisk = lotniska.iloc[:,[0,6,7,1]]

nielista = tabelalotnisk.iloc[:, 2]

lista = nielista.tolist()


pierwszaczesc = []
drugaczesc = []
trzeciaczesc = []
czwartaczesc = []

for i in range(916):
    pierwszaczesc.append(lista[i])

for i in range(916, 1831):
    drugaczesc.append(lista[i])

for i in range(1831, 2747):
    trzeciaczesc.append(lista[i])

for i in range(2747, 3613):
    czwartaczesc.append(lista[i])

#check
for i in lista:
    if i not in pierwszaczesc:
        if i not in drugaczesc:
            if i not in trzeciaczesc:
                if i not in czwartaczesc:
                    print(i)


panstwa = []
kody_miast = []
miasta = []
for i in czwartaczesc:
    try:
        apikey = "ee50fc3e-9210-4c81-9d53-c8c6f421ba6a"
        pobraniemiasta = requests.get(f"https://airlabs.co/api/v9/cities?city_code={i}&api_key={apikey}")
        tekstjsona=pobraniemiasta.json()
        liljson = tekstjsona["response"][0]
        panstwo = liljson["country_code"]
        kod_miasta = liljson["city_code"]
        miasto = liljson["name"]
        panstwa.append(panstwo)
        kody_miast.append(kod_miasta)
        miasta.append(miasto)
    except:
        pass

df = pandas.DataFrame(list(zip(panstwa, kody_miast, miasta)), columns=['panstwa', 'kody_miast', 'miasta'])
df.to_csv("czwartaczesc.csv", header=False, index=False)
