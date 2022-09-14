import csv
import datetime as dt

import requests as r
from PIL import Image

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


def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [{
            'label': labels[0],
            'data': y
        }]


def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }


def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_datasets(y, labels)
    options = set_title(title)
    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart


def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content


def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)


def display_image(path):
    img_pil = Image.open(path)
    img_pil.show()


y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels = ['Confirmados', 'Recuperados']
x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))
chart = create_chart(x, [y_data_1, y_data_2], labels, title='Confirmados x Recuperados')
chart_content = get_api_chart(chart)
save_image('grafico.png', chart_content)
display_image('grafico.png')

from urllib.parse import quote  # biblioteca para converter texto em url


def get_api_qrcode(link):
    text = quote(link)  # Transforma o link em um texto para ser usado na URL
    url_base = 'https://quickchart.io/qr'  # URL base para gerar o QR Code
    resp = r.get(f'{url_base}?text={text}')  # Faz a requisição
    return resp.content  # Retorna o conteúdo da resposta


url_base = 'https://quickchart.io/chart'  # URL base para gerar o QR Code
link = f'{url_base}?c={str(chart)}'  # Cria o link para o gráfico
save_image('qrcode.png', get_api_qrcode(link))  # Salva o QR Code
display_image('qrcode.png')  # Exibe o QR Code
