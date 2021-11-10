import json, requests
from datetime import datetime

import pandas as pd

url_latest_update = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni-latest.json"
url_total_update = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json"


def get_regions():
    url = requests.get(url_latest_update)
    text = url.text

    data = json.loads(text)
    region_dict = [{'label': 'Maak uw keuze', 'value': 0}]
    for i in range(len(data)):
        region_dict.append({'label': data[i]['denominazione_regione'], 'value': data[i]['codice_regione']})

    return region_dict

def lastupdate_data(region_numb):
    url = requests.get(url_total_update)
    text = url.text

    posi_test_list_value = []
    posi_test_list_date = []

    data = json.loads(text)
    for i in range(len(data)):
        if str(data[i]['codice_regione']) == str(region_numb):

            posi_test_list_value.append(data[i]['variazione_totale_positivi'])

            date_full = str(data[i]['data'])
            date_new = date_full.replace('T', ' ')
            date = datetime.strptime(date_new, '%Y-%m-%d %H:%M:%S')
            posi_test_list_date.append(date)

    df = pd.DataFrame({'date': posi_test_list_date, 'value': posi_test_list_value})

    return df

def total_data(region_numb):
    url = requests.get(url_total_update)
    text = url.text

    posi_test_list_value = []
    posi_test_list_date = []

    data = json.loads(text)
    for i in range(len(data)):
        if str(data[i]['codice_regione']) == str(region_numb):

            posi_test_list_value.append(data[i]['totale_positivi'])

            date_full = str(data[i]['data'])
            date_new = date_full.replace('T', ' ')
            date = datetime.strptime(date_new, '%Y-%m-%d %H:%M:%S')
            posi_test_list_date.append(date)

    df_total = pd.DataFrame({'date': posi_test_list_date, 'value': posi_test_list_value})

    return df_total