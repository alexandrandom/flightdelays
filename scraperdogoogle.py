from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

df = pd.read_csv("tabelazlotami-airportia.csv")
listamiast = df['skad'].unique()
listamiastdokad = df['dokad'].unique()
slownikwyniki = {}

for miasto in listamiast:
    try:
        r = requests.get(f"https://www.google.com/search?q=gdzie+jest+{miasto}&client=safari&rls=en&sxsrf=ALiCzsZdcLdDGrXSP_Uf1t6dCaP_1boUZA%3A1652440930344&ei=Yj9-YqDaFOfirgTQ6L7oCA&ved=0ahUKEwigk6mVrtz3AhVnsYsKHVC0D40Q4dUDCA0&uact=5&oq=gdzie+jest+Heraklion&gs_lcp=Cgdnd3Mtd2l6EAMyCAghEBYQHRAeOgcIABBHELADSgUIPBIBMkoECEEYAEoECEYYAFCJBViJBWCACGgCcAF4AIAB9QGIAfUBkgEDMi0xmAEAoAECoAEByAEIwAEB&sclient=gws-wiz", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15", "Referer": "https://google.com"})
        zupa=bs(r.content, "html.parser")
        napis = zupa.find("span", {"class": "desktop-title-subcontent"})
        if "," in napis.text:
            ciag=napis.text.split(", ")
            slownikwyniki[miasto]=ciag[-1]
        else:
            slownikwyniki[miasto]=napis.text
    except:
        slownikwyniki[miasto]="-"

slownikwyniki2={}

for key, value in slownikwyniki.items():
    if slownikwyniki[key]=="-":
        try:
            r = requests.get(f"https://www.google.com/search?client=safari&rls=en&q={key}+country&ie=UTF-8&oe=UTF-8", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15", "Referer": "https://google.com"})
            zupa=bs(r.content, "html.parser")
            napis = zupa.find("span", {"class": "wHYlTd z8gr9e"})
            slownikwyniki2[key]=napis.text
        except:
            slownikwyniki2[key]="-"
    else:
        slownikwyniki2[key]=slownikwyniki[key]
print(slownikwyniki2)