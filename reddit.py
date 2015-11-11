import praw
import datetime #https://docs.python.org/2/library/datetime.html#datetime-objects
import xml.etree.ElementTree as ET


my_user_agent="windows:www.usc.es:TGINE:v1.0 (by /u /pailroco)"
my_sub_reddit="sport"
limite=10
nombre_fichero="004_reddit_test.xml"
print("Antes de escribir")
fichero = open(nombre_fichero, 'wb') # Debe ser ab, comprobar 

#def escribe_reddit(contenido):
#    fichero = open(nombre_fichero, 'a')
#    fichero.write(contenido+"\n")

#def lee_xml(arbol):
    #tree = ET.parse('country_data.xml')
    #doc_xml = ET.fromstring(submission)  

r = praw.Reddit(user_agent=my_user_agent)
r.config.store_json_result=True #Revisar
subreddit = r.get_subreddit(my_sub_reddit)
#top = subreddit.get_new(limite) REVISAR
#ultimos =subreddit.get_last(limite) #get.last REVISAR

raiz = ET.Element('Aportes')
#comentario = ET.Comment('TGINE-Reddit')
#raiz.append(comentario)

for submission_hot in subreddit.get_hot(limit = limite):
    dicc={
    'id':submission_hot.id,
    'titulo':submission_hot.title,
    'fecha':datetime.datetime.fromtimestamp(submission_hot.created_utc).isoformat(),
    'texto':submission_hot.selftext
    }
    sub_elemento=ET.SubElement(raiz,'Submission',dicc)
    #sub_elemento.text = str(submission_hot.title) + ': ' + str(submission_hot.selftext )

ET.ElementTree(raiz).write(fichero, method='xml')
    #print("Title: "+submission_hot.title)
    #print("Text: "+submission_hot.selftext)
    #print("Score: "+"%d" % submission_hot.score)
    #print("---------------------------------\n")
    #fichero.write(submission_hot.title+"\n")
print(submission_hot.json_dict)


corpus=[]


fichero.close()


#https://praw.readthedocs.org/en/stable/pages/code_overview.html#praw.objects.Comment.submission


#XML
#https://docs.python.org/3.4/library/xml.etree.elementtree.html#building-xml-documents
#https://pymotw.com/2/xml/etree/ElementTree/create.html#serializing-xml-to-a-stream



#vec.get_feature_names()
