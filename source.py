from random import randint
my_number = randint(1,100)
past_guesses = []

print("Guess the number between 1-100")
print("If you're far from my number I'll say 'cold!''")
print("When you're closer than your previous guess, I'll say: 'warmer!'")
print("When you're farther from the number than your previous guess I'll say 'colder!'")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Your guess must be a whole number between 1-100")
    else:
        if guess > 100 or guess < 1:
            print("Your number must be between 1-100")
        else:
            if guess == my_number:
                print(f"Congratulations! Your guess: '{guess}' - was correct! It took you {len(past_guesses)+1} tries to guess the number!")
                break
            if len(past_guesses) > 0 and abs(guess-my_number) < abs(past_guesses[-1]-my_number):
                print("Warmer!")
                past_guesses.append(guess)
                continue
            if len(past_guesses) > 0 and abs(guess-my_number) > abs(past_guesses[-1]-my_number):
                print("Colder!")
                past_guesses.append(guess)
                continue
            if abs(guess-my_number) > 10:
                print("Cold!")
                past_guesses.append(guess)
