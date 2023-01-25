import random
print("Hello , what is your name?")
p_name = input()
print("Hello "+ p_name+" .Today we are playing guess the number game.")
print("I will guess a number in between (1 to 10) and you have to guess it . You are going to have 5 chances.")
number = random.randint(1,10)
#print(number)
#print(random.randint(1,100))
noOfGuesses = 0
while noOfGuesses < 5 :
    guess = int(input("Try guessing a number from 1 to 10 :"))
    noOfGuesses = noOfGuesses + 1
    if guess < number:
        print("Your guess is too low.")
    elif guess > number :
        print("Your guess is too high.")
    elif guess == number:
     #   print("You guessed correct.")
        break
if guess == number :
    print("You guessed it correct in ",noOfGuesses," tries")
else:
    print("Sorry you could'nt guess the correct number.")
    print("The correct number was: ",number)
    
