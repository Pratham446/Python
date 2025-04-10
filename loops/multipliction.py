# print table upto 10 but skip 5 iteration
numbe=5
for i in range(1,10):
   if i==5:
      continue
   print(numbe,"X",i,"=",numbe*i)