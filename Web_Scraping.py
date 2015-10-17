# IMPORTACIONES
# Paquete para importar contenido
import requests
# Paquete para el parseo de información
from bs4 import BeautifulSoup
# Paquete para introducir retardo
import time

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
def parseo(pagina):
    soup = BeautifulSoup(pagina.text)
    valor=soup.find('table',{'title':'Acciones'})
    tbody=valor.find('tbody')
    trs = tbody.findAll('tr')
    print('\n')
    texto=''
    for cada_tr in trs:
        tds = cada_tr.findAll('td')
        for cada_td in tds:
            texto=texto + cada_td.text + '\t'
            texto=texto + '\n'
    return texto

# Función de escritura a fichero
def escribe_fichero(contenido):
    with open("valores.txt", "w") as fvalores:
        fvalores.write(contenido)

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
            print(parseo(pagina))
        
        elif eleccion == 2:
            traer_URL()
            cont=parseo(pagina)
            escribe_fichero(cont)
            
        elif eleccion == 3:
            valor_estudiar = input("Seleccione un valor: ")            
            print("Monitorizando valor: "+valor_estudiar)
            while 1:            
                try:
                    time.sleep(retardo)
                    traer_URL()
                    cont=parseo(pagina)
                except KeyboardInterrupt:
                    break
                        
        elif eleccion == 4:
            break
        else:
            print("Opción incorrecta. Seleccione de nuevo")
