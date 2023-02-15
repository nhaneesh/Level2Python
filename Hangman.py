import random
name = input("Please enter your name : ")
print("Goodluck ",name," . Today we are going to play hangman")
print("You have 10 chances to guess the word")
words = ["scissor","eraser","speaker","sharpener","pencil"]
word = random.choice(words)
# print(word)
guesses = ""
turns = 10
while turns > 0:
    left = 0
    for i in word:
        if i in guesses :
            print(i)
        else :
           print(" _ ")
           left = left +1
        #    print(left)
    if left == 0 :
        print("You won the game.Congratulations!")
        print("You guessed the correct word -----> ",word)
        break

    # turns = 0
    guess = input("Guess a letter: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have" ,turns , "chances left")
        if turns == 0 :
            print("You lose the game.The word was",word)


