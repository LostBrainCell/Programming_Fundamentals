from price_is_right_games import guess_car_price

print("Welcome to the Car Price guessing game")


while True:

    guess = int(input("Guess the price of the car: "))

    result = guess_items_price(guess)

    print(result)

    play= input("Do you want to play again? (y/n): ")
    
    if play == "n":
        break
print("Thanks for playing!")