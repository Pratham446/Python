string ="abcabd"

for i in string:
    print(i)
    if string.count(i)==1:
        print("the nonrepeated character is :",i)
        break
