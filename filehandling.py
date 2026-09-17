#File Handling
'''File handling means reading data from a file or writing data into a file using Python.


'''

'''
#modes
r=read
w=write
a=append
x=create
b=binary mode
t=text mode
'''
''' 
#with open()
Instead of manually calling: file.close() Python automatically handles closing the file after the with block.'''

#Why use with?(It is safer and cleaner, especially if an error occurs.)
with open("student.txt","r") as file:
    data=file.read()
    print(data)

#1.open() Function
#Python uses open() to open a file.
file=open("hello.txt","r")
data=file.read() #read() -> Reads the complete file.
print(data)
file.close()

file=open("hello.txt","r")
print(file.readline()) #readline() Reads one line.
file.close() 

file=open("hello.txt","r")
data=file.readlines()#readlines() Reads all lines and returns them as a list.
print(data)
file.close() 

file=open("hello.txt","w")
data=file.write("As a Trainnee Software Engineer")#the old content can be replaced with the new data
file.close()

file=open("hello.txt","a")
data=file.write("\nWelcome Aswini")#a ante existing data ni delete cheyyakunda last lo new data add cheyyadam.
file.close


'''CSV
CSV = Comma-Separated Values
CSV is commonly used for tabular data.Python provides the built-in csv module.'''
import csv
with open("students.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

import csv
with open("students.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["name","age","course"])
    writer.writerow(["Santhosh",20,"B.Tech"])
    writer.writerow(["Ashu",22,"B.Tech"])

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])


'''JSON = JavaScript Object Notation
   It is commonly used for data exchange, especially between applications and APIs.
'''
import json
student={
    "name":"Ashu",
    "age":22,
    "course":"B.Tech"
}
with open("student.json","w")as file:
    json.dump(student,file)

import json
with open("student.json","r")as file:
   student= json.load(file)
   print(student)


#XML = Extensible Markup Language
import xml.etree.ElementTree as ET
tree=ET.parse("studentdetails.xml")
root=tree.getroot()
print(root.tag)
for child in root:
    print(child.tag,child.text)






