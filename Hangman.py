import random

def hangman():
    
    word_list = ["ankara","istanbul","izmir","paris","oslo","hamburg"]
    selected_word = random.choice(word_list)
    current_status = ["_"] * len(selected_word)
    wrong_guesses = 0
    max_wrong_guesses = 6
    
    while max_wrong_guesses > wrong_guesses and "_" in current_status:
        guess = input("Guess a letter please: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue
        
        if guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    current_status[i] = guess
                    
        else:
            wrong_guesses += 1
            print("Your guess is wrong! Remaining guesses: ", max_wrong_guesses - wrong_guesses)
            
        print(" ".join(current_status))
    
    if "_" not in current_status:
        print("Congratulations! You've found the word: ", selected_word)
    else:
        print("Sorry, you've run out of guesses. The correct word was: ", selected_word)

hangman()