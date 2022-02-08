#find sum of 2 numbers using oops

#class is a blueprint/template for creating objects
#classes don't take up memory by itself
class Number:   #class name's first letter must be capital  (pascalcase NOT camelcase)
    def sum(self):   #self here means the object(s) which is made using this class
        return self.a + self.b


#an object is an instantiation of class, it is created based on class(template)
num=Number()    #num is a object based on the Number class/blueprint 
num.a=34
num.b=69
s=num.sum()
print(s)   #prints 103