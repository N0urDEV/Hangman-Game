import random

word_list = ["Apple","Banana","Cherry","Dog","Elephant","Football","Grapes","Helicopter","Icecream","Jaguar","Kangaroo","Lemon","Monkey","Notebook","Orange","Pineapple","Cat","Rainbow","Strawberry","Tiger"]
random_word = random.choice(word_list).lower()
Tcar = random_word
Tessai = ["*"] * len(Tcar)
print(Tessai)

max_attempts = 5
attempts = 0

print("Welcome to Hangman! You have 5 attempts to guess the word.")

while True:
    guessed_char = input("Enter a character: ").lower()
    positions = []

    if len(guessed_char) != 1 or not guessed_char.isalpha():
        print("Please enter a single letter.")
        continue

    for index, char in enumerate(Tcar):
        if char == guessed_char:
            positions.append(index)
            Tessai[index] = guessed_char 

    if positions:
        print(f"The character '{guessed_char}' is in the word at positions: {positions}")
    else:
        print(f"The character '{guessed_char}' is not in the word.")
        attempts += 1 

    if "*" not in Tessai:
        print(f"Congratulations! You've won the game, the word is : {Tcar} ")
        break
    elif attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The word was : {Tcar}")
        break

print("Game over.")
