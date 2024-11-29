'''Author:Anugrah Chandran
Date:29-11-24
Description:Program to check whether the given number is a valid mobile number or not using functions.'''
def mobile_number(number):
    if len(number) == 10 and number[0] in "789":
       print("Valid number")
    else:
        print("Non-valid number")
number = input("Enter mobile number: ")
mobile_number(number)