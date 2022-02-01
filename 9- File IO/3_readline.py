#read only singular lines

f= open('sample.txt','r') 
data= f.readline()  
print(data)   #outputs only   Sumant is a Good Boy. and also a new line
data= f.readline()  #outputs only  He is also smart.  and also a new line
print(data)    
f.close()      