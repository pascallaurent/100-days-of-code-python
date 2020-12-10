print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_friends = int(input("How many people to split the bill? "))
tip = bill * (percentage/100)
total = bill + tip
each_person_pay = total / number_of_friends

message = f"Each person should pay: {round(each_person_pay, 2)}"
print(message)