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
    Res = [set() for i in range(len(Sem))]
    matchStud = [False for i in range(len(PSt))]
    while  False in matchStud:
        for i in range(0, len(matchStud)):
            if matchStud[i] == True:
                pass
            else:
                if not PSt[i]:
                    matchStud[i] = True
                else:                
                    maxp = max(PSt[i])[1]         # [3, 1] --> 1
                    if Sem[maxp-1]>0:
                        Res[maxp-1].add(i)
                        Sem[maxp-1] -= 1
                        matchStud[i] = True
                    else:
                        for z in Res[maxp-1]:                            
                            if 'PA' in DSt[i] and 'PA' not in DSt[z]:
                                matchStud[z] = False
                                Res[maxp-1].remove(z)
                                Res[maxp-1].add(i)                            
                                matchStud[i] = True
                                break                                      
                            if 'PA' not in DSt[i] and 'PA' in DSt[z]:
                                pass
                            else:
                                if  max(PSt[i])[0] > max(PSt[z])[0]:
                                    matchStud[z] = False
                                    Res[maxp-1].remove(z)
                                    Res[maxp-1].add(i)                            
                                    matchStud[i] = True
                                    break    
                                elif max(PSt[i])[0] == max(PSt[z])[0]:      # Timestamp nur pruefen wenn Prioritaeten fuer das Seminar gleich sind
                                    if DSt[i][0]<DSt[z][0]:
                                        matchStud[z] = False
                                        Res[maxp-1].remove(z)
                                        Res[maxp-1].add(i)
                                        matchStud[i] = True
                                        break
                        if matchStud[i]==False:
                            PSt[i].remove(max(PSt[i]))
    return Res
f = matching(PSt, DSt, Sem)
print(f)