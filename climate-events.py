import random
import json
import requests
from datetime import datetime, timedelta
import time

# Define the endpoint URL
url = "http://localhost:8081/climateStream"

# Define event types and their descriptions
event_types = [
    {
        "event_type": "ICE_EVENT",
        "description": "Icy road conditions reported with hazardous visibility."
    },
    {
        "event_type": "SNOW_EVENT",
        "description": "Heavy snow and strong winds are creating hazardous driving conditions."
    },
    {
        "event_type": "FLOOD_EVENT",
        "description": "Severe flooding with rising water levels affecting the area."
    }
]

# Define a list of possible locations
locations = [
    "Intersection 17 & Road 7",
    "Highway 101 - Mile 45",
    "Main Street & 4th Ave",
    "Bridge 5 & River Road",
    "Downtown Crossing & Elm Street"
]

def generate_weather_event():
    # Select a random event type
    event_type_data = random.choice(event_types)

    # Generate the event details
    event = {
        "timestamp": datetime.now().isoformat(),
        "event_id": f"Event_{random.randint(1000, 9999)}",
        "event_type": event_type_data["event_type"],
        "location": random.choice(locations),
        "impact_level": random.choice(["LOW", "MEDIUM", "HIGH"]),
        "source": f"WeatherSensor_{random.randint(1, 20)}",
        "temperature": round(random.uniform(-10.0, 5.0), 1),  # Temperature in Celsius
        "wind_speed": random.randint(10, 100),  # Wind speed in km/h
        "precipitation": round(random.uniform(0.0, 50.0), 1),  # Precipitation in mm
        "description": event_type_data["description"],
        "status": "UNRESOLVED"
    }
    return event

def post_event(event):
    try:
        response = requests.post(url, json=event)
        if response.status_code == 200:
            print(f"Event posted successfully: {event['event_id']}")
        else:
            print(f"Failed to post event: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error posting event: {e}")

if __name__ == "__main__":
    # Generate and post random events continuously
    print("Starting to post random weather events...")
    while True:
        event = generate_weather_event()
        print(f"Generated Event: {json.dumps(event, indent=2)}")
        post_event(event)
        # Wait for a random time interval before sending the next event
        delay = random.randint(5, 15)  # Delay between 5 to 15 seconds
        time.sleep(delay)
