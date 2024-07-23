#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def return_total_tip_per_person(total_bill, number_of_homies, tip_percentage):
    result = (total_bill / number_of_homies) * (1.0 + round(tip_percentage/100,2))
    return round(result,2)

total_bill = float(input("1. Enter the total bill: €"))
number_of_homies = int(input("2. Enter the number of homies: "))
tip_percentage = int(input("3. Enter one of the following numbers as tip percentage (10 / 12 / 15): "))

total_tip_per_person = return_total_tip_per_person(total_bill, number_of_homies, tip_percentage)

print(f"Result: Each homie has to pay: €{total_tip_per_person}")
