#!/usr/bin/python

inputfile = "input.xml"


Pst = []
Dst = []

import datetime

import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse(inputfile)
collection = DOMTree.documentElement

# Get all the students in the collection
students = collection.getElementsByTagName("Student")


for student in students:
    Std = []
    Dst1 = []
    seminars = student.getElementsByTagName("Seminar")
    for seminar in seminars:
        Seminar = []
        Seminar.append(int(seminar.getAttribute("id")))
        Seminar.append(int(seminar.childNodes[0].data))
        Std.append(Seminar)
    Pst.append(Std)
    date = datetime.datetime(int(student.getElementsByTagName("year")[0].childNodes[0].data),int(student.getElementsByTagName("month")[0].childNodes[0].data),int(student.getElementsByTagName("day")[0].childNodes[0].data),int(student.getElementsByTagName("hour")[0].childNodes[0].data),int(student.getElementsByTagName("minute")[0].childNodes[0].data),int(student.getElementsByTagName("second")[0].childNodes[0].data))
    Dst1.append(date)
    Dst1.append(student.getElementsByTagName("pflichtanmeldung")[0].childNodes[0].data)
    Dst.append(Dst1)
print(Pst)
print(Dst)
    