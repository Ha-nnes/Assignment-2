"""
Student Name: Hannes Meyer-Rahlfs    
Program Title: Erewhon Mobile Data Plans      
"""
# Function to calculate the charge based on data usage in megabytes
def calculate_charge(data_usage_mb):
    # Initialize variables for rate and charge
    rate = ""
    charge = 0.0

    # Determine charge based on data usage
    if data_usage_mb <= 200:
        rate = "$20.00 flat rate"
        charge = 20.00
    elif data_usage_mb <= 500:
        rate = "$0.105 per Mb"
        charge = data_usage_mb * 0.105
    elif data_usage_mb <= 1000:
        rate = "$0.110 per Mb"
        charge = data_usage_mb * 0.110
    else:                              #REMINDER: else is NOT always needed, and will only run if all other options failed 
        rate = "$118.00 flat rate"
        charge = 118.00

    return rate, charge

# Function to convert data usage to megabytes
def convert_data_usage(data, unit):
    if unit == 'GB':
        return data * 1024  # Convert gigabytes to megabytes
    elif unit == 'MB':
        return data  # Don't convert and return the data in megabytes
    else:
        print("Error: Invalid unit. Please use 'MB' or 'GB'.")
        return None  

# Main function to run the program
def main():
    # Get input from the user
    data_usage = float(input("Enter your data usage: "))
    unit = input("Is the data in MB or GB? ").strip().upper()

    # Convert data usage to megabytes
    data_usage_mb = convert_data_usage(data_usage, unit)

    # Checking if conversion was successful
    if data_usage_mb is None:
        return  # Return to exit the program if the unit was invalid

    # Calculate the charge based on data usage
    rate, charge = calculate_charge(data_usage_mb)

    # Output the results
    print("Your data usage is {:.2f} MB.".format(data_usage_mb))
    print("Rate:", rate)
    print("Total charge: ${:.2f}".format(charge))

main()
