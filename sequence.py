# Design an algorithm that generates the first n numbers in the 
# following sequence:
# ; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

# Make sure that you write up the algorithm before starting to code.
# Then implement the algorithm in Python. 
# Put your algorihmic description as a comment in the program file.



n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter = 1
num1 = 1
num2 = 2
num3 = 3
num4 = num1 + num2 + num3
while counter < (n+1):
    if counter == 1:
        print(num1)
    elif counter == 2:
        print(num2)
    elif counter == 3:
        print(num3)
    elif counter == 4:
        print(num4)
    else:
        num1 = num2
        num2 = num3
        num3 = num4
        num4 = num1 + num2 + num3
        print(num4)
    counter += 1

