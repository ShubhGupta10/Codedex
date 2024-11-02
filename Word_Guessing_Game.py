import random

word_bank = ["hello", "rizz", "sigma", "tiktok"]
word  = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = len(word)
while attempts > 0:
    print("\n Current Word: " + "".join(guessedWord))
    guess_letter = input("Guess a letter: ")
    if guess_letter in word:
        for i in range(len(word)):
            if word[i]==guess_letter:
                guessedWord[i] = guess_letter
        print("Great Guess!")
    else:
        attempts -=1
        print(f"Wrong Guess!Attempts left are\t:{attempts}")
    if '_' not in guessedWord:
        print(f"\nCongratulations!! You guessed the word: {word}")
        break
    elif attempts == 0 and '_' in guessedWord: #This logic is important nor would arise error everytime for either of guesses
        print(f"\nYou\'ve run out of attempts! The word was: {word}")

