# Datei zum Ausfuehren der Skripte
import copy
from readXML import PSt, DSt
from MatchingAlgFu import matching
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
f = matching(PSt, DSt, Sem)
print(f)

# Test auf stabiles Matching durchfuehren
g = stabilityCheck(f)
print(g)

# PA ueberpruefen
h = AllPAinErg(f, DSt)
print(h)

# hoechste Prioritaeten ueberpruefen
j = highestPref(f, StatisticPSt)
print(j)