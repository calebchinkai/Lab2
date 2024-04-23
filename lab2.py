def get_user_input():    
    user_input=input("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    split=user_input.split(",")
    numbers_as_floats = [float(split)]
    return numbers_as_floats

def calculate_statistics(temperatures):
    # Calculate average, minimum, and maximum values
    average_temp = sum(temperatures) / len(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)

    return average_temp, min_temp, max_temp

def main():
    # Step 1: Get user input
    temperatures = get_user_input()

    # Step 2: Calculate statistics
    average_temp, min_temp, max_temp = calculate_statistics(temperatures)

    # Step 3: Print results
    print("Average temperature:", average_temp)
    print("Minimum temperature:", min_temp)
    print("Maximum temperature:", max_temp)

if __name__ == "__main__":
    main()