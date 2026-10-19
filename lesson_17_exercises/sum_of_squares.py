from squares_calculator import calculate_squares

# declare my_square and get user input
my_square = int(input("Enter a number to sum the squares: "))

# declare total, outside of the loop!
# total = 0

# for 1 until my_square+1 because upper range is exclusive
# for number in range(1, my_square+1):
#     # add squared number to our total
#     total += number ** 2
total = calculate_squares(my_square)


# print total
print(F"The sum of squares is {total}")
   