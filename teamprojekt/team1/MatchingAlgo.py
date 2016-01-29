'''
Created on 29.01.2016

@author: fabian
'''

class MatchingAlgo:
    '''
    classdocs
    '''
    aktuellePref = 0

    def __init__(self, graph, studenten, seminare):
        '''
        Constructor
        '''
        self.graph = graph
        self.studenten = studenten
        self.seminare = seminare
        
    def algo(self):
        while len(self.studenten)>0:
            student = self.studenten[0]
            '''
            while()
                if seminarplatz frei
                    Student belegt Seminar
                    break
                else
                    if Student besser als aktuellerStudent
                        aktuellerStudent wird frei
                        Student belegt Seminarplatz
                        break
                    else
                        if Student hat kein anderes Seminar mit gleicher Präferenz                            if Präferenz von Student == minimale Präferenz
                                lösche Student
                                break
                            else
                                Präferenz— des Studenten
                                break
            '''