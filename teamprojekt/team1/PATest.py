#from readXML import DSt

#ergebnis = [{1,4,2},{8,9},{3,6}]

#===============================================================================
# ueberprueft, ob alle pflichtangemeldeten Studierenden einen Platz erhalten haben
#===============================================================================

def makeOneSet(ergebnis):           # Schreibt zur besseren Suche alle Studierenden im Ergebnis in ein set 
    oneSet = set()
    for sem in ergebnis:
        for st in sem:
            oneSet.add(st)
    return oneSet

def AllPAinErg(ergebnis, DSt):
    notInErg = set()
    allStudInErg = makeOneSet(ergebnis)
    for anm in range(len(DSt)):             # durchlaeuft die Liste DSt 
        if DSt[anm][1] == 'PA':             # und schreibt den Studierenden in notInErg wenn er pflichtangemeldet (PA) ist
            if anm not in allStudInErg:     # und er nicht im Ergebnis vorkommt
                notInErg.add(anm)
    if notInErg == set():
        return ("Alle pflichtangemeldeten Studierenden haben im Matching-Ergebnis einen Platz erhalten.")
    elif len(notInErg) == 1:
        return ("Der pflichtangemeldete Studierende mit der ID", notInErg, "hat im Matching-Ergebnis keinen Platz erhalten.")
    else:
        return ("Die pflichtangemeldeten Studierenden mit den IDs", notInErg, "haben im Matching-Ergebnis keinen Platz erhalten.")