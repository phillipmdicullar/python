class MyComplexNumber:
    #constructor methods
    def __init__(self, real = 0, img = 0):
        print("my complex number constructor executing...")
        self.real_part = real
        self.img_part = img
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.img_part))

#create a new objct agbainst my complex number
complx1 = MyComplexNumber(40, 50)

#calling displaycomplex() function
#output 40 + 50j
complx1.displayComplex()

#create a new object against myComplexNumber class
#and create a new attribute 'new_attribute'
complx2 = MyComplexNumber(60, 70)
complx2.new_attribute = 80
complx2.displayComplex()

print((complx2.real_part, complx2.img_part, complx2.new_attribute))

#complex 1 does not have an 'new_attribute'
complx1.new_attribute
#Deleteting object attribute and the object 
print(complx1)
del complx1.real_part
del complx1