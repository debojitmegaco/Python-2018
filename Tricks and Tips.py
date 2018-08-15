#Merging Two dictionary Values
di1={'a':1,'b':2}
di2={'c':1,'d':2}
di1.update(di2)
print(di1)

dic3 = {**di1,**di2}
print (dic3)

