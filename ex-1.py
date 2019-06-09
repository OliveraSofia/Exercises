'''Character Input: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.


    name = input("Enter your name:")
    print("Your name:" + name)

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



    Exercise
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
'''
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

