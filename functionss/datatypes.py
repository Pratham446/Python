# Refrence Count
# l1=[1,2,3]       #memory refrence is only one so l will take refrence of l1
# l2=l1            #directly assign refrence of l1->l2
# print(l1)
# print(l2)
# l1[0]=40
# print(l1)
# print(l2)
  
# [1, 2, 3]
# [1, 2, 3]
# [40, 2, 3]
# [40, 2, 3]

# Slicing concept 
# h1=[1,2,3]
# h2=h1[:] # made a refrence copy for h2 from h1
# print(h1)
# print(h2)
# h1[0]=25
# print(h1)
# print(h2) #h2 would be same

# [1, 2, 3]
# [1, 2, 3]
# [25, 2, 3]
# [1, 2, 3]




m=[1,2,3]                              #ref 1
n=[1,2,3]    #assigning explicitely    ref 2
print(n==m)  #check value
print(n is m )  # Checks memory refrence 


# x = str("Hello World")	str	
# x = int(20)	int	
# x = float(20.5)	float	
# x = complex(1j)	complex	
# x = list(("apple", "banana", "cherry"))	list	
# x = tuple(("apple", "banana", "cherry"))	tuple	
# x = range(6)	range	
# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	bool	
# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))
