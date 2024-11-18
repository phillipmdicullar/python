#append(): to add elememns to end of list
#extend(): to extend all elements of a list to another list
#insert(): to insert an element to another index
#remove(): to remove an element from a list
#pop(): to remove elements return element at a given nindex
#clear() : to remmove all elements from a given list
#index() : to return the index of a fist matched element
#count() : to count the number of elements passed as an argument#
#sort() : to sort elements in an ascending order by default 
#revers(): to revers element in a list
#copy() : to retun a copy of elements in a list
#define and declare array
arr = [10, 20, 30, 40, 51]
print(arr)
#accesing array elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])# negative indexing
print(arr[2])

brands = ["coke", "Apple","Googl", "Microsoft", "Toyota"]
print(brands)
#finding the length of an array
num_bands = len(brands)
print(num_bands)
#adding elememt by using append
brands.append("intel")
print(brands)
#Removing elements from an array
colors = ["violet", "indigo", "blue", "green","yellow","orange","red"]
print(colors)
del colors[4]
colors.remove("blue")
print(colors)
colors.pop(3)
print(colors)
#modifying elements in an array by indexing
fruits = ["Apple", "banana","grape","orange"]
print(fruits)
fruits[1] = "pineapple"
fruits[-1] = "Guava"
print(fruits)
#
#concatenating two arrays with + operator
concat = [1,2,3]
concat + [4,5,6]
print(concat)

#repeating element in array
repeat = ["a"]
repeat = repeat * 5
print(repeat)
#slicing an array
humans = ["phil", "tyson", "hello", "weiber", "skimmer"]
print(humans)
print(humans[1:4])
print(humans[1:3])
print(humans[:3])
print(humans[-4:])
print(humans[-3:-1])
#declaring and defining multi dimensional arraym
multd = [[1,2], [3,4],[5,6],[7,8]]
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])

#
#
#
#
#
#
#
#
