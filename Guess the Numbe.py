#import the random packge all the function in that pakeag is avilabe 
import random
# we are difining guess pramiter and X is our pramiter 
def guess (x):
 #after that we created the varieble random number to get random number random.randint(1,x) where b/w 1 and X
    rando_number = random.randint(1,x)
    # This initializes the variable 'guess' to 0. This variable will store the user's guess.
    guess = 0
    #This line assigns a string containing a message to the variable note. This message informs the user about the special prize they could win.
    note = "if You guess the number currect than you will Win special price 🎁🧧!! "
    #This prints the message stored in note to the console.
    print(note)
    #This starts a while loop that will continue to execute as long as the user's guess (guess) is not equal to the randomly generated number (rando_number).
    while guess !=  rando_number:
        #Inside the loop, this line prompts the user to input a guess. The input function displays the prompt and waits for the user to type a number. The user's input, which is a string, is converted to an integer using int(), and then assigned to the variable guess.
        guess = int(input(f" Guess the number betwen 1 and {x}: "))
        if guess  < rando_number:
          print("Sorry the number u have enterd is to low give it onther try 😉")
        elif guess > rando_number:
              print ("Sorry the number u have enterd is to high give it onther try 😉")

    print(f"Congratulations 🎉🎉 You have guess the curret nubmer {rando_number} and you have won the special price 🎁🎁")
# This line calls the guess function with an argument of 20, which means the user needs to guess a number between 1 and 20.
guess (20)