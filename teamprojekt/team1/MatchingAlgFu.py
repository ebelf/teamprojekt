import datetime

# Praeferenzlisten der Studierenden
#PSt_ = [Praeferenz, Seminarnr.]

PSt1 = [[3,1],[2,2],[1,3]]
PSt2 = [[3,1],[1,2],[2,3]]
PSt3 = [[1,1],[2,2],[3,3]]
PSt4 = [[1,1],[3,2],[2,3]]
PSt5 = [[2,1],[1,2],[3,3]]

PSt = [PSt1, PSt2, PSt3, PSt4, PSt5]    #Liste der Praeferenzlisten

#Input-Daten der Studierenden
DSt1 = [datetime.datetime(2015, 3, 1, 12, 59, 23),'NA']
DSt2 = [datetime.datetime(2015, 3, 1, 12, 31, 3), 'NA']
DSt3 = [datetime.datetime(2015, 4, 2, 10, 59, 23),'PA']
DSt4 = [datetime.datetime(2015, 3, 5, 12, 40, 33),'NA']
DSt5 = [datetime.datetime(2015, 3, 6, 10, 59, 20),'PA']

DSt = [DSt1, DSt2, DSt3, DSt4, DSt5]    #Liste mit Input-Daten

#Seminarliste mit Anzahl der Plaetze
Sem = [2,2,1]



def matching(PSt, DSt, Sem):
    Res = [set() for i in range(len(Sem))]              # Ergebnisliste leer anlegen, set() fuer Anzahl der Seminare
    matchStud = [False for i in range(len(PSt))]        # gibt an, welcher Studierende einen Platz erhalten hat; initialisiert mit False
    while  False in matchStud:                          # Algorithmus laeuft, solange es noch Studierende ohne Seminarplatz gibt (und deren Praeferenzliste nicht leer ist)
        for i in range(0, len(matchStud)):
            if matchStud[i] == True:                    # wenn der Studierende einen Platz hat (True), muss er nicht weiter beachtet werden
                pass
            else:                                       # anderenfalls, wenn er noch keinen Platz hat, aber ...
                if not PSt[i]:                          # seine Praeferenzliste leer ist / erschoepfend behandelt wurde, kann er keinen Platz mehr erhalten
                    matchStud[i] = True                 # wird auf True gesetzt, damit der Algorithmus terminieren kann
                else:                                   # Ist seine Praeferenzliste nicht leer ...
                    maxp = max(PSt[i])[1]               # wird in maxp die Seminar-ID des Seminars mit der hoechsten Praeferenz gespeichert, z.B. [3, 1] --> 1
                    if Sem[maxp-1]>0:                   # wenn es noch freie Seminarplaetze im Seminar mit der hoechsten Praeferenz gibt
                        Res[maxp-1].add(i)              # wird der Studierende eingetragen
                        Sem[maxp-1] -= 1                # die Anzahl der Plaetze im Seminar um 1 reduziert
                        matchStud[i] = True             # sein Wert auf True gesetzt
                    else:                               # keine freien Plaetze mehr:
                        for z in Res[maxp-1]:           # Vergleich mit den Studierenden, die schon einen Platz haben                 
                            if 'PA' in DSt[i] and 'PA' not in DSt[z]:   # Anfragender 'PA' und Studierender im Seminar nicht 'PA'
                                matchStud[z] = False                    # Studierender im Seminar verliert seinen Platz ...
                                Res[maxp-1].remove(z)                   # wird aus Ergebnismenge geloescht
                                Res[maxp-1].add(i)                      # anfragender Studierender wird eingetragen      
                                matchStud[i] = True                     # sein Wert auf True gesetzt
                                break                                   # er hat einen Platz und muss keine weiteren Vergleiche machen   
                            if 'PA' not in DSt[i] and 'PA' in DSt[z]:   # Anfragender nicht 'PA' und Studierender im Seminar 'PA'
                                pass                                    # anfragender Studierender erhaelt den Platz nicht
                            else:                                       # beide gleiche Werte --> Praeferenzen als naechstes Kriterium ueberpruefen
                                if  max(PSt[i])[0] > max(PSt[z])[0]:    # anfragender Studierender hat hoehere Praeferenz fuer das Seminar als Studierender, der Platz im Seminar hat
                                    matchStud[z] = False                # analog zu oben
                                    Res[maxp-1].remove(z)               
                                    Res[maxp-1].add(i)                            
                                    matchStud[i] = True
                                    break    
                                elif max(PSt[i])[0] == max(PSt[z])[0]:      # Timestamp als naechstes Kriterium pruefen, wenn Prioritaeten fuer das Seminar gleich sind
                                    if DSt[i][0]<DSt[z][0]:                 # anfragender Studierender hat sich frueher fuer das Seminar angemeldet als Studierender, der Platz im Seminar hat
                                        matchStud[z] = False                # analog zu oben
                                        Res[maxp-1].remove(z)
                                        Res[maxp-1].add(i)
                                        matchStud[i] = True
                                        break
                        if matchStud[i]==False:                         # alle Versuche einen Seminarplatz in diesem Seminar zu erlangen erfolglos
                            PSt[i].remove(max(PSt[i]))                  # Seminar wird aus Praeferenzliste des Studierenden entfernt
    return Res
f = matching(PSt, DSt, Sem)
print(f)