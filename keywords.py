#True false
print(5==5)
print(5 > 5)

#None
print(None == 0)
print(None == False)
print(None == [])
print(None == None)
def a_void_function():
    a = 1
    b = 2
    c = a + b
x = a_void_function()
print(x)
#and ,or, not
print(True and False)
print(True or False)

#as
import math as myMath
print(myMath.cos(myMath.pi))
#assert
assert 5 > 4
assert 5 == 5
#break
for i in range(1, 8):
    if i == 5:
        continue
    print(i)

class ExampleClass:
    def function(parameters):
        print("function1() executing")
    def function2(parameters):
        print("function2 executing....")
ob1 = ExampleClass()
ob1.function()
ob1.function2()

#def 
def function_name(parameters):
    pass
function_name(10)

#del for deleting a variable 
a = 10 
print(a)
del a
a = 15
print(a)


#if elif else
num = 2
if num == 1:
    print("one")
elif num == 2:
    print("success = 2")
else:
    print("failed")

#for 
for i in range(1,10):
    print(i)

# from ... import
import math
from math import cos
print(cos(10))
#global
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15
read1()
write1()
read1()
write2()
read1()

#in 
a = [1,2,3,4]
print(4 in a)
a = lambda x: x*2
for i in range(1,6):
    print(a(i))

#nonlocal 
def outer_function():
    a = 5
    def inner_function():
        nonlocal a 
        a = 10
        print("Inner function:", a )
    inner_function()
    print("outer function: ", a)
outer_function()

#return 
def funct_return():
    a = 10
    return a
print(funct_return())
#while
i = 5
while(i > 0):
     print(i)
     i -= 1

#with
with open("example.txt", 'w') as my_file:
    my_file.write("Hello world!")

#yield
def generator():
    for i in range(6):
        yield i * i
g = generator()
for i in g:
        print(i)