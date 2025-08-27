import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# -------------------------- User profile details (for Nutritionix API) --------------------------
GENDER = "Male"
WEIGHT_KG = 62
HEIGHT_CM = 175
AGE = 25

# -------------------------- Load environment variables from .env file --------------------------
load_dotenv()

# Nutritionix API credentials (from .env)
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_APP_KEY")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")

# Sheety API credentials (from .env)
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

# Nutritionix Request Headers
NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

# Sheety Request Headers (Bearer authentication)
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

# -------------------------- Step 1: Get exercise details from user --------------------------
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell me which Exercises you did: ")

# Data Payload for Nutritionix API
exercise_data = {
    "query": exercise_input,           # User's exercise description
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nutritionix_endpoint, json=exercise_data, headers=NUTRITIONIX_HEADERS) # Send POST Request to Nutritionix
result = response.json()


# -------------------------- Step 2: Prepare data for Sheety -------------------------
today = datetime.now().strftime("%d/%m/%Y")         # Current date
time_now = datetime.now().strftime("%H:%M:%S")      # Current time

for exercise in result["exercises"]: # Loop through all exercises returned by Nutritionix
    sheet_input = {
        "workout": {   # "workout" must match your Sheety sheet tab name
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),   # Convert exercise name to Title Case
            "duration": exercise["duration_min"],   # Duration in minutes
            "calories": exercise["nf_calories"]     # Calories burned
        }
    }

# -------------------------- Step 3: Send data to Google Sheets via Sheety --------------------------
    sheety_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=sheet_input,
        headers=SHEETY_HEADERS
    )
    print("Sheety response:", sheety_response.text)
