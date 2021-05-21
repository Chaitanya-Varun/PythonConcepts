x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a','b','c','d']
# for a,b,c in zip(x,y,z):
# 	print(a,b,c)

# print(zip(x,y,z))

# [print(i) for i in zip(x,y,z)]

# print(list(zip(x,y,z)))

# print(dict(zip(x,z)))

[print(a,b,c) for a,b,c in zip(x,y,z)]
#values in list comprehension will not store temporary variables unlike the 
#for loops