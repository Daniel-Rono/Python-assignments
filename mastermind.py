#Name: Daniel K Rono.      #Class of 2016.      # Third Programming Assignment.
# An interactive game of Mastermind. 

import random

password = "Amherst"                                                           # This is the cheat password.

code = input("Please enter the password: ")                                    # Prompts the user to input the password.

beads = 4

for bead in range(beads):                                                      # The range function iterates four times, once for each bead.                                                            

    pattern = random.choice(("red", "orange", "yellow", "green", "blue", "violet"))   #The random module here creates a secret pattern of colours of four beads from six.
    patternlist = pattern.split()

    if code == password:                                                       # Tests whether the password entered is correct.
        print (patternlist, end = " ")                

    else:
        print("Sorry, that's not the password. Enjoy the game!")
        break

def main():
    
    rules = input("Welcome to the game of Mastermind! If you would like to see the rules, enter '1' but if not, enter '2': ")  # Asks the user if he/she wants to see the rules.

    if rules == "1":
                                                                                                              # Prints the rules of the game upon the user's request.
        print (""" I will be the codemaker and you'll be the codebreaker. I'll make a secret pattern of 4 beads         
    of any colour combination, including repetitions. You shall have up to 10 tries or rounds to
    guess the correct pattern of colours. If you guess the exact pattern, you win! If you don't guess it in
    10 rounds, you lose. Let's begin! """)

    elif rules == "2":
        print ("Alright! Let's begin!")

    else:
        print ("That entry was invalid. Please enter either '1' or '2' as appropriate.")    #Validates the input for the prompt as to whether the user wishes to see the rules.
        main()

    mastermind()                                                                 # Calls the mastermind function, which actually plays the interactive game with the user.


def mastermind():                                                                #This function plays the game of Mastermind with the user.
    
    for trials in range (10):                                                    #This for-loop has a range of ten to correspond to the maximum rounds that the user can play.

        trial = 1

        while trial <= 10:                                                       # This while-loop iterates a maximum of ten times, one for each round of the game.

            for colour in range(4):                                              # This for-loop takes the user's guesses of the pattern of 4 bead colours.

                    guess = input ("I have four beads. Guess the colour of each bead one by one and press 'enter' after each guess: ")   
                    guesslist = guess.split()

            if guesslist == patternlist:                                         #Compares the user's guesses with the secret pattern.

                print ("Congratulations! Your guesses exactly match the color and position of the correct pattern! You have won the game!")     #Ends the game if the user guesses the correct pattern.     
                
                newgame = input("If you would like to play a new game, enter '1'. If not, enter any letter or number: ") #Asks the user if he/she would like to play a new game.  

                if newgame == "1":
                    main()                                                       #Starts over with a new game if the user requests it.

                else: 
                    print ("Thanks for playing!")
                    break                
            else:
                print ("Your guesses were not correct. Try again!")
                trial += 1                                                       # Incrementally adds the number of trials in a game within the while-loop.

                if trial == 11:                                                  # Ends a game after ten unsuccessful trials.                   

                    newgame = input("Unfortunately, you've lost after 10 guesses. If you would like to play a new game, enter '1'. If not, enter any letter or number: ")  #Starts over with a new game if the user requests it.

                    if newgame == "1":
                        main()                                                   #Starts over with a new game if the user requests it.

                    else:
                        print ("Thanks for playing!")
                        break

        break                                                                    # Ends the while-loop after a maximum of ten rounds. 

main()                                                                           #Calls the main function.

                                                                                 # This program lets the user know when he/she has entered the exact sequence of colours as that generated by the random function in
                                                                                 # line 14. However, after many, many trials, I've not been able to modify it to tell when there are beads that match in colour but
                                                                                 # not in position. As such, I've also not been successful at getting the turtle to draw the status of the game since this would be
                                                                                 # contingent upon correct and incorrect partial guesses.
            
