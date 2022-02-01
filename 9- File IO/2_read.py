
#remember to the terminal in this folder or provide full path to the file in open


#opening and reading a file
f= open('sample.txt','r')   #opened the file in read mode
data= f.read()  #read the content from the file using read function
print(data)   #outputs 
# Sumant is a Good Boy
# He is also smart.
f.close()   #always close the file after work is done

#we can do f.read(5) if we just want to read the first 5 characters of the file



