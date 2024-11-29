import json
from datetime import datetime, timedelta
import random
import time
import urllib.request

# Parameters for events
buses = [f"Bus_{i}" for i in range(1, 21)]
event_lifecycle = ["ACCIDENT", "ROAD_CLOSURE", "UPDATE", "ROAD_REOPENING"]

# Dictionary to track ongoing events by event_id
ongoing_events = {}

def generate_event(event_id):
    """Generates a new event or updates an existing event based on its current status."""
    # Check if this event_id already exists to update its state
    if event_id in ongoing_events:
        event = ongoing_events[event_id]
        current_stage = event["event_type"]
        
        if current_stage == "ACCIDENT":
            # Move to a road closure
            event["event_type"] = "ROAD_CLOSURE"
            event["closure_status"] = random.choice(["PARTIAL_CLOSURE", "FULL_CLOSURE"])
            event["status"] = "PROCESSING"
            event["estimated_reopen"] = datetime.now() + timedelta(minutes=random.randint(20, 60))  # Ensure this is a datetime
            
            # Update description
            event["description"] = f"Road closure in effect at {event['location']}."
        
        elif current_stage == "ROAD_CLOSURE":
            # Optionally update or proceed to reopening
            event["event_type"] = random.choice(["UPDATE", "ROAD_REOPENING"])
            if event["event_type"] == "UPDATE":
                event["status"] = "IN_PROGRESS"
                event["description"] = "Closure update: traffic being rerouted."
                # Make sure estimated_reopen is a datetime
                if isinstance(event["estimated_reopen"], str):
                    event["estimated_reopen"] = datetime.fromisoformat(event["estimated_reopen"])
                event["estimated_reopen"] += timedelta(minutes=random.randint(10, 20))
            else:
                event["closure_status"] = "REOPENED"
                event["status"] = "RESOLVED"
                event["description"] = f"Road reopened at {event['location']}."
                event["estimated_reopen"] = None

        elif current_stage == "UPDATE":
            # Proceed to reopening after update
            event["event_type"] = "ROAD_REOPENING"
            event["closure_status"] = "REOPENED"
            event["status"] = "RESOLVED"
            event["description"] = f"Road reopened at {event['location']}."
            event["estimated_reopen"] = None

    else:
        # Create a new event
        location = f"Intersection {random.randint(1, 50)} & Road {random.randint(1, 10)}"
        event = {
            "timestamp": datetime.now().isoformat(),
            "event_id": event_id,
            "event_type": "ACCIDENT",
            "location": location,
            "impact_level": random.choice(["LOW", "MEDIUM", "HIGH"]),
            "source": f"Sensor_{random.randint(1, 20)}",
            "affected_buses": random.sample(buses, k=random.randint(1, 5)),
            "closure_status": "OPEN",
            "estimated_reopen": datetime.now() + timedelta(minutes=random.randint(10, 30)),
            "description": f"Accident reported at {location}.",
            "status": "RECEIVED"
        }
        ongoing_events[event_id] = event

    event["timestamp"] = datetime.now().isoformat()  # Update timestamp for each event log
    if "estimated_reopen" in event and event["estimated_reopen"] is not None:
        event["estimated_reopen"] = event["estimated_reopen"].isoformat()  # Convert to ISO string for JSON output
    return event

def update_json_file(events, filename="traffic_events.json"):
    with open(filename, "w") as json_file:
        json.dump(events, json_file, indent=4)

def simulate_event_generation():
    events = []
    event_counter = 1

    while True:
        event_id = f"Event_{event_counter}"
        event = generate_event(event_id=event_id)

        if event["event_type"] == "ROAD_REOPENING":
            # Remove the event from ongoing_events once resolved
            ongoing_events.pop(event_id, None)
            event_counter += 1  # Increment counter for the next new event

        events.append(event)
        update_json_file(events)
        print(f"Logged event: {event}")

        # Wait a few seconds before generating the next event
        time.sleep(random.randint(2, 5))

# Run the simulation
simulate_event_generation()
