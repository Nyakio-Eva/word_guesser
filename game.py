import random

my_game = "guess a word"
my_word_bank = []   

with open("words.txt") as word_file:
    for line in word_file:
        my_word_bank.append(line.rstrip().lower())
        
print(my_word_bank)

word_to_guess = random.choice(my_word_bank)

misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0

print("welcome to ", my_game)
print("The word has ", len(word_to_guess), "letters.")

def guessing_game():
    while True:
        guess = input("Guess the word: ").lower()
        if len(guess) == 5 and guess.isalpha():
            return guess
        print("Please enter a valid 5-letter word.")


    
def check_guess(word_to_guess, guess, misplaced_guesses, incorrect_guesses):
    current_position = 0
    for i in range(len(guess)):
        if guess[i] == word_to_guess[i]:
            print(guess[i], end=" ")
            current_position +=1
        elif guess[i] in word_to_guess:
            if guess[i] == misplaced_guesses:
                misplaced_guesses.remove(guess[i])
                if guess[i] not in misplaced_guesses:
                    misplaced_guesses.append(guess[i])
                print("_", end=" ")
        
        else:
            if guess[i] not in incorrect_guesses:
                incorrect_guesses.append(guess[i])
                print("_", end=" ")
               
    print()
    
    if current_position == len(word_to_guess):
        return True
    return False



#game loop
while turns_taken < max_turns:
    guess = guessing_game()
    turns_taken +=1
    
    if check_guess(word_to_guess,guess, misplaced_guesses, incorrect_guesses):
        print("Congrats you won!")
        break
    
    print("Misplaced letters: ", misplaced_guesses)
    print("Incorrect letters: ", incorrect_guesses)
    print("Turns remaining: ", max_turns - turns_taken)
    
    if turns_taken == max_turns:
        print("Sorry you lost! The correct word is .", word_to_guess)