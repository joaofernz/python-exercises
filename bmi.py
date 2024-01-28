def calculate_bmi(weight, height):
    return weight / (height ** 2)


def main():
    print("Welcome to the BMI calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    print("Your BMI is:", bmi)

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 24.9:
        print("You are normal weight.")
    elif bmi >= 24.9 and bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")


if __name__ == "__main__":
    main()
