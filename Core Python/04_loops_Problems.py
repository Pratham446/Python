# Count Positve numbers 
# number=['1','2','-3','-4','5','6']
# positive_number_count=0
# for i in number:
#     if int(i) > 0:
#          positive_number_count +=1
# print(positive_number_count)

#  Sum of even numbers 

# number=10
# sum=0
# for i in range(1,number+1):
#     if int(i%2)==0:
#         sum +=1
# print(sum)

# Multiplcation Table Printer 

# table=10
# for i in range(1,11):
#     if i==5 :
#         continue
#     print(i ,' X ',int(table),' = ',i*table )

# # reverse a string using loop
# string="HEllO"
# reverse_String=""

# for i in string:
#     reverse_String=reverse_String+i

# # we simply swap 
#     reverse_String=i+reverse_String

# print(reverse_String)

# find First Non repeated character
# string="Pratham"
# for i in string:
#     if string.count(i)==1:
#         print(i)


# factorial using while loop

# factorial=1
# number=5

# while number>0:
#     factorial=factorial*number
#     number=number-1
# print(factorial)

# validate input until user dont enter number between 1 and 10

# while True:
#     number=int(input("enter a number between 1 to 10"))
#     if 1<=number<=10:
#         print("thanks")
#         break

# check number is prime or not

# number=3
# is_prime =True

# if number>1:
#     for i in range(2,number):
#         if(number % i)==0:
#             is_prime=False
#             break
# print(is_prime)

# unqique item checker

# item=["apple","mango","apple","orange"]
# unique_item=set()

# for i in item:
#     if i in unique_item:
#         print("Duplicate",i)
#         break
#     unique_item.add(i)


# Expoential backoff strategy

import time 
waittime=1
maxtries=5
attempt=0

while attempt<maxtries:
    print("Attemp",attempt+1,"waitTime",waittime)
    time.sleep(waittime)
    attempt+=1
    waittime*=2

