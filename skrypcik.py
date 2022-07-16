import pandas as pd
xd = pd.read_csv("rozkladlotow2.csv")
df = pd.read_csv("rozkladlotow.csv")

listaskad=df["skad"].unique()

menu_options = {}

index=1
for value in listaskad:
    menu_options[index]=value
    index += 1

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


print_menu()
wybor = int(input('Wybierz lotnisko początkowe: '))
option = menu_options[wybor]

slownik={0:"Niedziela", 1:"Poniedziałek", 2:"Wtorek", 3:"Środa", 4:"Czwartek", 5:"Piątek", 6:"Sobota"}

nazwydowyswietlenia=[]
nazwylotow=df["lot_miasta"].unique()
for i in nazwylotow:
    i=str(i)
    if i.startswith(option):
        i=i.split(option)
        i=i[-1]
        nazwydowyswietlenia.append(i)

menu_options2 = {}
index=1
for wartosc in nazwydowyswietlenia:
    menu_options2[index]=wartosc
    index += 1
def print_menu2():
    for key in menu_options2.keys():
        print (key, '-', menu_options2[key] )
print_menu2()
wybor2 = int(input('Wybierz lotnisko docelowe: '))
option2 = menu_options2[wybor2]
nazwa=option+option2

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=4, ncols=2,figsize=(15,15))

tabela=xd[xd["lot_miasta"]==nazwa]
tabela=tabela.iloc[:,[1,2,3]].groupby(["dzientygodnia", "status", "liczba"]).count()


lotydoi = xd[xd["lot_miasta"]==nazwa]
lotydoi.iloc[:,[1,2,3]].groupby(["dzientygodnia", "status"]).count()


for i in range(0,7):
    try:
        if i in range(0,2):
            iframe=lotydoi[lotydoi["dzientygodnia"]==i]
            iframe.plot.bar(x='status', y='liczba', rot=0, ax=axes[0,i], label=slownik[i])
        if i in range(2,4):
            iframe=lotydoi[lotydoi["dzientygodnia"]==i]
            iframe.plot.bar(x='status', y='liczba', rot=0, ax=axes[1,(i-2)], label=slownik[i])
        if i in range(4,6):
            iframe=lotydoi[lotydoi["dzientygodnia"]==i]
            iframe.plot.bar(x='status', y='liczba', rot=0, ax=axes[2,(i-4)], label=slownik[i])
        else:
            iframe=lotydoi[lotydoi["dzientygodnia"]==i]
            iframe.plot.bar(x='status', y='liczba', rot=0, ax=axes[3,(i-6)], label=slownik[i])
    except:
        pass
fig.savefig(f'{nazwa}.png', facecolor="white")