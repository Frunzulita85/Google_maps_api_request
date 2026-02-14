import requests
import csv

API_KEY = "AIzaSyDejS-pbufYh2vyTI-N6QXJxwJ7uFvSsqw"
URL = "https://places.googleapis.com/v1/places:searchText"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": (
        "places.displayName,"
        "places.formattedAddress,"
        "places.rating,"
        "places.userRatingCount,"
        "places.id"
    )
}

queries = [

    "brutarie Tractorul Brasov",
    "brutarie Noua–Darste Brasov",
    "brutarie Astra (Steagul Rosu) Brasov",
    "brutarie Valea Cetatii Brasov",
    "brutarie Florilor–Craiter Brasov",
    "brutarie Centrul Nou–Centrul Civic Brasov",
    "brutarie Bartolomeu Brasov",
    "brutarie Centrul Vechi Brasov",
    "brutarie Prund–Schei Brasov",
    "brutarie Triaj Brasov",
    # "burger Brasov"
    # "centru spa Rasnov"
]

places = {}

for q in queries:
    payload = {
        "textQuery": q,
        "languageCode": "ro"
    }

    response = requests.post(URL, headers=headers, json=payload)
    data = response.json()

    for place in data.get("places", []):
        places[place["id"]] = {
            "name": place["displayName"]["text"],
            "address": place.get("formattedAddress"),
            "rating": place.get("rating"),
            "user_ratings_total": place.get("userRatingCount"),
            "place_id": place.get("id")
        }

# numerotare
results = []
for i, p in enumerate(places.values(), start=1):
    p["nr"] = i
    results.append(p)

filename = "brutarii_brasov.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["nr", "name", "address", "rating", "user_ratings_total", "place_id"]
    )
    writer.writeheader()
    writer.writerows(results)

print(f"✅ {len(results)} cluburi UNICE salvate în {filename}")
