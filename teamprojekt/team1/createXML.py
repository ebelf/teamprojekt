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

def create():
    matrikelnr_start = 922011                       # erste Matrikelnr. die vergeben wird
    # xml Dokument erzeugen
    document = Document()    
    # root Element erzeugen
    root = document.createElement("Studierende")
    document.appendChild(root)
    # child Elemente hinzufügen
    for i in range(10):                             # Anzahl der zu erzeugenden Studenten
        student = document.createElement("Student")
        student.setAttribute("id", str(i))
        root.appendChild(student)                   # Student dem root-Objekt hinzufügen
        # Matrikelnr. dem Student als child hinzufügen
        matrikel = document.createElement("Matrikelnr")
        student.appendChild(matrikel)
        matrikelnr = document.createTextNode(str(matrikelnr_start))
        matrikel.appendChild(matrikelnr)
        matrikelnr_start+=10                        # fortlaufende Matrikelnr., damit eindeutig
        # Nachname dem Student als child hinzufügen
        nachnameelem = document.createElement("Nachname")
        student.appendChild(nachnameelem)
        nachname = document.createTextNode(random.choice(list_nachname)) # Nachnamen zufällig aus Liste wählen
        nachnameelem.appendChild(nachname)
        # Vorname dem Student als child hinzufügen
        vornameelem = document.createElement("Vorname")
        student.appendChild(vornameelem)
        vorname = document.createTextNode(random.choice(list_vorname))  # Vorname zufällig aus Liste wählen
        vornameelem.appendChild(vorname)
        # Art der Anmeldung (PA/NA) dem Student als child hinzufügen
        anmeldung = document.createElement("Pflichtanmeldung")
        student.appendChild(anmeldung)
        pflichtanmeldung = document.createTextNode(random.choice(list_pflichtanmeldung))    # zufällige Auswahl PA oder NA
        anmeldung.appendChild(pflichtanmeldung)
        # 
        # Prioritäten für Seminare
        prioritaeten = [1,2,3]                  # Prioritäten die verwendet werden dürfen: unterschiedlich, entspr. der Anzahl der Seminare
        for j in range (1,4):                   # entsprechend der ID's der Seminare, beginnend mit ID=1
            seminar = document.createElement("Seminar")
            seminar.setAttribute("id", str(j))  # Seminar als Atrribut die ID vergeben
            student.appendChild(seminar)        # Seminar dem Studenten als child hinzufügen
            # dem Seminar eine Priorität vergeben
            l = random.choice(prioritaeten)     # Priorität zufällig auswählen
            prioritaet = document.createTextNode(str(l))
            seminar.appendChild(prioritaet)     # Priorität dem Seminar hinzufügen
            prioritaeten.remove(l)              # damit laut Vorgabe keine gleichen Prioritäten
        # Anmeldezeit dem Studenten als child hinzufügen       
        anmeldezeit = document.createElement("Anmeldezeitpunkt")
        student.appendChild(anmeldezeit)
        zeitpunkt = document.createTextNode(str(datetime.datetime(2015, random.randint(2,3), random.randint(1,28), random.randint(7,18), random.randint(1,59), random.randint(1,59))))
        anmeldezeit.appendChild(zeitpunkt)
    # Ausgabe
    # print xml # Ausgabe auf Konsole
    # print(document.toprettyxml(indent="    "))
    f = open("Studierende.xml", "w", encoding='utf-8')      # Ausgabe in Datei (Anm.: je nach Einstellung der Entwicklungsumgebung muss encoding='utf-8' entfernt werden und/oder der Datei-PATH geändert werden)
    document.writexml(f, "", "\t", "\n")
    f.close()
    
#g = create()