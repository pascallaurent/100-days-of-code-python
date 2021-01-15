age = input("What is your current age?")

year_left = 90 - int(age)
days = year_left * 365
weeks = year_left * 52
months = year_left * 12

print(f"You have {days} days, {weeks} weeks and {months} months left.")