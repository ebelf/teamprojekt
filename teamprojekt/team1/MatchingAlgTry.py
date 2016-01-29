# Praeferenzlisten der Studierenden
import datetime
#from collections import deque

#PSt_ = [Praeferenz, Seminarnr.]

PSt1 = [[3,1],[2,2],[1,3]]
PSt2 = [[3,1],[1,2],[2,3]]
PSt3 = [[1,1],[2,2],[3,3]]
PSt4 = [[1,1],[3,2],[2,3]]
PSt5 = [[2,1],[1,2],[3,3]]

PSt = [PSt1, PSt2, PSt3, PSt4, PSt5]

#Input-Daten der Studierenden
DSt1 = [datetime.datetime(2015, 3, 1, 12, 59, 23),'NA']
DSt2 = [datetime.datetime(2015, 3, 1, 12, 31, 3), 'NA']
DSt3 = [datetime.datetime(2015, 4, 2, 10, 59, 23),'PA']
DSt4 = [datetime.datetime(2015, 3, 5, 12, 40, 33),'NA']
DSt5 = [datetime.datetime(2015, 3, 6, 10, 59, 20),'PA']

DSt = [DSt1, DSt2, DSt3, DSt4, DSt5]

#Seminarliste

Sem = [True, True, True]
Res = [set() for i in range(len(Sem))]

matchStud = [False for i in range(len(PSt))]

def emptylist():
    count=0
    for i in PSt:
        if i==set():
            count +=1
    if count==len(PSt):
        return True


def matching():
    while  False in matchStud:
        print('while')
        for i in range(0, len(matchStud)):
            print('for')
            if matchStud[i] == True:
                pass
            else:
                if not PSt[i]:
                    print('leer')
                    matchStud[i] = True
                else:                
                    maxp = max(PSt[i])[1]         # [3, 1] --> 1
                    if Sem[maxp-1]:
                        print(i)
                        Res[maxp-1] = i
                        Sem[maxp-1] = False
                        matchStud[i] = True
                        PSt[i].remove(max(PSt[i]))
                    else:
                        print('else')
                        if 'PA' in DSt[i] and 'PA' not in DSt[Res[maxp-1]]:
                            matchStud[Res[maxp-1]] = False
                            Res[maxp-1] = i
                            matchStud[i] = True
                            PSt[i].remove(max(PSt[i]))
                        if 'PA' not in DSt[i] and 'PA' in DSt[Res[maxp-1]]:
                            PSt[i].remove(max(PSt[i]))
                        else:
                            if DSt[i][0]<DSt[Res[maxp-1]][0]:
                                matchStud[Res[maxp-1]] = False
                                Res[maxp-1] = i
                                matchStud[i] = True
                                PSt[i].remove(max(PSt[i]))
                            if DSt[i][0]>DSt[Res[maxp-1]][0]:
                                PSt[i].remove(max(PSt[i]))
                
                    