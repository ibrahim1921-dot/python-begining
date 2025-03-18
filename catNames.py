catNames=[]
while True:
    print('Enter the name of cat '+str(len(catNames)+1)+' (or enter stop to end!)')
    name=input()
    if name=='stop':
        break
    catNames.append(name)

print('The names of the cats are:')

for name in catNames:
    print(' '+name)
