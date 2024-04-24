import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ")

def get_user_input():    
    user_input=input()
    split=user_input.split(",")
    numbers_as_floats = [float(num) for num in split]
    return numbers_as_floats

def calc_average_temperature(temperatures):
    average_temp = sum(temperatures) / len(temperatures)
    return average_temp

def calc_min_max_temperature(temperatures):
    min_temp=min(temperatures)
    max_temp=max(temperatures)
    return [min_temp,max_temp]

def sort_temps(temperatures):
    temperatures.sort()

def calc_median_temperature(temperatures):
    med_temp=statistics.median(temperatures)
    return med_temp

def main():
    display_main_menu()
    temperatures = get_user_input()
    average_temp=calc_average_temperature(temperatures)
    min_temp,max_temp=calc_min_max_temperature(temperatures)
    med_temp=calc_median_temperature(temperatures)
    print("Average temperature:", average_temp)
    print("Minimum temperature:", min_temp)
    print("Maximum temperature:", max_temp)
    print("Median temperature: ", med_temp)

if __name__ == "__main__":
    main()