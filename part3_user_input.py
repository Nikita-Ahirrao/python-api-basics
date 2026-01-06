"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate

Learn:
- Using input() to make dynamic API requests
- Building URLs with f-strings
- Query parameters in URLs
"""

import requests


def get_user_info():
    """Fetch user info based on user input."""
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ").strip()

    if not user_id.isdigit():
        print("❌ Please enter a valid number.")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\n❌ User with ID {user_id} not found!")


def search_posts():
    """Search posts by user ID."""
    print("\n=== Post Search ===\n")

    user_id = input("Enter user ID to see their posts (1-10): ").strip()

    if not user_id.isdigit():
        print("❌ Please enter a valid number.")
        return

    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("❌ Failed to fetch posts.")
        return

    posts = response.json()

    if posts:
        print(f"\n--- Posts by User #{user_id} ---")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found for this user.")


def get_crypto_price():
    """Fetch cryptocurrency price based on user input."""
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins:")
    print("btc-bitcoin, eth-ethereum, doge-dogecoin")

    coin_id = input("Enter coin ID: ").lower().strip()

    if not coin_id:
        print("❌ Coin ID cannot be empty.")
        return

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data['quotes']['USD']['price']
        change_24h = data['quotes']['USD']['percent_change_24h']

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")
    else:
        print(f"\n❌ Coin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")


def main():
    """Main menu for the program."""
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1–4.")


if __name__ == "__main__":
    main()

# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)

def get_weather():
    print("\n=== Weather Checker ===\n")

    city = input("Enter city name: ").strip()

    if not city:
        print("❌ City name cannot be empty.")
        return

    # Step 1: Get latitude & longitude
    geo_url = "https://geocoding-api.open-meteo.com/v1/search?name=Mumbai"
    geo_response = requests.get(geo_url, params={"name": city})

    if geo_response.status_code != 200:
        print("❌ Failed to fetch location data.")
        return

    geo_data = geo_response.json()

    if "results" not in geo_data:
        print("❌ City not found.")
        return

    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]

    # Step 2: Fetch weather
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    weather_response = requests.get(weather_url, params=weather_params)

    if weather_response.status_code == 200:
        weather = weather_response.json()["current_weather"]
        print(f"\n🌤 Weather in {city.title()}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")
    else:
        print("❌ Could not fetch weather data.")

#
# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false

def search_todos():
    print("\n=== Todo Search ===\n")

    status = input("Enter status (true / false): ").lower().strip()

    if status not in ["true", "false"]:
        print("❌ Please enter only true or false.")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"completed": status})

    if response.status_code != 200:
        print("❌ Failed to fetch todos.")
        return

    todos = response.json()
    print(f"\nFound {len(todos)} todos (completed={status})")

    for todo in todos[:5]:  # show first 5
        print(f"- {todo['title']}")
        


# Exercise 3: Add input validation (check if user_id is a number)

def get_user_info():
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ").strip()

    # ✅ INPUT VALIDATION
    if not user_id.isdigit():
        print("❌ Invalid input! Please enter a number only.")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")
        
    
