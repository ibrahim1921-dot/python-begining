catNames=[]
while True:
    print('Enter the name of cat '+str(len(catNames)+1)+' (or enter stop to end!)')
    name=input()
    if name=='stop':
        break
    catNames.append(name)

print('The names of the cats are: ')

for name in catNames:
    for i in  range(len(catNames)):
        print('cat name '+str(i+1)+' is '+catNames[i])
