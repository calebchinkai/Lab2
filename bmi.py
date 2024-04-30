def calculate_bmi(height, weight):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    BMI = weight / (height*height)
    print("bmi = "+ str(BMI))
    if BMI < 18.5:
        return -1
    if 18.5<=BMI<=25:
        return 0
    if BMI>25:
        return 1


calculate_bmi(weight=57, height=1.73)
