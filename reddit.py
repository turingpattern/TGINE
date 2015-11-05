import praw
import datetime #https://docs.python.org/2/library/datetime.html#datetime-objects


import xml.etree.ElementTree as ET
#import os

my_user_agent="windows:www.usc.es:TGINE:v1.0 (by /u /pailroco)"
my_sub_reddit="nosleep"
limite=2
nombre_fichero="000_reddit_test.txt"
fichero = open(nombre_fichero, 'a')

#def escribe_reddit(contenido):
#    fichero = open(nombre_fichero, 'a')
#    fichero.write(contenido+"\n")

#def lee_xml(arbol):
    #tree = ET.parse('country_data.xml')
    #doc_xml = ET.fromstring(submission)  

r = praw.Reddit(user_agent=my_user_agent)
r.config.store_json_result=True #Revisar
subreddit = r.get_subreddit(my_sub_reddit)
#get.last
for submission_hot in subreddit.get_hot(limit = limite):
    print("Title: "+submission_hot.title)
    print("Text: "+submission_hot.selftext)
    print("Score: "+"%d" % submission_hot.score)
    print("---------------------------------\n")
    fichero.write(submission_hot.title+"\n")
print(submission_hot.json_dict)

raiz = ET.Element(submission_hot.title)
contenido = ET.SubElement(raiz, submission_hot.selftext)
fecha = ET.SubElement(raiz, datetime.fromtimestamp(submission_hot.created_utc).isoformat())
#tipo = ET.SubElement(raiz, submission_hot.)

#print(json_dict)
fichero.close


#https://praw.readthedocs.org/en/stable/pages/code_overview.html#praw.objects.Comment.submission


#XML
#https://docs.python.org/3.4/library/xml.etree.elementtree.html#building-xml-documents
#https://pymotw.com/2/xml/etree/ElementTree/create.html#serializing-xml-to-a-stream
