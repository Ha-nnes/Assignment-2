
"""
Student Name: Hannes Meyer-rahlfs    
Program Title: Insurance calculator 
  
"""
#Note: tried using camel case for this program per the suggestion of my older brother who is a programmer.
#(for if your wondering why I used it in this program and not the others)

def calculateMonthlyInsurance(gender, age, vehiclePrice):
    # inputs for program
    if gender == 'Male':
        if 15 <= age < 25:
            return (vehiclePrice * 0.25) / 12
        elif 25 <= age < 40:
            return (vehiclePrice * 0.17) / 12
        elif 40 <= age < 70:
            return (vehiclePrice * 0.10) / 12
    elif gender == 'Female':
        if 15 <= age < 25:
            return (vehiclePrice * 0.20) / 12
        elif 25 <= age < 40:
            return (vehiclePrice * 0.15) / 12
        elif 40 <= age < 70:
            return (vehiclePrice * 0.10) / 12
    # If age isnt in applicable to conditions return 0
    return 0

def main():
    # Main program 
    gender = input("Enter your gender (Male/Female): ").capitalize() # Capitalized so it matches Male/Female when calling it.
    age = int(input("Enter your age: "))                             # REMINDER: use int because age cant be a float. (kept forgetting this)
    vehiclePrice = float(input("Enter the price of the vehicle: "))

    # Calculate the monthly insurance
    monthlyInsurance = calculateMonthlyInsurance(gender, age, vehiclePrice)

    if monthlyInsurance > 0: 
        print(f"The monthly insurance cost is: ${monthlyInsurance:.2f}") #REMINDER: do not forget to round to two decimal places
    else:
        print("No insurance available for the given age.") #REMINDER: can use else in place of Elif at end of if/elif statements (only at the end)

main()

