#PyNative Question 1
#Accept two int values from the user and return their product. 
#If the product is greater than 1000, then return their sum

  
#Solved using a function definition
def product_or_sum(a,b):  
  if (a*b > 1000):
    result = a+b
    print("The result is: ", result)
    
  else: 
    result = a*b
    print("The result is: ", result)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = product_or_sum(a,b)


