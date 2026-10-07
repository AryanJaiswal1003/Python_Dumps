# Workout Tracker with the 100 Days of Python Nutrition API + Sheety

This project uses the **100 Days of Python Nutrition API** to analyze exercises and the **Sheety API** to log them in
Google Sheets.

The exercise request is sent to
`https://app.100daysofpython.dev/v1/nutrition/natural/exercise`. The environment variable names retain the original
project naming, but their values must come from the 100 Days of Python Nutrition dashboard, not a legacy Nutritionix
account.

---

## Features
    - Take exercise input in plain English (e.g., `"ran 3 miles and did 20 pushups"`).
    - Use the **Nutrition API** to analyze the exercises and calculate:
        - Exercise name
        - Duration
        - Calories burned
    - Save the results into Google Sheets using the **Sheety API**.
    - Send exercise descriptions of up to 50 characters. Supported activity examples include running, jogging,
      swimming, walking, cycling, and weightlifting.

---

## Setup Environment Variables

Create a `.env` file in the repository root and add:

    # App ID and Nutrition API Key from the 100 Days of Python Nutrition dashboard:
        NUTRITIONIX_APP_ID=your_app_id
        NUTRITIONIX_APP_KEY=your_nutrition_api_key
    
    # Sheety API Endpoint (your Google Sheet endpoint):
        SHEETY_ENDPOINT=https://api.sheety.co/<project-id>/<sheet-name>/workouts
    
    # Sheety Bearer Token (from Sheety dashboard):
        SHEETY_BEARER_TOKEN=your_bearer_token

---