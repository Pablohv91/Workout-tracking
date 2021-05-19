import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

NUTRITION_ID = "1e560807"
NUTRITION_KEY = "3c807c5c3319c2a5c8700e6c9c31dc5d"

USERNAME = 'hidalgus'
PASSWORD = 'fa43wj234in93lk0'

NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/4bfcdd9565b8f6580177f103d8851ed0/workoutTracking/workouts"

GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 178
AGE = 29

RUN = input("How much did you run today? ")

headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_KEY,
}

nutrition_params = {
     "query": RUN,
     "gender": GENDER,
     "weight_kg": WEIGHT_KG,
     "height_cm": HEIGHT_CM,
     "age": AGE
}

response_nutrition = requests.post(url=f"{NUTRITION_ENDPOINT}", data=nutrition_params, headers=headers)
response_nutrition.raise_for_status()
result_nutrition = response_nutrition.json()['exercises']


TYPE_OF_EXERCISE = result_nutrition[0]['name']
CALORIES = result_nutrition[0]['nf_calories']
DURATION = result_nutrition[0]['duration_min']


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

''' 
Hay otra forma de completar este ejercicio que seria hacer un for loop, tiene sentido ya que vas buscando entro 
todos los objectos que hay en la lista y seleccionas los que concuerdan con la palabra clave, 
ej [name] te ahorras las lineas que yo he escrito arriba. TYPE_OF_EXERCISES, ETC. 
'''
sheet_params = {
    'workout': {
        "date": today_date,
        "time": now_time,
        'exercise': TYPE_OF_EXERCISE.title(),
        'duration': f"{DURATION}",
        'calories': f"{CALORIES}",
    }
}

# response_workout = requests.get(url=f"{sheet_endpoint}", auth=HTTPBasicAuth('hidalgus', 'fa43wj234in93lk0'))
# result_workout = response_workout.json()
# print(response_workout)

response_workout = requests.post(SHEET_ENDPOINT, json=sheet_params, auth=HTTPBasicAuth(f"{USERNAME}", f"{PASSWORD}"))
print(response_workout.text)
