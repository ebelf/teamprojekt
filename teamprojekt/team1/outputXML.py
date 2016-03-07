# -*- coding: utf8 -*-
#from start import f    # todo: später soll das Erg. automatisch umgewandelt werden

#===============================================================================
# Datei zum Umwandeln des Matching-Ergebnisses in XML-Output-Daten
#===============================================================================

#erg = [{0, 9, 5, 6}, {2, 3}, {1, 4}]    # als Bsp.
def output(f):
    erg = f
    
    inputfile = 'studierende.xml'
    
    from xml.dom.minidom import Document
    import xml.dom.minidom
    
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse(inputfile)
    collection = DOMTree.documentElement
    
    # Get all the students in the collection
    studenten = collection.getElementsByTagName("Student")
    
    
    # create xml document
    document = Document()
    
    # create root element
    root = document.createElement("Seminarzuordnung")
    document.appendChild(root)
    
    for i in range(1,len(erg)+1):
        seminar = document.createElement("Seminar")
        seminar.setAttribute("id", str(i))
        root.appendChild(seminar)
    
        titel = document.createElement("Seminartitel")
        seminar.appendChild(titel)
        thema = document.createTextNode("Titel/Thema des Seminars")
        titel.appendChild(thema)
        
        dozent = document.createElement("Dozent")
        seminar.appendChild(dozent)
        prof = document.createTextNode("Name des Dozenten")
        dozent.appendChild(prof)
        
        plaetze = document.createElement("Seminarplaetze")
        seminar.appendChild(plaetze)
        anzahl = document.createTextNode(str(len(erg[i-1])))
        plaetze.appendChild(anzahl)
    
        #Teilnehmer
        teilnehmer = document.createElement("Teilnehmer")
        seminar.appendChild(teilnehmer)
        
        for j in (erg[i-1]):
            for k in studenten:
                attr = k.getAttribute("id")
                if int(attr) == int(j):
                    student = document.createElement("Student")
                    matrikeloutp = k.getElementsByTagName("Matrikelnr")
                    student.setAttribute("matrikelnr", str(matrikeloutp[0].childNodes[0].data))
                    teilnehmer.appendChild(student)
                    nachname = document.createElement("Nachname")
                    student.appendChild(nachname)
                    nachnameoutp = k.getElementsByTagName("Nachname")
                    nachnameoutput = document.createTextNode(str(nachnameoutp[0].childNodes[0].data))
                    nachname.appendChild(nachnameoutput)
                    vorname = document.createElement("Vorname")
                    student.appendChild(vorname)
                    vornameoutp = k.getElementsByTagName("Vorname")
                    vornameoutput = document.createTextNode(str(vornameoutp[0].childNodes[0].data))
                    vorname.appendChild(vornameoutput)
                    break
    
    
    # Ausgabe auf Konsole    # todo: später Ausgabe in Datei
    # print created xml
    # print(document.toprettyxml(indent="    "))
    z = document.toprettyxml(indent="    ")
    print(z)
    f = open("Ergebnis.xml", "w")
    document.writexml(f, "", "\t", "\n")
    f.close()