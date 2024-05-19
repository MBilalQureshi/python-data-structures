# myMixedlist 
myMixedlist = [1,2,3,True,'hello', None,[1,2,3]]
print(myMixedlist)

# Looping through list
for item in myMixedlist:
    print(item)

# looping through only list inside list
for item in myMixedlist:
    if(type(item)==list):
        print(item)