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
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import status_codes
from datetime import datetime
from datetime import date
from openpyxl import Workbook
from openpyxl import load_workbook
from collections import Counter


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
##browser = mechanicalsoup.StatefulBrowser()
##browser.open("https://www.adnradio.cl/economia/2021/04/08/autoridad-sanitaria-confirmo-que-prohibicion-de-vender-y-hacer-delivery-de-productos-no-esenciales-se-termina-el-15-de-abril.html",verify=False)
##print(browser.get_url())

##url = browser.get_url()
##title = browser.get_current_page().find('title').text
##des = browser.get_current_page().find('meta',{'name':'description'})
##description = des["content"]

ds = pd.read_csv('dataset noticias falsas chilenas csv.csv', error_bad_lines=False, delimiter=";")
list_i=0
data=[]
while list_i<len(ds):
    print("Numero en el que va la lista= " + str(list_i))
    url = ds["Url"][list_i]
    title = ds["Titulo"][list_i]
    subtitle = ds["Subtitulo"][list_i]
    description = ds["Cuerpo"][list_i]
    has_title=1
    has_subtitle=1
    has_description=1
    
    if title == "":
        has_title=0
    if subtitle == "":
        has_subtitle=0
    if description =="":
        has_description=0
    
    titles_description = str(title) + " " + str(subtitle) + " " + str(description)
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url,verify=False)
    html = browser.get_current_page().text
    print(html)

    ##print(title)
    ##print(description)

    if "https" in url:
        print("El sitio esta verificado")
        url_verify = 1
    else:
        print("El sitio no esta verificado")
        url_verify = 0

    medios_verificados = ["the economist","public television","reuters","bbc","npr","pbs","the guardian","the wall street journal","los angeles times","the dallas morning news","chvnoticias","cnn","cnnchile","biobio","radiobiobio","latercera","adnradio","cooperativa","elmercurio"]
    i=0
    medio_verificado=0
    while i<len(medios_verificados):
        if medios_verificados[i] in html:
            medio_verificado = 1
            i=i+1
        else:
            i=i+1

    medios_no_verificados = ["occupy democrats","buzzfeed","breitbart","infowars","yahoo","huffpost","huffington post","the blaze","la legal","12 minutos","noticias tt","c5n","minuto uno","elinformadorchile","marca"]
    i=0
    medio_no_verificado=0
    while i<len(medios_no_verificados):
        if medios_no_verificados[i] in html:
            medio_no_verificado = 1
            i=i+1
        else:
            i=i+1

    impact_words = ["dictadura","pandemia","coronavirus","covid-19","covid","5g","cuarentena","ultimo minuto","control","muertes","mato","muerte","cancer","sida","vih","murio","fallecio","preocupante","alerta","comunismo","comunista","abusó","abusar","facista","asalto"]
    i=0
    impact_words_num=0
    while i<len(impact_words):
        if impact_words[i] in titles_description:
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
    ##
    ##i=0
    ##while i<len(impact_words):
    ##    if impact_words[i] in description:
    ##        impact_words_num = impact_words_num + 1
    ##        i=i+1
    ##    else:
    ##        i=i+1
        
    ###### Corrector Ortografico
    def words(text): return re.findall(r'\w+', text.lower())

    WORDS = Counter(words(open('spanish.txt').read()))

    def P(word, N=sum(WORDS.values())): 
        "Probability of `word`."
        return WORDS[word] / N

    def correction(word): 
        "Most probable spelling correction for word."
        return max(candidates(word), key=P)

    def candidates(word): 
        "Generate possible spelling corrections for word."
        return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

    def known(words): 
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in WORDS)

    def edits1(word):
        "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in edits1(word) for e2 in edits1(e1))


    subtitle_1_1 = titles_description.replace(",","")
    subtitle_1_2 = subtitle_1_1.replace(".","")
    subtitle_1_3 = subtitle_1_2.replace("'","")
    subtitle_1_4 = subtitle_1_3.replace('“',"")
    subtitle_1_5 = subtitle_1_4.replace('”',"")
    subtitle_1_6 = subtitle_1_5.replace('-',"")
    subtitle_1_7 = subtitle_1_6.replace(':',"")
    subtitle_1_8 = subtitle_1_7.replace(';',"")
    subtitle_2 = subtitle_1_8.replace('"',"")
    ##subtitle_corregido = correction(subtitle_2)
    subtitle_split = subtitle_2.split()
    i=0
    while i<len(subtitle_split):
        subtitle_split[i] = subtitle_split[i].lower()
        i=i+1
    ##if subtitle == subtitle_corregido:
    ##    faltas_ortograficas = 0
    ##else:
    ##    faltas_ortograficas = 1

    i=0
    contador_faltas_ortograficas = 0
    faltas_ortograficas_lista = []
    while i<len(subtitle_split):
        palabra_correccion = correction(subtitle_split[i])
        if subtitle_split[i] == palabra_correccion:
            i=i+1
        else:
            contador_faltas_ortograficas = contador_faltas_ortograficas + 1
            faltas_ortograficas_lista.append(subtitle_split[i])
            i=i+1
            
    i=0

    #while i<len(faltas_ortograficas_lista):
    #    print(faltas_ortograficas_lista[i])
    #    i=i+1

    print("Url_verify= " + str(url_verify))
    print("Impact_words_num= " + str(impact_words_num))
    print("Contador_faltas_ortograficas= " + str(contador_faltas_ortograficas))
    print("Medio verificado= " + str(medio_verificado))
    print("Medio no verificado= " + str(medio_no_verificado))
    print("Tiene Titulo= "+ str(has_title))
    print("Tiene Subtitulo= "+ str(has_subtitle))
    print("Tiene Cuerpo= "+ str(has_description))
    print("Veracidad= "+ str(ds["Veracidad"][list_i]))
    data_line = str(url) + "," + str(url_verify) + "," + str(has_title) + "," + str(has_subtitle) + "," + str(has_description) + "," + str(medio_verificado) + "," + str(medio_no_verificado) + "," +  str(impact_words_num) + "," +  str(contador_faltas_ortograficas) + "," + str(ds["Veracidad"][list_i])
    data.append(data_line)
    list_i=list_i+1


    
i=0
while i<len(data):
    print(data[i])
    i=i+1

header = ['Url','Url Verify','Tiene Title','Tiene Subtitle','Tiene Description','Medio Confiable','Medio No Confiable','Impact Words Count','Faltas Ortograficas','Veracidad']

with open('dataset noticias falsas chilenas procesadas.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file,dialect='excel')
    writer.writerow(header)
    for item in data:
        writer.writerow([item])
    file.close()
        

