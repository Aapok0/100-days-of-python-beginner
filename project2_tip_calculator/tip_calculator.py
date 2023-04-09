#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Hi, welcome to the tip calculator!\n")

bill_amount = float(input("How much was the bill in total?\n"))
people = int(input("How many of you are there?\n"))
tip_percentage = float(input("What percentage do you want to tip? (Just the number)\n"))

cost_per_person = round(bill_amount / people * ((tip_percentage) / 100 + 1), 2)
print(f"\nEach person needs to pay {cost_per_person:.2f}€.")