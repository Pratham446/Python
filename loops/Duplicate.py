#Check the Duplicate items in list 

list=["mango","apple","apple","Banana","kiwi"]

Unique_item=set()
# made a bucket of unique items 

for i in list:
    if i in Unique_item:
        print("duplicate",i)
        break
# if unique item ke pass sab nai hai to add hojyea set me
    Unique_item.add(i)