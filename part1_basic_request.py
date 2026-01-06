"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner

Learn: How to make a simple GET request and view the response.

We'll use JSONPlaceholder - a free fake API for testing.
"""

import requests

# Step 1: Define the API URL
url = "https://www.aileela.com/course/deep-learning-full-stack-deployment/learn?chapter=flask-basics"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("=== Basic API Request ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())

### Exercise 1: Change the URL to fetch post number 5
#             Hint: Change /posts/1 to /posts/5

import requests

url = "https://jsonplaceholder.typicode.com/posts/5"

response = requests.get(url)

print("Exercise 1: Fetch Post 5")
print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())

# Exercise 2: Fetch a list of all users
#             URL: https://jsonplaceholder.typicode.com/users

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Exercise 2: Fetch All Users")
print("Status Code:", response.status_code)

users = response.json()
print("Total Users:", len(users))

for user in users:
    print(user["name"], "-", user["email"])


# Exercise 3: What happens if you fetch a post that doesn't exist?
#             Try: https://jsonplaceholder.typicode.com/posts/999

import requests

url = "https://jsonplaceholder.typicode.com/posts/999"

response = requests.get(url)

print("Exercise 3: Fetch Invalid Post")
print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())
