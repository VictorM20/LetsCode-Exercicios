import requests as r
import datetime as dt
import csv
url = "https://api.covid19api.com/country/brazil"
resp = r.get(url)
raw_data = resp.json()
# print(raw_data[0])
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0, ['Confirmados', 'Mortes', 'Recuperados', 'Ativos', 'Data'])
CONFIRMADOS = 0
MORTES = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4
for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

with open('brasil-covid.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)
for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')
    print(final_data)