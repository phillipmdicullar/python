# #create set
# #set of intergers
# my_set1 = {11,23,54,55,66,44}
# print(my_set1)
# #set of mixed data sets
# my_set5 = set([1,2,3,2])
# print(my_set5)
#  #we can make  alist from a set
# my_set1.add(77)
# print(my_set1)
# my_set1.update([88,99,22])
# print(my_set1)
# my_set1 = {11,22,33,44,55,66}
# print(my_set1)
# my_set1.discard(4)
# my_set1.remove(55)
# print(my_set1.pop())

#add()- add an el ement too a set 
#clear()- remove all elements from aset
#copy - return a shallow copy of a list
#differene()- return the difference or more sets as a new set
#difference_update - return all elemebts of another set from this set
#discard() - remove an element from set if it is a member
#intersection() - return the intersection of two sets as a new set 

#set operations union
myset1 = {0,1,2,3,4,5}
myset2 = {4,5,6,7,8,9}
print(myset1)
print(myset2)
#use | operator or union
print(myset1 | myset2)
print(myset2 | myset1)
print(myset1.union(myset2))
print(myset2.union(myset1))
#use & operator for intersection 
print(myset1 & myset2)
print(myset2 & myset1)
print(myset1.intersection(myset2))
print(myset2.intersection(myset1))
#
for letter in set("welcome"):
    print(letter)
myset1 = {0,1,2,3,4,5}
print(len(myset1))
print(max(myset1))
print(min(myset1))
print(sorted(myset1))

####################
