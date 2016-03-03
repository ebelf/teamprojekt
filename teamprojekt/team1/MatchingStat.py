
#ergebnis = [{1,4,2},{8,9},{3,6}]

# ueberprueft, wie viele Studierende im Ergebnis in dem Seminar sind, dem sie die hoechste Prioritaet gegeben haben

def highestPref(ergebnis, StatisticPSt):
    count=0
    anzStud = len(StatisticPSt)
    SetOFStudWithHPref = set()
    for sem in range(len(ergebnis)):
        for stud in ergebnis[sem]:
            highestPrefOfStud = max(StatisticPSt[stud])[1]
            if highestPrefOfStud == sem+1:
                count+=1
                SetOFStudWithHPref.add(stud)
    if count != 0:
        return count ,"von" , anzStud , "Studierenden sind im Matching-Ergebnis in einem Seminar, dem sie die hoechste Prioritaet vergeben haben: ", SetOFStudWithHPref
    else:
        return "Kein Studierender ist im Matching-Ergebnis in einem Seminar, dem er die hoechste Praeferenz vergeben hat."