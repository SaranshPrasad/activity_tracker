import requests
from datetime import datetime
APP_ID = "af55a885"
API_KEY = "8ffa2494ffae53baf51896d68dc4f007"
PARAMS = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": "54",
    "height_cm": "175",
    "age": 19
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
sheety_endpoint = "https://api.sheety.co/c09466f75fb3c961c32c3eb55d0dc9af/copyOfMyWorkouts/workouts"
response = requests.post(url=exercise_endpoint, json=PARAMS, headers=headers)
results = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)