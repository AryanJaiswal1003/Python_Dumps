# Workout Tracker with Nutritionix + Sheety

This project integrates the **Nutritionix API** and **Google Sheets (via Sheety API)** to automatically log your daily 
    exercises into a Google Sheet.

---

## Features
    - Take exercise input in plain English (e.g., `"ran 3 miles and did 20 pushups"`).
    - Use **Nutritionix API** to analyze the exercises and calculate:
        - Exercise name
        - Duration
        - Calories burned
    - Save the results into Google Sheets using the **Sheety API**.

---

## Setup Environment Variables

Create a .env file in the root directory and add:

    # Nutritionix API Credentials:
        NUTRITIONIX_APP_ID=your_nutritionix_app_id
        NUTRITIONIX_APP_KEY=your_nutritionix_app_key
    
    # Sheety API Endpoint (your Google Sheet endpoint):
        SHEETY_ENDPOINT=https://api.sheety.co/<project-id>/<sheet-name>/workouts
    
    # Sheety Bearer Token (from Sheety dashboard):
        SHEETY_BEARER_TOKEN=your_bearer_token

---