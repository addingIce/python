list1 = list('wearediscoveredsaveyourself')
list2 = list('deceptivedeceptivedeceptive')
list3 = []
for i in range(0,len(list1)):
    list3.append(chr((ord(list1[i])+ord(list2[i])-194)%26+98))
print(list1)
print(list2)
print(list3)
