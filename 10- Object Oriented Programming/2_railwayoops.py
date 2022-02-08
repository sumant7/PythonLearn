class Railway:
    formType= "Railway Form"   # a variable
    def printData(self):    #printData is a method
        print(f"Name: {self.name}")
        print(f"Train: {self.train}")

myApplication = Railway()
myApplication.name= "Sumant"
myApplication.train= "Anime Express"
myApplication.printData() #calls the method and it prints
# Name: Sumant
# Train: Anime Express
print(myApplication.formType)   #outputs Railway Form