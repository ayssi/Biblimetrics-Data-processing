# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:00:53 2015
@author: ayssi
Ce script traite tout type de fichier log et crée par la suite un fichier CSV
"""
## Ezproxy Log : Outputs a file with these columns:
## Ip Address
## Session
## # Login
## date
## # URL
## ## ## Database
## ## ## DOI
## ## ## ISSN or ISBN
## ## ## Ressourc Type : TOC, Book or Article
## ## ## Ressourc Format : html, Pdf
## % Stat
## # Size


import os
import sys
import configparser
import re
import csv

output_csvfile = open("outurlsplit.csv", 'w', newline='')
headers=["IP Address","session","Login","date","Database","DOI","ISSN or ISBN","Resource type","Ressource format","Stat","Size"]
data = csv.writer(output_csvfile, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
print("les ligne du fichier sont de type :",type(data))
with open("test.csv") as f:
    f_csv = csv.reader(f, delimiter=';')
    next(f_csv, None) # skip the headers
    data.writerow(headers)
    i=0
    for row in f_csv:
        if re.match("eressources",row[i]):
            print ("cette ligne a été ignorée !")
            
        else:
            data.writerow(row)
        i +=i
