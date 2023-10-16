def bmiCalculator(height, weight):
    #function which takes weight and height as a paramater and return BMI value
    # weight : in kg
    # height : in meters
    if height<= 0:
        print("Invalid Height, Please enter correct value")
    bmiValue = weight / (height ** 2)
    return bmiValue
def main():
    height = float(input("What is your height in meters?"))
    weight = float(input("What is your weight in kilograms? "))
    bmi = bmiCalculator (height, weight)
    print("Your BMI value is" , bmi)
    if bmi<18.5:
        print(" You are under weight")
    elif (bmi >= 18 and bmi< 24.9) :
        print("Based on your BMI, you are categorized as Normal Weight")
    elif (bmi >= 25 and bmi < 29.9) :
        print(" Based on your BMI, you are categorized as Overweight")
    else :
        print("Based on your BMI, you are Obese")
main()

