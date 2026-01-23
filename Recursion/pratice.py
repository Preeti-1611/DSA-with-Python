# def func(x,N):
#     if N==0:
#         return 
#     print(x)
#     func(x,N-1)



# print(func(15,3))
        







# def func(n):
#     if 1 > n:
#         return
#     func(n-1)
#     print(n)

# func(4)



# #1 to N 
# def func(i,N):
#     if i>=N:
#         return 
#     print(i)
#     func(i+1,N)


# print(func(0,6))



# # N to 1
# def func(N):
#     if N ==0:
#         return 
#     print(N)
#     func(N-1)

# print(func(5))


# # Count numbers

# # Return how many numbers exist from i to N.
# # count = 0
# # def countnum(i,N):
# #     if i>N:
# #         return 
# #     count+=1
# #     countnum(i+1,N)
# #     print(count)
    

# # print(countnum(0,6))


# #sum from 1 to N

# def sumnum(sum,i,N):
#        if i>N:
#            print(sum)
#            return 
#        sumnum(sum+i,i+1,N)
       

# sumnum(0,1,5)





# #Factorial

# def fact(n):
#      if n ==0 or n==1:
#           return 1
#      return n*fact(n-1)

# print(fact(6))



# #power of num

# def power(x,n):
#      return x**n

# print(power(2,3))





def countnum(i, N):
    if i > N:
        return 0
    return 1 + countnum(i+1, N)

print(countnum(0, 6))
