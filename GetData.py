import json, requests
from datetime import datetime

import pandas as pd
# source: https://github.com/pcm-dpc/COVID-19
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

def get_medicaldata(region_numb):
    url = requests.get(url_total_update)
    text = url.text

    medical_update_date = []
    medical_update_value = []

    data = json.loads(text)
    for i in range(len(data)):
        if str(data[i]['codice_regione']) == str(region_numb):
            medical_update_value.append(data[i]['totale_ospedalizzati'])

            date_full = str(data[i]['data'])
            date_new = date_full.replace('T', ' ')
            date = datetime.strptime(date_new, '%Y-%m-%d %H:%M:%S')
            medical_update_date.append(date)
            #

    df_medical= pd.DataFrame({'date': medical_update_date, 'value': medical_update_value})


    return df_medical

#https://www.agenas.gov.it/covid19/web/index.php?r=site%2Fgraph3
ICU_beds_capacity = [
                     {'region': 'Abruzzo', 'regio_numb': 13, 'max_capacity': 181},
                     {'region': 'Basilicata', 'regio_numb': 17, 'max_capacity': 88},
                     {'region': 'Calabria', 'regio_numb': 18, 'max_capacity': 174},
                     {'region': 'Campania', 'regio_numb': 15, 'max_capacity': 555},
                     {'region': 'Emilia-Romagna', 'regio_numb': 8, 'max_capacity': 889},
                     {'region': 'Friuli Venezia Giulia', 'regio_numb': 6, 'max_capacity': 175},
                     {'region': 'Lazio', 'regio_numb': 12, 'max_capacity': 943},
                     {'region': 'Liguria', 'regio_numb': 7, 'max_capacity': 217},
                     {'region': 'Lombardia', 'regio_numb': 3, 'max_capacity': 1530},
                     {'region': 'Marche', 'regio_numb': 11, 'max_capacity': 238},
                     {'region': 'Molise', 'regio_numb': 14, 'max_capacity': 39},
                     {'region': 'P.A. Bolzano', 'regio_numb': 21, 'max_capacity': 100},
                     {'region': 'P.A. Trento', 'regio_numb': 22, 'max_capacity': 90},
                     {'region': 'Piemonte', 'regio_numb': 1, 'max_capacity': 628},
                     {'region': 'Puglia', 'regio_numb': 16, 'max_capacity': 482},
                     {'region': 'Sardegna', 'regio_numb': 20, 'max_capacity': 204},
                     {'region': 'Sicilia', 'regio_numb': 19, 'max_capacity':861},
                     {'region': 'Toscana', 'regio_numb': 9, 'max_capacity': 570},
                     {'region': 'Umbria', 'regio_numb': 10, 'max_capacity': 84},
                     {'region': "Valle d'Aosta", 'regio_numb': 2, 'max_capacity': 33},
                     {'region': "Veneto", 'regio_numb': 5, 'max_capacity': 1000}
    ]


def get_ICUdata(region_numb):
    url = requests.get(url_total_update)
    text = url.text

    ICU_update_date = []
    ICU_update_value = []

    data = json.loads(text)
    for i in range(len(data)):
        if str(data[i]['codice_regione']) == str(region_numb):
            if data[i]['ingressi_terapia_intensiva']:
                for l in range(len(ICU_beds_capacity)):
                    if str(ICU_beds_capacity[l]['regio_numb']) == str(region_numb):

                        ICU_percent = data[i]['terapia_intensiva'] /ICU_beds_capacity[l]['max_capacity'] * 100

                        ICU_update_value.append(ICU_percent)

                        date_full = str(data[i]['data'])
                        date_new = date_full.replace('T', ' ')
                        date = datetime.strptime(date_new, '%Y-%m-%d %H:%M:%S')
                        ICU_update_date.append(date)

    df_ICU = pd.DataFrame({'date': ICU_update_date, 'value': ICU_update_value})

    return df_ICU

def change_color(region_numb):
    # color_zone = ""

    df = lastupdate_data(region_numb)
    df_total = total_data(region_numb)
    df_medical = get_medicaldata(region_numb)
    df_ICU = get_ICUdata(region_numb)

    df_rolweek = df.resample('W', on='date').mean()

    ## White zone
    if df_rolweek['value'].iloc[-1] < 50:
        color_zone = 'White'
    elif df_rolweek['value'].iloc[-1] >= 50 and df_ICU['value'].iloc[-1] < 10:
        color_zone = 'White'

    ## Yellow zone

    elif 50 < df_rolweek['value'].iloc[-1] <= 150 and 10 < df_ICU['value'].iloc[-1] < 20:
        color_zone = 'Yellow'
    elif df_rolweek['value'].iloc[-1] > 150 and 10 < df_ICU['value'].iloc[-1] < 20:
        color_zone = 'Yellow'

    ## Orange zone
    elif df_rolweek['value'].iloc[-1] > 150 and 20 < df_ICU['value'].iloc[-1] < 30:
        color_zone = 'Orange'

    ## Red zone
    elif df_rolweek['value'].iloc[-1] > 150 and 30 < df_ICU['value'].iloc[-1]:
        color_zone = 'Red'


    return color_zone
