# Datei zum Ausfuehren der Skripte
from readXML import PSt, DSt
from MatchingAlgFu import matching
print(PSt)
print(DSt)

#Seminarliste mit Anzahl der Plaetze
Sem = [4,2,2]
print(Sem)

# Alg. ausfuehren
f = matching(PSt, DSt, Sem)
print(f)
