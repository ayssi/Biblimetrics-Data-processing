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
## % Stat
## # Size


import os
import sys
import configparser
import csv

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')
PATH = CONFIG ['DEFAULT']['CFG_PATHDIR']
PATHDATA = CONFIG ['DEFAULT']['CFG_PATHDIR_DATA']

#CSVFILE = CONFIG['DEFAULT']['CSVFILE']

def cleanLine(s):
    s = s.strip()
    s = s.strip('\t')
    s = s.replace('[', '"')
    s = s.replace(']', '"')
    #s = s.replace(']\r', '') #Retour en début de ligne
    #s = s.replace('\n', '') #Saut de ligne
    #s = s.replace('\n\r', '') #saut de ligne sous Windows
    s = s.replace('\t', '') # #tabulation horizontale
    s = s.replace('\f', '') #saut de page
    return s
     
    
def cleanFile (source,destination):
    dest = open(destination,'w')
    lines = dest.write("\"IP Address\" session Login date URL Stat Size\n")
    with open(source) as f:
       for line in f :
           lines = cleanLine(line)
           lines = lines + "\n"
           if lines != '\n': dest.write(lines)
    dest.close()             

def log2csv(CLEANFILE,CSVFILE):
    output_csvfile = open(CSVFILE, 'w', newline='')
    data = csv.writer(output_csvfile, delimiter=';')
    with open(CLEANFILE) as f:
        f_csv = csv.reader(f, delimiter=' ')
        #headers = next(f_csv)
        #for row in f_csv: data.writerow(next(f_csv)
        data.writerow(next(f_csv))
        for row in f_csv:
            data.writerow(row)


if (__name__) == '__main__':
    if len(sys.argv) != 4:
        print("Erreur : Il vous faut deux arguments (Fichier source et destination) !")
    else:
        INPUTFILE = PATHDATA + sys.argv[1] #must be a .log file
        OUTPUTFILE = PATHDATA + sys.argv[2] #must be a text file
        CSVFILE = PATHDATA + sys.argv[3]
        if os.path.exists(INPUTFILE) and os.path.exists(OUTPUTFILE):
            cleanFile(INPUTFILE,OUTPUTFILE)
            log2csv(OUTPUTFILE,CSVFILE)
        else:
            print ("le fichier",INPUTFILE,"ou le fichier",OUTPUTFILE , "n'existe pas !")
            #print (PATHDATA + sys.argv[3])
        
