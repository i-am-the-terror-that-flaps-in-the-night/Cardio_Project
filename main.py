# ------------------------------------------------------------
# This program is a learning project to analyze heart-related
# data using Python.
#
# DISCLAIMER:
# This program DOES NOT provide medical advice.
# It is NOT medically accurate and should NOT be used for
# diagnosis, treatment, or health decisions.
#
# It is only a student project for learning programming.
# ------------------------------------------------------------

"""
Cardio Project
A Python learning project that analyzes simple heart health metrics.
DISCLAIMER:
This program is for educational purposes only.
This is NOT medically accurate, see the disclaimer above.
"""


from input_data import get_user_data
from analysis import health_data
age, resting_heart_rate, exercise_hours, height, weight = get_user_data()
body_mass_index, max_heart_rate, heart_rate_reserve, fitness_score, cardio_risk = health_data()

health_data()
print(health_data())