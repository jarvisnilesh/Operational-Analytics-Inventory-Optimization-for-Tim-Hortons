import requests


def get_google_reviews(api_key, place_id):
    # Endpoint for Place Details
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJk8HOnQ0uO4gRArWB-BBRq_Y&fields=name,rating,reviews&key={api_key}"


    response = requests.get(url)
    data = response.json()

    if data.get('status') == 'OK':
        place_name = data['result']['name']
        reviews = data['result'].get('reviews', [])
        print(f"Reviews for {place_name}:")
        for review in reviews:
            print(f"Author: {review['author_name']}")
            print(f"Rating: {review['rating']}")
            print(f"Review: {review['text']}\n")
    else:
        print(f"Error: {data.get('status')}")


# Google API key
API_KEY = 'YOUR_GOOGLE_API_KEY'


PLACE_ID = 'ChIJk8HOnQ0uO4gRArWB-BBRq_Y'  # Google Place ID

# Fetch reviews
get_google_reviews(API_KEY, PLACE_ID)