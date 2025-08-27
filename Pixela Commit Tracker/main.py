import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# ------------------- Load Environment Variables -------------------
# Load sensitive info from .env file so they are not hardcoded in code

load_dotenv()
USERNAME = os.getenv("PIXELA_USERNAME") # Your Pixela username
TOKEN = os.getenv("PIXELA_TOKEN") # Your Pixela authentication token

# Authentication headers for Pixela API requests
HEADERS = {
    "X-USER-TOKEN": TOKEN
}
pixela_endpoint = "https://pixe.la/v1/users" # Base Pixela API endpoint

# ------------------- Step 1: Create a User (only required once) -------------------
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",  # Required field
    "notMinor": "yes",             # Confirms you're not a minor
}

# Try creating a user account. If it already exists, Pixela returns "already exist"
response_1 = requests.post(url=pixela_endpoint, json=user_params)

if response_1.status_code == 200:
    print("✅ User exists or created successfully")
else:
    print("⚠️ User creation error:", response_1.text)


# ------------------- Step 2: Create a Graph (only required once per graph) -------------------
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",             # Unique graph ID
    "name": "Coding Graph",     # Graph title
    "unit": "commit",           # Measurement unit
    "type": "int",              # Data type (int/float)
    "color": "momiji"           # Graph color
}

# Attempt to create the graph. If the graph already exists, Pixela returns "already exist"
response_2 = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)

if response_2.status_code == 200:
    print("✅ Graph exists or created successfully")
else:
    print("⚠️ Graph creation error:", response_2.text)


# ------------------- Step 3: Add a Pixel (record today's commits) -------------------
graph_post_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now() # Get today’s date
post_config = {
    "date": today.strftime(format="%Y%m%d"),                        # Format: YYYYMMDD
    "quantity": input("How Many Commits did you made Today?: "),    # Ask user for input
}

# Add today's pixel (a data point on the graph)
response_3 = requests.post(url=graph_post_endpoint, json=post_config, headers=HEADERS)

if response_3.status_code == 200:
    print("✅ Pixel added")

elif "already exist" in response_3.text.lower():
    print("ℹ️ Pixel already exists for today")

else:
    print("⚠️ Pixel creation error:", response_3.text)


# ------------------- Step 4: Update a Pixel (modify yesterday's data) -------------------
yesterday = today - timedelta(days=1) # Automatically calculate yesterday’s date (instead of hardcoding)

put_endpoint = f"{graph_post_endpoint}/{yesterday.strftime(format="%Y%m%d")}"
put_config = {
    "quantity": "15" # Updating yesterday's commits to 15
}

# Update yesterday’s pixel if it exists
response_4 = requests.put(url=put_endpoint, json=put_config, headers=HEADERS)

if response_4.status_code == 200:
    print("✅ Pixel updated")
else:
    print("⚠️ Pixel update error:", response_4.text)


# ------------------- Step 5: Delete a Pixel (remove today's data if needed) -------------------
delete_endpoint = f"{graph_post_endpoint}/{today.strftime(format="%Y%m%d")}" # Endpoint to delete today’s pixel (use carefully!)

response_5 = requests.delete(url=delete_endpoint, headers=HEADERS)

if response_5.status_code == 200:
    print("✅ Pixel deleted")
else:

    print("⚠️ Pixel deletion error:", response_5.text)
