def get_user_data():
    age = float(input("How old are you? \n"))
    resting_heart_rate = float(input("What is your resting heart rate? \n"))
    exercise_hours = float(input("How many hours do you excercise each week on average? \n"))
    height = float(input("What is your height in meters? \n"))
    weight = float(input("What is your weight in kilograms? \n"))

    return age, resting_heart_rate, exercise_hours, height, weight

if __name__ == "__main__":
    get_user_data()