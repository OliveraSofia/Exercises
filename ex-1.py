'''1. Character Input: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.


    name = input("Enter your name:")
    print("Your name:" + name)

2. Odd Or Even : Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = input("Enter a number:")
x = int(number) % 2
if x == int():
    print("This is an even number")
else:
    print("This is an odd number")



 3   Exercise
    Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.





lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in lista:
 if i(lista) <5:
  print(i)

  Exercise 4
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

y = int(input("Ingresa un numero: "))
x = list(range(1, y+1))
lista = []
for i in x:
 if y %  i==0:
  lista.append(i)
  if i == y:
   print(lista)

Exercise 5 (and Solution)
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set(a) & set(b))




Exercise 6 (and Solution)
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

w = input("Enter a word:")

lista1 =[c for c in w]
print(lista1)

a = lista1[::-1]
print(a)
if a == lista1:
    print("It is a palindrome")
else:
    print ("It is not a palindrome")


Exercise 7 (and Solution)
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([i for i in a  if i % 2 ==0])

Exercise 8 (and Solution)
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

while True:
    usr_inp = input("Do you whants to play? Y/N" )
    if usr_inp is "y":
        p1 = input("Enter your hand as Player1:")
        p2 = input("Enter your hand as Player2:")

        if p1 == p2:
            print("Empate!")
        else:
            #r > s
            if p1 ==  ("rock").lower() and p2 == ("scissors").lower():
                print("P1 Wins!")
                print(p1,"beats: ",p2)
                print("Do you whants to play again?")
                #p>r
            elif p1 ==  ("paper").lower() and p2 == ("rock").lower():
                print("P1 Wins! ")
                print(p1,"beats: ",p2)
                print("Do you whants to play again?")
                #s > p
            elif p1 == ("scissors").lower() and p2 == ("paper").lower():
                print("P1 Wins!")
                print(p1,"beats: ",p2)
                print("Do you whants to play again?")
               # r < p
            elif p1 == ("rock").lower() and p2 == ("paper").lower():
                print("P2 Wins!")
                print(p2,"beats: ",p1)
                print("Do you whants to play again?")
            #p< s
            elif p1 == ("paper").lower() and p2 == ("scissor").lower():
                print("P2 Wins!")
                print(p2,"beats: ",p1)
                print("Do you whants to play again?")
            #S <r
            elif p1 == ("scissor").lower() and p2 == ("rock").lower():
                print("P2 Wins!")
                print(p2,"beats: ",p1)
                print("Do you whants to play again?")
            else:print("Pease, enter a valid value")
    elif usr_inp is "n":
        print("Bye")
        break

List Overlap Comprehensions
Exercise 10
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.




import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

b = random.sample(range(10), 10)
a= random.sample(range(15), 13)
print(a,b)
list1=[]
list1 = [i for i in a for y in b if i == y]
print(list1)



12 List Ends

 Exercise 12 (and Solution)
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new
 list of only the first and last elements of the given list. For practice, write this code inside a function.




def random_list():
    import random

    x = int(input("Enter a number:"))
    list1 = random.sample(range(10), x)
    print(list1)
    return list1

def first_and_last(list1):
    list2 = [list1[0],list1[-1]]
    return list2

x = first_and_last(random_list())
print(x)


Fibonacci
Exercise 13
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is
 the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


'''