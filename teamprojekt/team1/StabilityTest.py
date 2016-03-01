from readXML import PSt, DSt
# import datetime
# Test ob das Ergebnis ein stabiles Matching ist

#candidate = [{0, 9, 5, 6}, {2, 3}, {1, 4}]
#candidate = [{1, 9, 5, 6}, {2, 3}, {0, 4}] # Testkandidat mit blockierenden Paaren

#candidate = [{1, 2, 3, 5, 6, 7, 13, 15, 16, 17}, {8, 9, 11, 18, 19}, {0, 4, 10, 12, 14}]

#candidate = [{0, 2, 4, 5, 7}, {3, 6}, {9}]

# PSt = [[[3, 1], [1, 2], [2, 3]], [[1, 1], [2, 2], [3, 3]], [[3, 1], [1, 2], [2, 3]], [[1, 1], [3, 2], [2, 3]], [[2, 1], [1, 2], [3, 3]], [[3, 1], [1, 2], [2, 3]], [[3, 1], [2, 2], [1, 3]], [[2, 1], [1, 2], [3, 3]], [[3, 1], [1, 2], [2, 3]], [[2, 1], [1, 2], [3, 3]]]
# DSt = [[datetime.datetime(2015, 3, 22, 12, 20, 23), 'PA'], [datetime.datetime(2015, 3, 19, 16, 1, 35), 'PA'], [datetime.datetime(2015, 2, 3, 12, 42, 5), 'NA'], [datetime.datetime(2015, 2, 22, 11, 39, 2), 'PA'], [datetime.datetime(2015, 2, 1, 17, 19, 48), 'PA'], [datetime.datetime(2015, 2, 19, 11, 4, 49), 'PA'], [datetime.datetime(2015, 2, 23, 17, 52, 23), 'PA'], [datetime.datetime(2015, 3, 15, 16, 19, 3), 'NA'], [datetime.datetime(2015, 3, 26, 16, 1, 57), 'NA'], [datetime.datetime(2015, 3, 26, 9, 17, 9), 'PA']]

# PSt = [[[3, 1], [1, 2], [2, 3]], [[1, 1], [2, 2], [3, 3]], [[3, 1], [1, 2], [2, 3]], [[1, 1], [3, 2], [2, 3]], [[2, 1], [1, 2], [3, 3]], [[3, 1], [1, 2], [2, 3]], [[3, 1], [2, 2], [1, 3]], [[2, 1], [1, 2], [3, 3]], [[3, 1], [1, 2], [2, 3]], [[2, 1], [1, 2], [3, 3]]]
# DSt = [[datetime.datetime(2015, 3, 22, 12, 20, 23), 'PA'], [datetime.datetime(2015, 3, 19, 16, 1, 35), 'PA'], [datetime.datetime(2015, 2, 3, 12, 42, 5), 'NA'], [datetime.datetime(2015, 2, 22, 11, 39, 2), 'PA'], [datetime.datetime(2015, 2, 1, 17, 19, 48), 'PA'], [datetime.datetime(2015, 2, 19, 11, 4, 49), 'PA'], [datetime.datetime(2015, 2, 23, 17, 52, 23), 'PA'], [datetime.datetime(2015, 3, 15, 16, 19, 3), 'NA'], [datetime.datetime(2015, 3, 26, 16, 1, 57), 'NA'], [datetime.datetime(2015, 3, 26, 9, 17, 9), 'PA']]


def stabilityCheck(candidate):
    blockingpairs=0
    for i in range(len(candidate)):
        for j in candidate[i]:          # Studenten ueberpruefen
            if i+1 !=  max(PSt[j])[1]:  # ob das Seminar in dem sie im Matching-Ergebnis sind eines ist, welchem sie nicht die hoechste Prioritaet vergeben haben
                for k in PSt[j]:            # in Prioritaetsliste des zu pruefenden Studenten die
                    if k[1] == i+1:         # Praeferenz fuer das Seminar suchen, in dem er sich im Matching-Ergebnis befindet
                        matchpref = k[0]    # und in matchpref diese Praeferenz speichern
                        break
                for k in PSt[j]:            # alle Praeferenzen des zu pruefenden Studenten durchgehen
                    if (k[0] > matchpref):  # wenn die Praeferenz hoeher ist als die fuer das Seminar in dem er sich im Matching-Ergebnis befindet --> hoehere Prioritaeten ueberpruefen
                        print("Pruefung durchfuehren bei Student", j, " mit Sem.", k[1])
                        for z in candidate[k[1]-1]:                            # alle Studenten im Matching-Ergebnis ueberpruefen ob der zu pruefende Student anstelle eines anderen in ein Seminar gelangen kann, dem er eine hoehere Prioritaet vergeben hat
                            if 'PA' in DSt[j] and 'PA' not in DSt[z]:          # zu pruefender Student in pflichtangemeldet und Student im Seminar nicht
                                blockingpairs+=1
                                print("    blockierendes Paar bei Student", j , "mit Sem", k[1], "bei", z, "wegen PA")
                                break                                      
                            if 'PA' not in DSt[j] and 'PA' in DSt[z]:
                                pass
                            else:               # zu pruefender Student und Student im Matching-Ergebnis sind beide PA oder beide NA --> Ueberpruefen wer die hoehere Praeferenz fuer das jeweilige Seminar hat
                                for v in PSt[z]:    # alle Prioritaeten des Studenten im Matching-Ergebnis durchgehen
                                    if v[1]==k[1]:  # wenn gleiches Seminar
                                        testpref = v[0]         # Praeferenz in testpref speichern
                                        if k[0] > testpref:     # wenn die Praeferenz des zu pruefenden Studenten hoeher ist als die des sich im Seminar befindenden Studenten im Matching-Ergebnis
                                            blockingpairs+=1
                                            print("    blockierendes Paar bei Student", j , "mit Sem", k[1], "bei", z, "wegen PR")
                                            break
                                        elif k[0] == testpref:          # zu pruefender Student und Student im Matching-Ergebnis haben gleiche Praeferenz fuer das Seminar, daher Anmeldezeitpunkt ueberpruefen
                                            if DSt[j][0]<DSt[z][0]:     # wenn der Anmeldezeitpunkt des zu ueberpr. Studenten vor dem des sich im Seminar befindenden Studenten liegt
                                                blockingpairs+=1
                                                print("    blockierendes Paar bei Student", j , "mit Sem", k[1],"bei",z, "wegen TS", )
                                                break
    print("Anzahl blockierende Paare:")
    return blockingpairs

#print(stabilityCheck(candidate))

