#import xml.etree.cElementTree as ET
#from lxml import etree as ET
import xmltodict

"""
stream = open("LogCuautitlan.xml","r")
mytree = ET.parse(stream)
myroot = mytree.getroot()
"""


"""
print(ET.tostring(myroot).decode("utf8"))
for i in myroot:
   print(ET.tostring(i))
"""
"""
for i in myroot.iter("field"):
   print(i.tag, i.text, i.attrib)
"""


stream = open("LogCuautitlan.xml","r")
xml = xmltodict.parse(stream.read())
print(xml[3])
#for e in xml["user"]:
    #print(e)


#know all the elements in the entire tree ".iter()" in loop
#for i in myroot.iter("street"): know a specific element in the tree
 #print(i.text)
#print(myroot.tag)
#print(myroot.attrib)

#the .tostring() method, you can return the whole document e.g print(ET.tostring(myroot).decode("utf8")) with out loop
#for i in myroot:
   #print(ET.tostring(i))
   #print(i.get("trunc"))

#find and findall, seek in the tree "for i in myroot.find("address"):"
#text and tag in print with loop

#.findall() function that will traverse the immediate children of the referenced element. You can use XPath expressions to specify more useful searches.
#for movie in myroot.findall("./genre/decade/movie/[year='2000']"):
   # print(movie.tag)

#search on attributes
#for movie in myroot.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    #print(movie.attrib)
#for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
 #   print(movie.attrib)

