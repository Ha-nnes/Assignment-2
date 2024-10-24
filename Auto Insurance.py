
"""
Student Name: Hannes Meyer-rahlfs    
Program Title: Insurance calculator 
  
"""

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
    gender = input("Enter your gender (Male/Female): ").capitalize()
    age = int(input("Enter your age: "))
    vehiclePrice = float(input("Enter the price of the vehicle: "))

    # Calculate the monthly insurance
    monthlyInsurance = calculateMonthlyInsurance(gender, age, vehiclePrice)

    if monthlyInsurance > 0:
        print(f"The monthly insurance cost is: ${monthlyInsurance:.2f}")
    else:
        print("No insurance available for the given age.")

main()

