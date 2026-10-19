import random

def guess_items_price(guess):
    random_prices = [
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    ]
    print(F"The prices were: {random_prices}")
    if guess in random_prices:
        return "You win!"
    else:
        return "You lose!"