import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)

GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 175
AGE = 25
NUTRITION_API_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_APP_KEY")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT_WORKOUT")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN_WORKOUT")

if not NUTRITIONIX_API_KEY or not NUTRITIONIX_APP_ID:
    raise ValueError(
        "NUTRITIONIX_APP_KEY and NUTRITIONIX_APP_ID must be set in the repository .env file."
    )
if not SHEETY_ENDPOINT or not SHEETY_BEARER_TOKEN:
    raise ValueError(
        "SHEETY_ENDPOINT and SHEETY_BEARER_TOKEN must be set in the repository .env file."
    )

NUTRITION_API_HEADERS = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
}


def request_json(response: requests.Response, service: str) -> Any:
    try:
        payload: Any = response.json()
    except requests.exceptions.JSONDecodeError as error:
        raise RuntimeError(
            f"{service} returned a non-JSON response (HTTP {response.status_code})."
        ) from error

    if not response.ok:
        detail = payload.get("message") if isinstance(payload, dict) else None
        if service == "Nutrition API" and response.status_code == 401:
            raise RuntimeError(
                "The Nutrition API rejected the credentials. Set NUTRITIONIX_APP_ID "
                "and NUTRITIONIX_APP_KEY to the App ID and Nutrition API Key from "
                "the 100 Days of Python Nutrition dashboard."
            )
        if not isinstance(detail, str):
            if response.status_code == 422:
                detail = "Request validation failed; check the required query and field ranges."
            elif response.status_code == 429:
                detail = "Rate limit exceeded (maximum 60 requests per minute per API key)."
            else:
                detail = f"HTTP {response.status_code}"
        raise RuntimeError(f"{service} rejected the request: {detail}")
    return payload


def main() -> None:
    sheety_endpoint = SHEETY_ENDPOINT
    if not sheety_endpoint:
        raise ValueError("SHEETY_ENDPOINT must be set in the repository .env file.")

    exercise_input = input("Tell me which Exercises you did: ").strip()
    if not exercise_input:
        raise ValueError("Enter at least one exercise before submitting.")
    if len(exercise_input) > 50:
        raise ValueError("Exercise description must be 50 characters or fewer.")

    exercise_data = {
        "query": exercise_input,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }

    try:
        response = requests.post(
            url=NUTRITION_API_ENDPOINT,
            json=exercise_data,
            headers=NUTRITION_API_HEADERS,
            timeout=30,
        )
    except requests.RequestException as error:
        raise RuntimeError("Could not connect to the Nutrition API.") from error

    result = request_json(response, "Nutrition API")
    exercises = result.get("exercises") if isinstance(result, dict) else None
    if not isinstance(exercises, list):
        detail = result.get("message") if isinstance(result, dict) else None
        if not isinstance(detail, str):
            detail = "The response did not contain an exercises list."
        raise RuntimeError(f"Nutrition API returned an unexpected response: {detail}")

    if not exercises:
        print("The Nutrition API found no exercises in that description; nothing was sent to Sheety.")
        return

    today = datetime.now().strftime("%d/%m/%Y")
    time_now = datetime.now().strftime("%H:%M:%S")

    for exercise in exercises:
        if not isinstance(exercise, dict):
            raise RuntimeError("The Nutrition API returned an exercise in an unexpected format.")

        name = exercise.get("name")
        duration = exercise.get("duration_min")
        calories = exercise.get("nf_calories")
        if not isinstance(name, str) or duration is None or calories is None:
            raise RuntimeError(
                "The Nutrition API returned exercise data missing name, duration, or calories."
            )

        sheet_input = {
            "workout": {
                "date": today,
                "time": time_now,
                "exercise": name.title(),
                "duration": duration,
                "calories": calories,
            }
        }

        try:
            sheety_response = requests.post(
                url=sheety_endpoint,
                json=sheet_input,
                headers=SHEETY_HEADERS,
                timeout=30,
            )
        except requests.RequestException as error:
            raise RuntimeError("Could not connect to the Sheety endpoint.") from error

        request_json(sheety_response, "Sheety")
        print(f"Saved {name.title()} workout to Sheety.")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1) from None
