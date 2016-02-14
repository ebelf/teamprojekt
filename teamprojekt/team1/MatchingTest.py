'''
Created on 14.02.2016

@author: marc
'''
import unittest
import datetime
import MatchingAlgTry as candidate


class Test(unittest.TestCase):


    def test_1(self):
        PSt1 = [[3,1],[2,2],[1,3]]
        PSt2 = [[3,1],[1,2],[2,3]]
        PSt3 = [[1,1],[2,2],[3,3]]
        PSt4 = [[1,1],[3,2],[2,3]]
        PSt5 = [[2,1],[1,2],[3,3]]
        PSt6 = [[2,3],[1,1],[3,2]]
        PSt7 = [[2,1],[1,3],[3,2]]
        PSt8 = [[2,2],[1,1],[3,3]]
        PSt9 = [[2,3],[1,1],[3,2]]
        PSt10 = [[2,3],[1,2],[3,1]]
        
        PSt = [PSt1, PSt2, PSt3, PSt4, PSt5, PSt6, PSt7, PSt8, PSt9, PSt10]
        
        #Input-Daten der Studierenden
        DSt1 = [datetime.datetime(2015, 3, 1, 12, 59, 23),'NA']
        DSt2 = [datetime.datetime(2015, 3, 1, 12, 31, 3), 'NA']
        DSt3 = [datetime.datetime(2015, 4, 2, 10, 59, 23),'PA']
        DSt4 = [datetime.datetime(2015, 3, 5, 12, 40, 33),'NA']
        DSt5 = [datetime.datetime(2015, 3, 6, 10, 59, 20),'PA']
        DSt6 = [datetime.datetime(2015, 3, 3, 9, 40, 13),'NA']
        DSt7 = [datetime.datetime(2015, 3, 3, 8, 59, 22),'PA']
        DSt8 = [datetime.datetime(2015, 3, 2, 7, 40, 13),'NA']
        DSt9 = [datetime.datetime(2015, 3, 2, 8, 40, 13),'NA']
        DSt10 = [datetime.datetime(2015, 3, 2, 9, 40, 13),'NA']
        
        DSt = [DSt1, DSt2, DSt3, DSt4, DSt5, DSt6, DSt7, DSt8, DSt9, DSt10]
        
        #Seminarliste
        
        Sem = [2, 2, 4]
        Res = [set() for i in range(len(Sem))]
        
        matchStud = [False for i in range(len(PSt))]

        r = candidate.matching()
        self.assertEqual(r, [{0,1},{6,8},{2,4,7,9}])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()