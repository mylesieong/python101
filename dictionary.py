#!/c/Users/BI77/AppData/Local/Programs/Python/Python35-32/python
phonebook1 = {}
phonebook1["John"] = 938477566
phonebook1["Jack"] = 938377264
phonebook1["Jill"] = 947662781
print(phonebook1)

phonebook2 = {
    "John2" : 938477566,
    "Jack2" : 938377264,
    "Jill2" : 947662781
}
print(phonebook2)

for name, number in phonebook1.items():
    print("Phone number of %s is %d" % (name, number))
    
print("Before delete:")
print(phonebook1)
del phonebook1["John"]
phonebook1.pop("Jack")
print("After delete:")
print(phonebook1)