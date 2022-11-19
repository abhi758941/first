num=int(input("enter the number whose factorial you want to findd")) #taking the inout from the user
factorial=1
if num<0: #checking if the number is nagetive
    print("sorry the factorial does not exist")
elif num==0: #checking is the number is zero
    print("factorial of 0 is 1")
for i in range (1,num+1): #finding the factorial
    factorial= factorial*i
print(factorial)