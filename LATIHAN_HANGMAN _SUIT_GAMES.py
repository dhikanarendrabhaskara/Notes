################################## HANGMAN GAME
# secretWord = "umbrella"
# lengthWord = len(secretWord)
# alphabet = "abcdefghijklmnopqrstu"
# guessWord = []
# letterStorage = []
# name = input("what's your name? ")
# print("Hello " + name + ", time to play hangman!\n")

# def function1():
#     for i in secretWord:
#         guessWord.append("-")
#     print("Ok, the word you need has {} characters:".format(lengthWord))
#     print(guessWord)
# def function2():
#     guessCount = 10
#     while guessCount > 0:
#         guess = input("Pick a letter: ").lower()
#         if guess in letterStorage:
#             print("You've already guessed that letter!")       
#         else:
#             letterStorage.append(guess)
#             if guess in secretWord:
#                 print("You guessed correctly!")
#                 for x in range(0,lengthWord):
#                     if secretWord[x] == guess:
#                         guessWord[x] = guess
#                         print(guessWord)
#                 if not '-' in guessWord:
#                     print("YOU FUCKIN WON!")
#                     break       
#             else:
#                  print("The letter is not in then word")
#                  guessCount -= 1
#                  print("You have {} chance(s) left".format(guessCount))
#                  if guessCount == 0:
#                      print("YOU'RE FUCKIN DEAD!")
#                      break

# function1()
# function2()



###################################### SUIT GAME
# def Game():
#     my_points = 0
#     computer_points = 0 
#     play = True
#     '''
#     1 == batu
#     2 == gunting
#     3 == kertas
#     '''
#     name = input("\nHello there, what's your name ? ")
#     name = name.lower()
#     name1 = name.capitalize()
#     name2 = name.upper()
#     print("Alright {}, let's play SUIT!".format(name1))

#     while play:
    
#         import random

#         list1 = [1,2,3]
#         Computer = random.choices(list1)
#         inputComputer = ""
#         for i in Computer:
#             inputComputer += str(i)
#             inputComputer = int(inputComputer)
#         inputGame = int(input("\nChoose your input: "))
        
#         if inputGame == 1:
#             print("Your move: BATU")
#         elif inputGame == 2:
#             print("Your move: GUNTING")
#         elif inputGame == 3:
#             print("Your move: KERTAS")
#         if inputComputer == 1:
#             print("Computer's move: BATU")
#         elif inputComputer == 2:
#             print("Computer's move: GUNTING")
#         elif inputComputer == 3:
#             print("Computer's move: KERTAS")

#         if inputGame == 1 and inputComputer == 2:
#             print("YOU WIN")
#             my_points += 1
#         elif inputGame == 2 and inputComputer == 3:
#             print("YOU WIN")
#             my_points += 1
#         elif inputGame == 3 and inputComputer == 1:
#             print("YOU WIN")
#             my_points += 1
#         elif inputGame == inputComputer:
#             print("IT'S A DRAW")
#         else:
#             print("YOU LOSE")
#             computer_points += 1

#         if my_points == 3:
#             play = False
#             print("\nCONGRATULATIONS, {}! YOU'VE WON THE GAME".format(name2))
#         elif computer_points == 3:
#             play = False
#             print("\nI'M SORRY, {}. YOU'VE LOST THE GAME".format(name2))

# Game()




