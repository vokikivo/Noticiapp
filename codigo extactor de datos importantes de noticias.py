#Importacion de bibliotecas a usar
import requests
import string
import mechanicalsoup
from datetime import datetime, timedelta
import time
import re
import socket
import sys
import openpyxl
import os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import status_codes
from datetime import datetime
from datetime import date
from openpyxl import Workbook
from openpyxl import load_workbook


###################################

#import matplotlib.pyplot as plt
#import matplotlib as mpl
import pandas as pd
#import pylab as pl
import numpy as np
#import seaborn as sns
#import IPython as ipy

from pandas import ExcelFile
from pandas import ExcelWriter

#import datetime as dts
#mpl.style.use('ggplot') #ggplot-like style
#%matplotlib inline


##### Extracción

#Login en login.digicoldchain.com
##browser = mechanicalsoup.StatefulBrowser()
##browser.open("https://www.adnradio.cl/economia/2021/04/08/autoridad-sanitaria-confirmo-que-prohibicion-de-vender-y-hacer-delivery-de-productos-no-esenciales-se-termina-el-15-de-abril.html",verify=False)
##print(browser.get_url())

##url = browser.get_url()
##title = browser.get_current_page().find('title').text
##des = browser.get_current_page().find('meta',{'name':'description'})
##description = des["content"]

url ="https://www.radioagricultura.cl/politica/2021/04/08/camara-de-diputados-discutira-la-proxima-semana-el-proyecto-que-busca-un-tercer-retiro-del-10.html"
title = "Cámara de Diputados discutirá la próxima semana el proyecto que busca un tercer retiro del 10%"
subtitle = ""
description = "Durante esta jornada, el presidente de la Comisión de Constitución de la Cámara de Diputados, Marcos Ilabaca, dio a conocer que el proyecto que busca un tercer retiro de los fondos de las AFP será analizado en particular dentro de la próxima semana, en conjunto con la iniciativa del impuesto a los denominados “súper ricos”. El parlamentario detalló que el martes 13 de abril se discutirá en particular la iniciativa que busca un tercer retiro de ahorros previsionales, agregando que espera que sea despachada durante esta jornada. Por su parte, el diputado Raúl Soto (PPD) comunicó que, tras una reunión de los comités de partidos de la Cámara Baja, se llegó a un acuerdo para que la propuesta sea analizada el próximo miércoles 14 y jueves 15 de abril en Sala. “En reunión de comités parlamentarios fue acogida nuestra solicitud de dar urgencia y prioridad a la iniciativa, por lo que será analizada en la Sala el miércoles 14 y jueves 15 de abril”, detalló Soto. Junto a esto, aseveró que “es una buena noticia para millones de chilenos y chilenas que están esperando urgentemente esta medida“. En tanto, ratificó que la iniciativa que busca aplicar un impuesto a los “súper ricos” será analizada en particular en la Comisión de Constitución de la Cámara el miércoles 14 de abril."
##print(title)
##print(description)

if "https" in url:
    print("El sitio esta verificado")
    url_verify = 1
else:
    print("El sitio no esta verificado")
    url_verify = 0

impact_words = ["dictadura","pandemia","coronavirus","covid-19","cuarentena","ultimo minuto","control","muertes","muerte","murio","fallecio","preocupante","alerta"]
i=0
impact_words_num=0
while i<len(impact_words):
    if impact_words[i] in title:
        impact_words_num = impact_words_num + 1
        i=i+1
    else:
        i=i+1

##i=0
##while i<=len(impact_words):
##    if impact_words[i] in subtitle:
##        impact_words_num = impact_words_num + 1
##        i=i+1
##    else
##        i=i+1

i=0
while i<len(impact_words):
    if impact_words[i] in description:
        impact_words_num = impact_words_num + 1
        i=i+1
    else:
        i=i+1

print(url_verify)
print(impact_words_num)
    


