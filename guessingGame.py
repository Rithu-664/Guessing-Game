import random

randomInt = random.randint(1,9)

chances = 0

print('Guess a number between 1 and 9')

while chances < 5:

    inputVal = int(input('Enter your guess: '))
    
    if inputVal == randomInt:
        print('Congratulations! You won! 🎉🎊')
        break
    elif inputVal < randomInt:
        print("Your guess was too low: Guess a number higher than", inputVal)
    else:
        print('Aww man! Your guess was too high :( Guess a number lower than',inputVal)

    chances += 1

if not chances < 5:
    print("YOU LOST...The number was", randomInt)
