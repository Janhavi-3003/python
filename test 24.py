def calculate_fare(miles, minutes, surge):
    try:
        miles = float(miles)
        minutes = float(minutes)
        surge = float(surge)
        
        if miles < 0 or minutes < 0 or surge < 0:
            print("Error: values cannot be negative.")
            return
        
        mile_cost = 1.50 * miles
        minute_cost = 0.25 * minutes
        total_fare = 2.50 + mile_cost + minute_cost + surge
        print(f"Total fare: ${total_fare:.2f}")
    
    except ValueError:
        print("Error: Invalid input")

 surge = input("Enter surge: ")

calculate_fare(miles, minutes, surge)           
