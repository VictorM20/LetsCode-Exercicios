"""
Em 2019 surgiram os primeiros casos de COVID-19 que se alastrou pelo
mundo resultando numa pandemia. A proposta deste exercício é utilizar
uma API com informações de COVID-19 do mundo todo desde o início da
proliferação e descobrir que dia o Brasil confirmou o primeiro caso de
Coronavírus.

Para fazer isso, utilize a URL "https://api.covid19api.com/country/brazil" em seu
código. Ela retorna uma lista de dicionários, onde cada dicionário traz
informações através das chaves:

"ID", "Country", "CountryCode", "Province", "City",
"CityCode","Lat","Lon","Confirmed","Deaths", "Recovered", "Active" e "Date".

Utilize essas informações e retorne a data em que o Brasil confirmou o
primeiro caso de COVID.
"""
import requests

url = "https://api.covid19api.com/country/brazil"
req = requests.get(url)
dados = req.json()

for i in dados:
    if i['Confirmed'] != 0:
        print(f"Brasil confirmou o primeiro caso de COVID-19 em {i['Date']}")
        break
