from price_is_right_games import guess_items_price


while True:
    print("Welcome to the Price is Right! Guess the price of this coffee")
    guess = int(input("Guess the price of the item: "))

    result = guess_items_price(guess)

    print(result)

    play= input("Do you want to play again? (y/n): ")
    
    if play == "n":
        break
print("Thanks for playing!")
# print("Welcome to the Price is Right! Guess the price of this coffee")
# guess = int(input("Guess the price of the item: "))

# result = guess_items_price(guess)

# print(result)

# print("The price were: ")
# print(random_prices)