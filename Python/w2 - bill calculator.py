# Basic Tip Calculator. Write a program that asks for the total bill amount and the tip percentage. It should then calculate and
# display the tip amount and the total bill including the tip.
# Advanced: You can also ask for a name (using input()) and print the total amount with that name in it

name = input("Enter your name: ")

person_count = int(input("How many people? "))

amount = float(input("Enter the total bill amount: "))

tips = float(input("Tip percentage: ")) / 100

total_amount = amount + (amount * tips)

total_amount_per_person = total_amount / person_count

print(f"{name}, total amount (with tip): {total_amount:.2f}")

print(f"Each person pays: {total_amount_per_person:.2f}")