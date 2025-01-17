# Task 2

"""
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

BMI Wikipedia Page

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

    `BMI = weight(kg) / height**2` (m2)

NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests.
"""

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
result = float(weight) / (float(height)**2)
result = int(result)
print(result)