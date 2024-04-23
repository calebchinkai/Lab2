def calculate_bmi(height, weight):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    BMI = weight / (height*height)
    print("bmi = "+ str(BMI))
    if BMI < 18.5:
        print("Under weight")
    if 18.5<=BMI<=25:
        print("Normal weight")
    if BMI>25:
        print("Over weight")


calculate_bmi(weight=57, height=1.73)
