# Items = ["apple", "banana", "cherry", "date"]

#  for index, item in enumerate(Items):
#     print(f"Index: {index}, Item: {item}")

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_of_weekend = ["Saturday", "Sunday"]
print("Days of the week:")

for index, day in enumerate(days_of_week):
    # print(F"{day} is a day of the week.")
    # if day == "Monday":
    
    if day == "Wednesday":
        break

    # print("Is h in our list?")
    # print("h" in ["h", "e", "l", "l", "o"])


    # print(f"{day} is day number {index + 1} of the week.")

    if day in days_of_weekend:
        print(f"{day} is a weekend day.")
    else:
        print(f"{day} is a weekday.")

#     print("Inside the loop.")

# print("Outside the loop.")