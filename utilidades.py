import requests
import random
import pandas as pd 
from tqdm import tqdm
from bs4 import BeautifulSoup
#from cred_here import YOUR_API_KEY
import json 
from tqdm import tqdm
import time
from datetime import datetime

import ast



# API del sitio https://api.opencagedata.com
API_KEY = ''

address = 'Ruezga Sur Sector 06 Bloque 06, Barquisimeto, Venezuela'

api_url = f'https://api.opencagedata.com/geocode/v1/geojson?q={address}&key={API_KEY}&pretty=1'


def deg_to_dec(degrees, minutes, seconds, pole):
    
    if pole == 'S' or pole == 'W':
        sign = -1
    else:
        sign = 1

    decimal = sign * (abs(degrees) + (minutes / 60.0) + (seconds / 3600.0))

    return decimal

def convertir (coordenada,tipo):
        
    coordenada = coordenada.replace("\'","").replace("°","").replace("'","").replace('"','').split(',')
    coord1 = coordenada[0].replace("'","").split(" ")
    valor = None
    if coord1 != 'NA' :
        if tipo == 'Latitud':
            valor = deg_to_dec(float(coord1[0]), float(coord1[1]), float(coord1[2]), coord1[3])
        else :
            valor = deg_to_dec(float(coord1[0]), float(coord1[1]), float(coord1[2]), coord1[3])
    else :
        valor = 'Empty'
    return float(valor)

def Get_Coords(address,YOUR_API_KEY):
    
    #url = f'https://geocode.search.hereapi.com/v1/geocode?q={address}&apiKey={YOUR_API_KEY}'
    url = api_url

    try : 
        
        response = requests.get(url).json()
        #CleanAddress = response['items'][0]['title'].upper()
        CleanAddress = address
        LAT = response['features'][0]['properties']['annotations']['DMS']['lat']
        LNG = response['features'][0]['properties']['annotations']['DMS']['lng']
        
        print(LAT + '\n' + LNG)
        results = [CleanAddress,convertir(LAT,'Latitud'),convertir(LNG,'Logitud')]
        
    except :
        
        results = ['Not Found','NA','NA']
        
    return results 

print(Get_Coords(address,API_KEY))


