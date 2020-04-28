from math import *  #imports all possible 'math' modules in python3
num1 = input("Give me a number: ")  #Asks user for first num in the function
num2 = input("Give me another number: ")  #Asks user for second num in the function
operation = input("What operation would you like to do: add, subtract, multiply, or divide? ")  #Asks user for operation to be used
while operation not in ["add", "subtract", "multiply", "divide"]:  #if user didn't submit valid operation, prompt displays again
        operation = input("Please choose one of the listed operations: ") # " "
if operation == "add": #if operation is add, do following
    ans_add = round(float(num1) + float(num2))  #completes arithmetic operation
    print(num1 + " + " + num2 + " = " + str(ans_add))  #prints statement + result
elif operation == "subtract": #if op is subtract, do following
    ans_subtract = round(float(num1) - float(num2))  #" "
    print(num1 + " - " + num2 + " = " + str(ans_subtract))  #" "
elif operation == "multiply": #if op is multiply, do following
    ans_multiply = round(float(num1) * float(num2))  #" "
    print(num1 + " * " + num2 + " = " + str(ans_multiply)) #" "
elif operation == "divide": #if op is divide, do following
    ans_divide = round(float(num1) / float(num2)) #" "
    print(num1 + " / " + num2 + " = " + str(ans_divide)) #" "
else: #end of program
    quit