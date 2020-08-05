person = {"first name" : "liliana" , "second name" : "solis" , "age" : 37 , "city" : "méxico"}



print(person["first name"].title() + ".")
print(person["second name"].title() + ".")
print(str(person["age"]) + ".")
print(person["city"].title() + ".\n")


number =   {


    "rafael" : str(8),
    "liliana" : 7,
    "paty" : 9,
    "jorge" : 11,
    }

print("Liliana´s favorite number is: " + str(number["liliana"]) + ".")
print("Paty´s favorite number is: " + str(number["paty"]) + ".")
print("Jorge´s favorite number is: " + str(number["jorge"]) + ".")
print("Rafael´s favorite number is " + number["rafael"] + ".\n")

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }


word = "string"
print("\n" + word.title() +  ":" " " + glossary["string"])

word = "comment"
print("\n" + word.title() + ":" " " + glossary["comment"])

word = "list"
print("\n" + word.title() + ":" " " + glossary["list"])

word = "loop"
print("\n" + word.title() + ":" " " + glossary["loop"])

word = "dictionary"
print("\n" + word.title() + ":" " " + glossary["dictionary"])