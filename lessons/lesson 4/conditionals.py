
# username = input("Luke")
# password = input("1234")

# if username == "Luke" and password == "1234":
#       print("Logged in")
# else:
#     print("Invalid credentials")

# Equals ==
# Not equals = !=
# Greater than = >
# Less than = <
# Greater than or equal to = >=
# Less than or equal to = <=

import random

guessed_number =(input("87"))
print(guessed_number)
random_number = random.randint(1, 100)


if guessed_number == random_number:
    print("you guessed correct :)")
elif True < 0 and guessed_number > 100:
    print("you guessed outside of the allowed range.")
elif True == True:
    print("Why are we here?")
else:
    print("you guessed incorrect.")