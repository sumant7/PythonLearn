class Railway:
    formType= "Railway Form"   # a class attribute
    def printData(self):    #printData is a method
        print(f"Name: {self.name}")
        print(f"Train: {self.train}")

myApplication = Railway()
myApplication.name= "Sumant"  #defining an object attributes
myApplication.train= "Anime Express"
myApplication.printData() #calls the method and it prints
# Name: Sumant
# Train: Anime Express
print(myApplication.formType)   #outputs Railway Form

#we can change class attributes also