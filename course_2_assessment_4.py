#1. Write a function called int_return that takes an integer as input and returns the same integer.

#Answer is:

def int_return(a):
    return a
num = 4
ans = int_return(num)
print(ans)
    
#2. Write a function called add that takes any number as its input and returns that sum with 2 added.

#Answer is

def add(a):
    return a + 2
print(add(5))

#3. Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.

#Answer is

def change(st):
    newstr = st + "Nice to meet you!"
    return newstr
print(change("Sam"))

#4. Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

#Answer is:

def accum(ls):
    acc = 0
    for i in ls:
        acc = acc + i
    return acc
lst = [2,4,6,43,8,48]
print(accum(lst))

#5. Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”.
#If the length is less than 5, return “Less than 5”.

#Answer is:

def length(ls):
    if len(ls) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"
lst = [2,4,6,43,8,48]
print(length(lst))    

#6. You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2.
#The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function.
#Do not worry about decimals.

#Answer is:

def divide(n):
    return n / 2
def sum(a):
    return (a / 2) + 6
print(divide(sum(4)))
