#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60  

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇'
print("Welcome to the tip calculator!")
base_amount = float(input("What was the total bill? $"))
tip_amount = (input("What percentage of tip would you like to give? "))
tip_amount2 = float(tip_amount)
tip_amount3 = ((tip_amount2 / 100) + 1)
num_people = float(input("How many people to split the bill? "))
split_amount = (base_amount / num_people) * (tip_amount3)
split_rounded = round(split_amount,2)
print(f"Each person should pay ${split_rounded}")
