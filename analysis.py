from input_data import get_user_data

age, resting_heart_rate, exercise_hours, height, weight = get_user_data()


def health_data():
    body_mass_index = weight  / (height ** 2)
    max_heart_rate = (220 - age) * 0.9
    heart_rate_reserve = (max_heart_rate - resting_heart_rate) * 0.9
    fitness_score = exercise_hours * 3.5 / abs((22 - body_mass_index) / 6) * (heart_rate_reserve / 100)
    cardio_risk = 1 / ((fitness_score + heart_rate_reserve) / 2)\
    
    cardio_risk = float(cardio_risk * 100 + '%')

    return body_mass_index, max_heart_rate, heart_rate_reserve, fitness_score, cardio_risk

