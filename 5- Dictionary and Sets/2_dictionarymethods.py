myDic ={
    "fast": "Quick Manner",
    "sumant": "Coder",
    "marks": [1,2,3], 
    "anotherdic": {      #dictionary inside dictionary
        'sumant': 'Player'
        },
    1: 2
}


#keys returns a dict_keys of all the keys
print(myDic.keys())     #outputs dict_keys(['fast', 'sumant', 'marks', 'anotherdic', 1])
print(type(myDic.keys()))    #outputs <class 'dict_keys'>  


#values
print(myDic.values())   #prints all values


#items
print(myDic.items())  #prints all the key,value as kind of a list which we can iterate over



#update
updateDic ={
    "Greet": "Hello",
    "JapGreet": "Konichiwa"
}
myDic.update(updateDic)    # "Greet":"Hello" key value pair gets added to myDic and it can update existing value too
print(myDic)  #output
#{'fast': 'Quick Manner', 'sumant': 'Coder', 'marks': [1, 2, 3], 'anotherdic': {'sumant': 'Player'}, 1: 2, 'Greet': 'Hello', 'JapGreet': 'Konichiwa'}




#get
print(myDic.get("fast"))    #returns Quick Manner
print(myDic["fast"])    #returns Quick Manner
#same but...if we put a key that doesn't exist then .get returns none but mydic["key"] throws error