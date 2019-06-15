'''Character Input: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.


    name = input("Enter your name:")
    print("Your name:" + name)

---------------------------------------------------------
Odd Or Even : Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = input("Enter a number:")
x = int(number) % 2
if x == int():
    print("This is an even number")
else:
    print("This is an odd number")

-------------------------------------------------------

    Exercise List Less Than Ten
    Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.




x = int(input("enter a number:"))

b= []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for e in a:
 if (e <=x):
  b.append(e)
print(b)
'''

