#if the bill was $150. split between 5 peopel with 12% tip
#each person should pay (1500.00 / 5) * 1.12#
#round the results into 2 decimial place = 33.50
#print(round(150 * 1.12, 2 ))
# print("Welcome to the tip calculator")
# bill = int(input("What was the total bill? "))
# tip = float(input("What percentage of tip would you like ti give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# payment = (bill / people) * tip
#
# print(f"Each person should pay: {payment} ")
print("Welcome to the tip calculator")
bill = float(input("what was the tosal bill? $"))
tip = int(input("What percentage of tip would you like ti give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = round(bill_with_tip / people, 2)
print(f"Each prosn sould pay {bill_per_person}")

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

print(f"Each person should pay: ${final_amount}")