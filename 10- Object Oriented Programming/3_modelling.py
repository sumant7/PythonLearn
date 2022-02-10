# We identify the following
#let's take a company's example 
# Noun        ->  Class       ->Employee
# Adjective   ->  Attributes  ->name,age, salary
# Verbs       ->  Methods     ->getSalary(),increment()

class Employee:
    company="Google"

sumant =Employee()
sumant.company="Youtube"   #changed in object
harry =Employee()
print(sumant.company)   #outputs youtube
print(harry.company)    #outputs google


Employee.company= "Microsoft"  #changed in class itlself but object has more priority
print(sumant.company)   #outputs Youtube
print(harry.company)    #outputs Microsoft



sumant.salary= 50000   #instance attribute (not in class but specific to object)

#instance attribute has more priority than class attribute and is searched first during assingment and retrival