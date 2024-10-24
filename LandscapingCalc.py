def main():
    def calculate_landscaping_price():
        # Base labor charge
        base_charge = 1000
        
        # Inputing values
        address = input("Enter the address: ")
        length = float(input("Enter the plot length (in feet): "))
        width = float(input("Enter the plot width (in feet): "))
        grass_type = input("Enter the type of grass (fescue, bentgrass, campus): ").lower()
        num_trees = int(input("Enter the number of trees: "))
        
        # Calculate area
        area = length * width
        total_cost = base_charge
        
        # Add charge for area over 5000 sq ft
        if area > 5000:
            total_cost += 500
        
        # Add cost based on type of grass
        if grass_type == "fescue":
            total_cost += area * 0.05
        elif grass_type == "bentgrass":
            total_cost += area * 0.02
        elif grass_type == "campus":
            total_cost += area * 0.01
        else:
            print("Invalid grass type. No additional charge will be added.")
        
        # Add cost for trees
        total_cost += num_trees * 100
        
        # Output the total cost
        print(f"\nTotal cost for landscaping at {address}: ${total_cost:.2f}")

    # Call the function to calculate the price
    calculate_landscaping_price()

# Run the program
main()


