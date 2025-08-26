import requests

# -------------------- API Parameters --------------------
parameters = {
    "amount": 20,  # number of questions you want
    "type": "boolean" # True/False questions
}

# -------------------- Fetch Questions --------------------
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"] # Extract the "results" list from JSON response
