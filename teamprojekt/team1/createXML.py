#!/usr/bin/env python
# -*- coding: utf8 -*-

#===============================================================================
# Datei zum Erzeugen von XML-Input-Beispieldaten
# 
# 
# 
#===============================================================================
from xml.dom.minidom import Document
import random
import datetime

#Beispieldaten aus denen zufällig ausgewählt wird
list_nachname = ["Müller", "Meier", "Schulz", "Schneider", "Fischer", "Webel"]
list_vorname = ["Stefan", "Joachim", "Mike", "Luisa", "Matthias", "John", "Anna", "Luca", "Rico", "Martin"]
list_pflichtanmeldung = ["PA", "NA"]
matrikelnr_start = 922011

# create xml document
document = Document()

# create root element
root = document.createElement("Studierende")
document.appendChild(root)

# create child element
for i in range(10):                             # Anzahl der zu erzeugenden Studenten
    student = document.createElement("Student")
    student.setAttribute("id", str(i))
    root.appendChild(student)

    matrikel = document.createElement("Matrikelnr")
    student.appendChild(matrikel)
    matrikelnr = document.createTextNode(str(matrikelnr_start))
    matrikel.appendChild(matrikelnr)
    matrikelnr_start+=10
    
    nachnameelem = document.createElement("Nachname")
    student.appendChild(nachnameelem)
    nachname = document.createTextNode(random.choice(list_nachname))
    nachnameelem.appendChild(nachname)
    
    vornameelem = document.createElement("Vorname")
    student.appendChild(vornameelem)
    vorname = document.createTextNode(random.choice(list_vorname))
    vornameelem.appendChild(vorname)
    
    anmeldung = document.createElement("Pflichtanmeldung")
    student.appendChild(anmeldung)
    pflichtanmeldung = document.createTextNode(random.choice(list_pflichtanmeldung))
    anmeldung.appendChild(pflichtanmeldung)
    
    #Prioritäten für Seminare
    prioritaeten = [1,2,3]                  # Prioritäten die verwendet werden dürfen
    for j in range (1,4):
        seminar = document.createElement("Seminar")
        seminar.setAttribute("id", str(j))
        student.appendChild(seminar)
        
        l = random.choice(prioritaeten)
        prioritaet = document.createTextNode(str(l))
        seminar.appendChild(prioritaet)
        prioritaeten.remove(l)              # hier als Bsp. keine gleichen Prioritäten
           
    anmeldezeit = document.createElement("Anmeldezeitpunkt")
    student.appendChild(anmeldezeit)
    zeitpunkt = document.createTextNode(str(datetime.datetime(2015, random.randint(2,3), random.randint(1,28), random.randint(7,18), random.randint(1,59), random.randint(1,59))))
    anmeldezeit.appendChild(zeitpunkt)

# print created xml
# print(document.toprettyxml(indent="    "))
f = open("Studierende.xml", "w", encoding='utf-8')
document.writexml(f, "", "\t", "\n")
f.close()