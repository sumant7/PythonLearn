story = "once Upon a time there was a boy named Sumant. he was very smart"

#functions

#len function ouputs length of the string
print(len(story))   #ouputs 63


#endswith tells you if the string ends with given string/character or not
print(story.endswith("Y"))   #output false
print(story.endswith("smart"))   #output true


#count tells you the count of a character/word/string in a string
print(story.count("a"))   #outputs 7
print(story.count("wa"))   #outputs 2


#capitalize makes first letter of a string capital 
print(story.capitalize())    #once -> Once


#find tells you if a character/word is in a string
print(story.find("was"))   #outputs 23 which is the index of the first apperance of was
print(story.find("bad"))   #outputs -1 since not present


#replace well....replaces every occurance
print(story.replace("Sumant", "Sumant Chaudhary"))  #replaces every occurance of Sumant with Sumant Chaudhary

# Example
# string1 = "Hello You"
# string1= string1.replace("You", "Sumant")
# print(string1)   outputs Hello Sumant