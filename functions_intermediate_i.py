#1

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#a
x[1][0] = 15
print(x)

#b
students[0]["last_name"] = "Bryant"
print(students[0])

#c
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

#d
z[0]["y"] = 30
print(z)

#2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in some_list: #iterates through each list entry
        for j in i.keys(): #interates through every key in dictionary
            print(j, "-", i[j])#prints the key, then the value at that key


iterateDictionary(students)

#3

def iterateDictionary2(key_name, some_list):
    for i in some_list:#iterates through a list of dictionaries
        print(i[key_name])#prints the values of the dictionary at the keyname

iterateDictionary2("last_name", students)

#4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in some_dict.keys():#iterates through a dictionary containing lists
        print(len(some_dict[i]), i)#prints the length of the list, then the key
        for j in some_dict[i]:#iterates through the list at a certain keyword
            print(j)#prints the value in the list
        print()
printInfo(dojo)