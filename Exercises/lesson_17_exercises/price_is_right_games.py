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

def guess_car_price(guess):
    car_price = random.randint(10000, 50000)
    print(f"The price of the car {car_price}")

    if guess == car_price
        print("You win! That's exactly the price! You're a cheater")
    elif guess > car_price -1000 and guess < car_price +1000
        print("You win!")
    elif guess > car_price -5000 and guess < car_price + 5000
        print("Your close!")
        