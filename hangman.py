wins = 0
losses = 0

# Give users 3 options to pick which type of animal and imported from our .py files
def choice():
    try:
        ask = input(
            "\n-Enter 1 to guess for a Land Type Animal 🦁\n-Enter 2 to guess for a Water Type Animal 🐋\n-Enter 3 to guess for a Flying Type Animal 🦅 \n>: ")
    except TypeError:
        print("Invalid Input, input must be a number 1-3 please try again")
    else:
        if ask == "1":
            import land_animal #import modules from other saved .py files
            land_animals = land_animal.get_random_word()
            return land_animals.upper()
        elif ask == "2":
            import water_animal #importing module from saved .py file
            water_animals = water_animal.get_random_word()
            return water_animals.upper()
        elif ask == "3":
            import flying_animal #importing module from saved .py file
            flying_animals = flying_animal.get_random_word()
            return flying_animals.upper()
        else:
            print("")


# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces


# Draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("🐆🦭🌊🐋🐍" * 8)
    draw_hangman(num_wrong)
    print("\nWord:", add_spaces(displayed_word), "  Guesses:", num_guesses,
          "  Wrong:", num_wrong, "  Tried:", add_spaces(guessed_letters))

def draw_hangman(num_wrong):
    print("____")
    print("    |")
    if num_wrong == 0:
        print()
    if num_wrong == 1:
        print("    O\n")
    elif num_wrong == 2:
        print("    O")
        print("    |\n")
    elif num_wrong == 3:
        print("    O")
        print("   \\|\n")
    elif num_wrong == 4:
        print("    O")
        print("   \\|/\n")
    elif num_wrong == 5:
        print("    O")
        print("   \\|/")
        print("    |\n")
    elif num_wrong == 6:
        print("    O")
        print("   \\|/")
        print("    |")
        print("   /\n")
    elif num_wrong == 7:
        print("    O")
        print("   \\|/")
        print("    |")
        print("   / \\\n")
    elif num_wrong == 8:
        print("    O")
        print("   \\|/")
        print("    |")
        print("   / \\\n")
        print("☠️"*30)



# Get next letter from user
def get_letter(guessed_letters):
    while True:
        digit = False # Check to make sure user only enters a letter
        alpha = True
        guess = input("Enter a letter: ").strip().upper()
        for char in guess:
            if char.isdigit():
                digit = True
                print("Please only enter letters")
            for char in guess:
                if char.isalpha():
                    alpha = False
                    continue
            # Make sure the user enters a letter and only one letter
            if guess == "" or len(guess) > 1:
                print("Invalid entry. " + "Please enter one and only one letter.")
                continue
            # Don't let the user try the same letter more than once
            elif guess in guessed_letters:
                print("You already tried that letter.")
                continue

            else:
                return guess


# The input/process/draw technique is common in game programming
def play_game():
    # Used a try an except function for our choice() to see if it is listed
    try:
        returned_word = choice()
        word = returned_word
        word_length = len(word)
        remaining_letters = word_length
        displayed_word = "_" * word_length
        num_wrong = 0
        num_guesses = 0
        wins = 0
        losses = 0
        guessed_letters = ""
        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)
        while num_wrong < 8 and remaining_letters > 0:
            guess = get_letter(guessed_letters)
            guessed_letters += guess

            pos = word.find(guess, 0)
            if pos != -1:
                displayed_word = ""
                remaining_letters = word_length
                for char in word:
                    if char in guessed_letters:
                        displayed_word += char
                        remaining_letters -= 1
                    else:
                        displayed_word += "_"
            else:
                num_wrong += 1

            num_guesses += 1

            draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

        print("🌊🌊🌊" * 10)

        if remaining_letters == 0:
            print("Congratulations! You got it in", num_guesses, "guesses.")
            wins += 1
            print("wins: ",wins)


        elif num_guesses <= 30:
            print("Sorry, you lost.")
            print("The word was:", word)





        # I changed this part of the code to accomodate for the extra total guesses that may occur correctly but still have 8 wrong in total leading to the revealing of the correct word
    except TypeError:
        print("Invalid Input, input must be a number 1-3 please try again")

def score():
    print("")
    print(" Score")
    print(" ------")
    print(" Won: ",wins, " Lost: ",losses)
# Used a try and except so that users can only enter a number between 1 - 3
def main():
    text = ("\t🦍 Welcome to the H A N G M A N Animal Game 🦍")
    x = text.center(8)
    print(x)
    draw_hangman(7)
    while True:

        play_game()
        print()
        score()
        again = input("Do you want to try again (y/n)?: ").lower()
        if again != "y":
            print("Thank you for playing! I hope you had fun!")
            print("==" * 30)
            break


# Setting our main function to play_game()

if __name__ == "__main__":
    main()
