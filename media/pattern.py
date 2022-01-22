# 1 
# 1 2 
# 1 2 3
# 1 2 3 4

# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(i+1):      # here i+1 because we have i rows so we will have need i+1 columns
#         print(j+1,end="")    # here j+1 because we have j columns so we have need j+1 values in indexes
#     print('')



 
i = 1
while i <= 5 :
    j = 1
    while j <=i:
        print("*",end = " ")
        j =j+1
    print()
    i =i+1

# 1234123412341234
# i=1
# while i<5:
#     j=1
#     while j<5:
#         print(j,end="")
#         j=j+1
#     i=i+1

# reverse indexs
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()
#  -----------------------#

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=int(input("enter"))
# for i in range(n):
#     for j in range(i,-1,-1): # or for j in range(i+1)
#         print(i+1,end=" ")   # here print row value
#     print()

i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    print()
    i=i+1

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1


# 5
# 4 4 
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(i,-1,-1):  
#         print(n-i,end=" ")    
#     print()

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(i+1):  
#         print(n-j,end=" ")    
#     print()

# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5


i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1
    print()
    i=i+1


# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(i,-1,-1):  
#         print(n-j,end=" ")    
#     print()

#         5 
#       5 4
#     5 4 3
#   5 4 3 2
# 5 4 3 2 1

# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):  
#         print(n-j,end=" ")    
#     print()

#         5
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5

# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):  
#         print(n-j,end=" ")    
#     print()


#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1

# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i,-1,-1):  
#         print(j+1,end=" ")    
#     print()


n=5
i=n-1
while i>=0:
    j=0
    while j<i:
        print('',end=" ")
        j=j+1
    k=i
    while k<=n-1:
        print("*", end=" ")
        k=k+1
    print()
    i=i-1