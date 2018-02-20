#A sample of program for dictionary
#Define first the dictionary, it is initially empty

age = {}

#Add some names to the dictionary with corresponding age
age['Anna'] = 20
age['Portia'] = 19
age['Ambrose'] = 65
age['Allain'] = 45

#Use the function has_key(), it takes this form:
#function_name.has_key(key-name)
#It returns TRUE if the dictionary has key-name in it
#and returns FALSE if it doesn't

if age.has_key('Anna'):
    print "Anna is listed in the dictionary. She is",\
    age['Anna'], "years old"

else:
    print "Anna is not listed in the dictionary"

if age.has_key('Portia'):
    print "Portia is listed in the dictionary. She is",\
    age['Portia'], "years old"

else:
    print "Portia is not listed in the dictionary"

if age.has_key('Allain'):
    print "Allain is listed in the dictionary. He is",\
    age['Allain'], "years old"

else:
    print "Allain is not listed in the dictionary"

if age.has_key('Althea'):
    print "Althea is listed in the dictionary. She is ",\
    age['Althea'], "years old"

else:
    print "Althea is not listed in the dictionary"

#Use the function keys() -
#This function returns a list of all keys

print "The following are listed in the dictionary:"
print age.keys()

#Use this function to put all the key names in a list:

keys = age.keys()

#You can get a list of all the values in a dictionary.
#use the function values():

print "The following are the persons and their ages:"
print age.values()

#Put it in a list:
values = age.values()

#You can sort lists using the sort() function
#It will sort the values in a list
#If you use sort() in keys, it will only arrange
#everything in alphabetical order, as you will see when you run
#this progra, the values will be listed in ascendin order
#however, the names and age won't match, you need to create
#a code that will assign the value to its real key
print keys
keys.sort()
print keys

print values
values.sort()
print values

#You can find the number of entries
#with the len() function:
print "The dictionary contains ",\
len(age), "entries."