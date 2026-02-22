import requests

#Part 1

api_url = "https://api.coingecko.com/api/v3/simple/price"

parameters = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}

try:
    response = requests.get(api_url, params=parameters, timeout=10)

    if response.status_code == 200:
        result = response.json()
        price = result["bitcoin"]["usd"]
        print("Bitcoin current price:", price, "USD")
    else:
        print("Request failed. Status code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Connection error:", error)


#Part 2

example_url = "https://api.example.com/data?type=latest&limit=5"

print("\nExample URL:")
print(example_url)


#Part 3

javascript_code = """
const element = document.getElementById("location");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        element.innerHTML = "Geolocation is not supported.";
    }
}

function showPosition(position) {
    element.innerHTML =
        "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
}
"""

print("\nJavaScript example:")
print(javascript_code)