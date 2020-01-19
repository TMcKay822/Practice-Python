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


#PyNative 2
#Given a range of numbers. 
#Iterate from o^th number to the end number and print the sum of the current number
# and previous number
def sumNum(a):
  prev=0
  for i in range(a):
    sums = prev +i
    print(sums)
    prev = i
sumNum(10)


#PyNative Question 3
#Accept string from the user and display only those characters which are present at an 
#even Index

def even_string_index(a):
  #print("Original string is: ", a)
  for i in range(len(a)):
    if i%2==0:
      print("index", [i],"=", a[i])
      i+=1

a = input("Enter string: ")
print("Original string is: ", a)
print("Printing only even index characters")
even_string_index(a)


