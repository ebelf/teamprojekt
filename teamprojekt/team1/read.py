#!/usr/bin/python

Pst = []

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("input.xml")
collection = DOMTree.documentElement

# Get all the movies in the collection
students = collection.getElementsByTagName("Student")

# Print detail of each movie.
for student in students:
    Std = []
    seminars = student.getElementsByTagName("Seminar")
    for seminar in seminars:
        Seminar = []
        Seminar.append(int(seminar.getAttribute("id")))
        Seminar.append(int(seminar.childNodes[0].data))
        Std.append(Seminar)
    Pst.append(Std)
print(Pst)
    