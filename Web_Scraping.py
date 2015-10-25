# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:25:42 2015
@author: Adolfo Sanz Anchelergues

TGINE: Web Scraping de página de valores bursátiles
"""
# IMPORTACIONES
import requests # Paquete para importar contenido
from bs4 import BeautifulSoup # Paquete para el parseo de información
import time # Paquete para introducir retardo
import pandas as pd # Biblioteca para la manipulación y análisis de datos

# DEFINICIÓN DE VARIABLES
# URL origen de información
URL="http://www.invertia.com/mercados/bolsa/indices/ibex-35/acciones-ib011ibex35"
# Opciones del menú
items = ["ESCRITURA POR PANTALLA","ESCRITURA A ARCHIVO","MONITORIZAR VALOR"]

# FUNCIONES
# Función de lectura de importación de los datos
def traer_URL():    
    pagina = requests.get(URL)
    return pagina

# Función de parseo
def parseo(pagina):
    soup = BeautifulSoup(pagina.text)
    valor=soup.find('table',{'title':'Acciones'})
    trs = valor.findAll('tr')
    ibex=[]    
    for cada_tr in range(len(trs)):
        Fila=[]
        if cada_tr==0: #La fila de cabecera tiene los títulos de cada columna
            ths=trs[cada_tr].findAll('th')
            for cada_th in range(len(ths)):
                if cada_th != 4: #El quinto valor está vacío
                    th_corr = ths[cada_th].text.replace("\n","")
                    Fila.append(th_corr)
        else:
            tds = trs[cada_tr].findAll('td')
            for cada_td in range(len(tds)):
                if cada_td != 4:
                    Fila.append(tds[cada_td].text)
        ibex.append(Fila)
    texto=pd.DataFrame(ibex[1:], index=None, columns=ibex[0])
    
    return texto

# Función de escritura a fichero
def escribe_fichero(contenido):
    nombre_fichero=input("Introduzca el nombre del fichero: ")
    nombre_fichero = nombre_fichero + ".csv" # Convertimos a csv
    contenido.to_csv(nombre_fichero)
    print("Fichero "+nombre_fichero+" guardado"+"\n")

# Función de obtención de datos de un valor
def parseo_valor(codigo):
    texto=parseo(traer_URL())
    for sigla in range(len(texto)):
        if texto.ix[sigla]["TKR*"] == codigo:
            print(texto.ix[sigla:sigla])
            return True
        
    print("No existe el valor "+codigo)
    return False

# main
print("--Web scrapting de valores bursátiles--\n")
print("Seleccione el modo de operación:\n")

# Bucle de elección de opciones del menú
running = True
while running: 
    opcion = 1 
    for eleccion in items: # Bucle para crear el menú
        print(str(opcion) + ". " + eleccion) 
        opcion = opcion + 1 
    print(str(opcion) + ". SALIR") 
 
    eleccion = int(input("Seleccione una opción: "))
    if eleccion == opcion: 
        running = False 
    else:
        if eleccion == 1: # Escritura por pantalla
            datos=parseo(traer_URL())
            print(datos)
        
        elif eleccion == 2: # Escritura a fichero csv
            datos=parseo(traer_URL())
            escribe_fichero(datos)

        elif eleccion == 3: # Monitorización de valor bursátil
            valor_estudiar = input("Escriba la sigla de un valor bursátil: ")
            retardo = int(input("Introduzca intervalo de sondeo (en segundos): "))
            print("Pulse CTRL+C para interrumpir")            
            try:            
                while parseo_valor(valor_estudiar):            
                    time.sleep(retardo)
            except KeyboardInterrupt:
                pass
        elif eleccion == 4:
            pass
        else:
            print("Opción incorrecta. Seleccione de nuevo")
