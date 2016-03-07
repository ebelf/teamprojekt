# Datei zum Ausfuehren der Skripte
import copy
import timeit
from readXML import PSt, DSt
from MatchingAlgFu import matching
from outputXML import output
from StabilityTest import stabilityCheck
from PATest import AllPAinErg
from MatchingStat import highestPref

print(PSt)
print(DSt)

# fuer Statistik / zur Ueberpruefung der hoechsten Prioritaeten, da Liste PSt sich waehrend der Ausfuehrung des Alg. veraendert
StatisticPSt = copy.deepcopy(PSt)

#Seminarliste mit Anzahl der Plaetze
Sem = [5,2,2]
print(Sem)

# Alg. ausfuehren
t1 = timeit.Timer("matching(PSt,DSt,Sem)", "from __main__ import matching, PSt, DSt, Sem") 
f = matching(PSt, DSt, Sem)
print("Zeit: ", t1.timeit(number=100)/100)
print(f)
output(f)

# Test auf stabiles Matching durchfuehren'
#g = stabilityCheck(f)
#print(g)

# PA ueberpruefen
h = AllPAinErg(f, DSt)
print(h)

# hoechste Prioritaeten ueberpruefen
j = highestPref(f, StatisticPSt)
print(j)