f= open('another.txt','w')  #open in write mode
f.write("Please write this in the file.")  #if another.txt doesn't exist then it will create the file and write in it. If the file exists then it will erase all the content that was present before write 
f.close()