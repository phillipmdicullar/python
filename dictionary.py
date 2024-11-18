#is an unordered collection of items 
#has a key value pair
new_dict = {1:"Hello", 2:"Hi",3:"hola buenos"}
print(new_dict)
print(new_dict[1])

#updating value
new_dict[1] = "hey"
print(new_dict)
#creating a new dictionary
squares = {1:1,2:4,3:9,4:16,5:25}
print(squares)
#remove a particul item
print(squares.pop(4))
print(squares)
#remove an arbitary item
print(squares.popitem())
print(squares)
#delete a artuicular time
del squares[1]
print(squares)

squares.clear()#remove all items
print(squares)

#dictionary memebership test
#creating a new dictionay using comrehension
squares = {x: x*x for x in range(6)}
print(squares)

#dictionary membership test
squares = {1: 1, 3:9,5:25,7:49,9:81}
print(1 in squares)
print(2 not in squares)
#membesrhip tests for key only not alue
print(49 in squares)

#iterating through a dictionary
squares = {1:1,3:9,5:25,7:49,9:81}
for i in squares:
    print(squares[i])
squares = {1:1,3:9,5:25,7:49,9:81}
print(len(squares),"printing length")
print(sorted(squares),"This have been sorted")