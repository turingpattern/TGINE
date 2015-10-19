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
import pandas as pd

# DEFINICIÓN DE VARIABLES
# URL origen de información
URL="http://www.invertia.com/mercados/bolsa/indices/ibex-35/acciones-ib011ibex35"
# Intervalo de sondeo (en segundos)
retardo = 0.5
# Opciones del menú
items = ["ESCRITURA POR PANTALLA","ESCRITURA A ARCHIVO","MONITORIZAR VALOR"]

# FUNCIONES
# Función de lectura de importación de los datos
def traer_URL():
    global pagina 
    pagina = requests.get(URL)
    return pagina

# Función de parseo
def parseo():
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

def parseo_valor(codigo):
    texto=parseo()
    #id="TKR*"
    for sigla in range(len(texto)):
        if texto.ix[sigla]["TKR*"] == codigo:
            print("{0}".format(texto.ix[sigla:sigla]))
            return True
        
    print("No existe el valor "+codigo)
    return False

# Función de escritura a fichero
def escribe_fichero(contenido):
    nombre_fichero=input("Introduzca el nombre del fichero: ")
    nombre_fichero = nombre_fichero + ".csv"
    contenido.to_csv(nombre_fichero)

# Función de selección de valor

# main
print("--Web scrapting de valores bursátiles--")
print("\n")
print("Seleccione el modo de operación")
print("\n")

running = True
while running: 
    opcion = 1 
    for eleccion in items: 
        print(str(opcion) + ". " + eleccion) 
        opcion = opcion + 1 
    print(str(opcion) + ". SALIR") 
    eleccion = int(input("Seleccione una opción: "))
    if eleccion == opcion: 
        running = False 
    else:
        if eleccion == 1:
            traer_URL()
            datos=parseo()
            print(datos)
        
        elif eleccion == 2:
            traer_URL()
            datos=parseo()
            escribe_fichero(cont)
            
        elif eleccion == 3:
            valor_estudiar = input("Seleccione un valor: ")            
            print("Monitorizando valor: "+valor_estudiar)
            while 1:            
                try:
                    time.sleep(retardo)
                    traer_URL()
                    parseo_valor(valor_estudiar)
                except KeyboardInterrupt:
                    break
                        
        elif eleccion == 4:
            break
        else:
            print("Opción incorrecta. Seleccione de nuevo")
