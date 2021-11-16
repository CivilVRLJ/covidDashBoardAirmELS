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

            posi_test_list_value.append(data[i]['totale_positivi'])

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

# def get_medicaldata(region_numb):
#     url = requests.get(url_total_update)
#     text = url.text
#
#     medical_update_date = []
#     medical_update_value = []
#
#     data = json.loads(text)
#     for i in range(len(data)):
#         if str(data[i]['codice_regione']) == str(region_numb):
#             medical_update_value.append(data[i]['ricoverati_con_sintomi'])
#
#             date_full = str(data[i]['data'])
#             date_new = date_full.replace('T', ' ')
#             date = datetime.strptime(date_new, '%Y-%m-%d %H:%M:%S')
#             medical_update_date.append(date)
#             #
#
#     df_medical= pd.DataFrame({'date': medical_update_date, 'value': medical_update_value})
#
#
#     return df_medical

#https://www.agenas.gov.it/covid19/web/index.php?r=site%2Ftab2
ICU_Med_beds_capacity = [
                     {'region': 'Abruzzo', 'regio_numb': 13, 'ICU_capacity': 181, 'med_capacity': 1324},
                     {'region': 'Basilicata', 'regio_numb': 17, 'ICU_capacity': 88, 'med_capacity': 362},
                     {'region': 'Calabria', 'regio_numb': 18, 'ICU_capacity': 174, 'med_capacity': 967},
                     {'region': 'Campania', 'regio_numb': 15, 'ICU_capacity': 555, 'med_capacity': 3511},
                     {'region': 'Emilia-Romagna', 'regio_numb': 8, 'ICU_capacity': 889, 'med_capacity': 7920},
                     {'region': 'Friuli Venezia Giulia', 'regio_numb': 6, 'ICU_capacity': 175, 'med_capacity': 1277},
                     {'region': 'Lazio', 'regio_numb': 12, 'ICU_capacity': 943, 'med_capacity': 6421},
                     {'region': 'Liguria', 'regio_numb': 7, 'ICU_capacity': 217, 'med_capacity': 1703},
                     {'region': 'Lombardia', 'regio_numb': 3, 'ICU_capacity': 1530, 'med_capacity': 6369},
                     {'region': 'Marche', 'regio_numb': 11, 'ICU_capacity': 238, 'med_capacity': 966},
                     {'region': 'Molise', 'regio_numb': 14, 'ICU_capacity': 39, 'med_capacity': 176},
                     {'region': 'P.A. Bolzano', 'regio_numb': 21, 'ICU_capacity': 100, 'med_capacity': 500},
                     {'region': 'P.A. Trento', 'regio_numb': 22, 'ICU_capacity': 90, 'med_capacity': 517},
                     {'region': 'Piemonte', 'regio_numb': 1, 'ICU_capacity': 628, 'med_capacity': 5824},
                     {'region': 'Puglia', 'regio_numb': 16, 'ICU_capacity': 482, 'med_capacity': 2722},
                     {'region': 'Sardegna', 'regio_numb': 20, 'ICU_capacity': 204, 'med_capacity': 1602},
                     {'region': 'Sicilia', 'regio_numb': 19, 'ICU_capacity':861, 'med_capacity': 3620},
                     {'region': 'Toscana', 'regio_numb': 9, 'ICU_capacity': 570, 'med_capacity': 5033},
                     {'region': 'Umbria', 'regio_numb': 10, 'ICU_capacity': 84, 'med_capacity': 662},
                     {'region': "Valle d'Aosta", 'regio_numb': 2, 'ICU_capacity': 33, 'med_capacity': 83},
                     {'region': "Veneto", 'regio_numb': 5, 'ICU_capacity': 1000, 'med_capacity': 6000}
    ]



def get_ICUdata(region_numb):
    url = requests.get(url_total_update)
    text = url.text

    ICU_update_date = []
    ICU_update_value = []

    data = json.loads(text)
    for i in range(len(data)):
        if str(data[i]['codice_regione']) == str(region_numb):
            if data[i]['terapia_intensiva']:
                for l in range(len(ICU_Med_beds_capacity)):
                    if str(ICU_Med_beds_capacity[l]['regio_numb']) == str(region_numb):

                        ICU_percent = data[i]['terapia_intensiva'] /ICU_Med_beds_capacity[l]['ICU_capacity'] * 100

                        ICU_update_value.append(ICU_percent)

                        date_full = str(data[i]['data'])
                        date_new = date_full.replace('T', ' ')
                        date = datetime.strptime(date_new, '%Y-%m-%d %H:%M:%S')
                        ICU_update_date.append(date)

    df_ICU_percent = pd.DataFrame({'date': ICU_update_date, 'value': ICU_update_value})

    return df_ICU_percent

def get_medicaldata(region_numb):
    url = requests.get(url_total_update)
    text = url.text

    Med_update_date = []
    Med_update_value = []

    data = json.loads(text)
    for i in range(len(data)):
        if str(data[i]['codice_regione']) == str(region_numb):
            if data[i]['ricoverati_con_sintomi']:
                for l in range(len(ICU_Med_beds_capacity)):
                    if str(ICU_Med_beds_capacity[l]['regio_numb']) == str(region_numb):

                        med_percent= data[i]['ricoverati_con_sintomi'] /ICU_Med_beds_capacity[l]['med_capacity'] * 100

                        Med_update_value.append(med_percent)

                        date_full = str(data[i]['data'])
                        date_new = date_full.replace('T', ' ')
                        date = datetime.strptime(date_new, '%Y-%m-%d %H:%M:%S')
                        Med_update_date.append(date)

    df_med_percent = pd.DataFrame({'date': Med_update_date, 'value': Med_update_value})

    return df_med_percent

def change_color(region_numb):
    #Source: https://www.ticonsiglio.com/colori-regioni-regole-governo/

    df_total = total_data(region_numb)
    df_medical = get_medicaldata(region_numb)
    df_ICU = get_ICUdata(region_numb)

    df_rolweek = df_total.resample('W', on='date').mean()

    ## White zone
    if df_rolweek['value'].iloc[-1] < 50:
        color_zone = 'White'
    elif df_rolweek['value'].iloc[-1] >= 50 and df_ICU['value'].iloc[-1] <= 10 and df_medical['value'].iloc[-1] <= 15:
        color_zone = 'White'
    # elif df_rolweek['value'].iloc[-1] >= 50 and df_medical['value'].iloc[-1] <= 15:
    #     color_zone = 'White'

    ## Yellow zone
    # elif 50 < df_rolweek['value'].iloc[-1] <= 150 and 10 < df_ICU['value'].iloc[-1] < 20 and 15 < df_medical['value'].iloc[-1] < 30:
    #     color_zone = 'Yellow'
    elif df_rolweek['value'].iloc[-1] > 150 and 10 < df_ICU['value'].iloc[-1] <= 20:
        color_zone = 'Yellow'
    elif df_rolweek['value'].iloc[-1] > 150 and 15 < df_medical['value'].iloc[-1] <= 30:
        color_zone = 'Yellow'

    ## Orange zone
    elif df_rolweek['value'].iloc[-1] > 150 and 20 < df_ICU['value'].iloc[-1] < 30:
        color_zone = 'Orange'
    elif df_rolweek['value'].iloc[-1] > 150 and 30 < df_medical['value'].iloc[-1] < 40:
        color_zone = 'Orange'

    ## Red zone
    elif df_rolweek['value'].iloc[-1] > 150 and 30 < df_ICU['value'].iloc[-1]:
        color_zone = 'Red'
    elif df_rolweek['value'].iloc[-1] > 150 and 40 <= df_medical['value'].iloc[-1]:
        color_zone = 'Red'


    return color_zone
