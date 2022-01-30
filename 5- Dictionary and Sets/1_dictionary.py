#Dictionary is a collection of key value pairs   key: value
myDic ={
    "Fast": "Quick Manner",
    "Sumant": "Coder",
    "Marks": [1,2,3], 
    "anotherdic": {      #dictionary inside dictionary
        'sumant': 'Player'
        }
}

print(myDic["Fast"])   #outputs Quick Manner
print(myDic['Marks'])    #outputs [1, 2, 3]
print(myDic['anotherdic'])    #outputs {'sumant': 'Player'}
print(myDic['anotherdic']['sumant'])    #outputs Player


#Dictionary is unordered unlike list.
#Unlike Tuple it is mutable       myDic['Marks]=[2,3,4]   is valid
#Duplicate keys are not allowed