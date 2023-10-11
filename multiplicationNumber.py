######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. Get the number as input

multiplicationNumber = int (input('enter the number:'))
noOfEntries = int (input("How many rows do you want to print:"))
for i in range (1,noOfEntries+1):
    print (i , "*" , multiplicationNumber , " = ", multiplicationNumber*i)     