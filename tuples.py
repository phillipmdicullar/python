#all()- return true if all elements of the tuple are true or if empty
#any()- return true if any of the tuple is true. if tuple is empty return false 
#enumerate()- return an enumarate object. it contains the index and value of all items of tuples as pairs
#len()- return the lenght in the tuple(number f items )
#max()- return the largest item in the tuple
#min()- return the smallest item in the tuple
#sorted()- take elements in the tuple and return a new sorted list 
#sum()- return the sum of al elements in the tuple 
#tuple()- convert an iterable (list, string, set dictionary )

#creating an empty value
tuple1 = ()
print(tuple1)

#creating tuples with interger value
tuple2 = (1 ,2,3)
print(tuple2)

#tuple with mixed data types
tuple3 = (101, "Aniban", 2000.00, "Hr nick")
print(tuple3)

#creation of nested tuple
tuple4 = ("points", [1,4,3],(7,8,9))
print(tuple4)

#tuple can be created without any parentheses
#also calle tuple packing 
tuple5 = 101, "sniper", 300.00, "hr depit"
print(tuple5)

#table unpackikng is also possible
empid, empname, empsa1, empdept = tuple5
print(empid, empname, empsa1, empdept)

#accesing elements in a tuple
tuple1 = ('a','b','c','d','e','f','g','h')
print(tuple1)
print(tuple1[3])
print(tuple1[4])
print(tuple1[5])

#nested tuple
nested_tuple = ("point", [1,3,4],(8,7,9))
print(nested_tuple)
print(nested_tuple[0][3])
print(nested_tuple[1][2])
print(nested_tuple[2][2])

#slicing tupel
tuple1   =  ('a','b','v','e','r','f','t')
print(tuple1[1:3])
print(tuple1[:-3])
print(tuple1[3:])
print(tuple1[:])
#tuples are immutable
tuple1 = ('w','e','l')
#tuple1[2] = 'x    #error

#concantenation of tuple 
tuple2 = ('w','e','f','g')
tuple3 = ('a','b','c','d','e')
print(tuple2 + tuple3)
print(('again',)*4)

#deletion of a tuple
tuple4 = ('w','e','f','g','h','i','i')

#as immutable so elements can not be deleted 
#del tuple4[2]

#but can delete an entire tuple 
# del tuple4
# print(tuple4)

#tuple operations
tuple6 = ('w','e','l','c','o','m','e')
print(tuple6.count('e'))
print(tuple6.index('c'))

#tuple operations
tuple6 = ('w','e','l','c','o','m','e')
#memebership
print('c' in tuple6)
print('c' not in tuple6)

#iteration through tuple i elements
for letters in tuple6:
    print("the tuples are --->: ", letters)

#built in functions
built_in = (22,23,534,56,67,8,9,9,200,888)
print(max(built_in))
print(min(built_in))
print(sorted(built_in))
print(len(built_in))
#
#
#
#