#!/usr/bin/python

#Datei zum Lesen der Input-XML-Datei und Umwandeln der Daten fuer den Algorithmus

inputfile = 'studierende.xml'

PSt = []
DSt = []
    
import datetime
import xml.dom.minidom
    

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse(inputfile)
collection = DOMTree.documentElement

# Get all the students in the collection
students = collection.getElementsByTagName("Student")


for student in students:
    Std = []
    Dst1 = []
    seminars = student.getElementsByTagName("Seminar")
    for seminar in seminars:
        Seminar = []
        Seminar.append(int(seminar.childNodes[0].data))         # Prioriaet fuer das Seminar
        Seminar.append(int(seminar.getAttribute("id")))         # Seminar-ID
        Std.append(Seminar)
    PSt.append(Std)
    date = student.getElementsByTagName("Anmeldezeitpunkt")[0].childNodes[0].data
    dateConvert = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")     # Umwandeln in datetime-Objekt
    Dst1.append(dateConvert)
    Dst1.append(student.getElementsByTagName("Pflichtanmeldung")[0].childNodes[0].data)
    DSt.append(Dst1)
#print(PSt)
#print(DSt)