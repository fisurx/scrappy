# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#route
url = "http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx"

page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")

#get
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})

name=""
price=""
nroFila=0
for fila in tabla.find_all("tr"):
    if nroFila==1:
        nroCelda=0
        for celda in fila.find_all('td'):
            if nroCelda==0:
                name=celda.text
                print("Indice:", name)
            if nroCelda==2:
                price=celda.text
                print("Valor:", price)
            nroCelda=nroCelda+1
    nroFila=nroFila+1

with open('bolsa.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])