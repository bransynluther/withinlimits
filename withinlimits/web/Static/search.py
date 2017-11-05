import requests
import json

def RestSearch(lat, lon, budget, radius=5000):

    if budget < 10.00:
        budget = 1
    elif budget < 30.00:
        budget = 2
    elif budget < 60:
        budget = 3
    else:
        budget = 4

    params = {
        "key" : "AIzaSyBkgq6skqj_3s0ME2aQHUmq6N_EJ4iADKs",
        "location": lat + "," + lon,
        "radius": radius,
        "maxprice" : budget,
        "type":"restaurant"
    }
    response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json", params)

    results = json.loads(response)
