# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:08:41 2015

@author: Adolfo
"""

import praw
import os

my_user_agent="TGINE:v1.0 by /u /pailroco"
my_sub_reddit="science"
limite=25
nombre_fichero="reddit_test.txt"
fichero = os.open(nombre_fichero, os.O_CREAT)#os.O_APPEND)

#def escribe_reddit(contenido):
#    fichero = os.open('nombrefich.txt','a')
#    fichero.write(contenido)

r = praw.Reddit(user_agent=my_user_agent)

subreddit = r.get_subreddit(my_sub_reddit)

for submission in subreddit.get_hot(limit = limite):
    print("Title: "+submission.title)
    print("Text: "+submission.selftext)
    print("Score: "+"%d" % submission.score)
    print("---------------------------------\n")
    os.write(fichero, submission.title)

os.close(fichero)

