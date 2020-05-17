secret = 19
guess = 0

guess = int(input("Guess the secret number:"))
if guess == secret:
    print("Congrats, you're guessed the secret number! It's "+ str(secret))
else:
    print("Sorry, you're wrong. Secret number is "+ str(secret))
