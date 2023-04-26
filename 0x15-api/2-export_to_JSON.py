import requests
import sys
import json

if len(sys.argv) != 2:
    print("Usage: python3 script.py EMPLOYEE_ID")
    sys.exit(1)

employee_id = sys.argv[1]

# Make a GET request to the API endpoint
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    sys.exit(1)

# Parse the JSON response
todos = response.json()

# Count the number of completed tasks
completed_tasks = [todo for todo in todos if todo["completed"]]
num_completed_tasks = len(completed_tasks)

# Print the employee's name and TODO list progress
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_name = response.json()["name"]
num_total_tasks = len(todos)
print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{num_total_tasks}):")

# Print the titles of completed tasks
for todo in completed_tasks:
    print(f"\t{todo['title']}")

# Export data in JSON format
data = {"USER_ID": []}
for todo in todos:
    data["USER_ID"].append({"task": todo["title"], "completed": todo["completed"], "username": employee_name})

filename = f"{employee_id}.json"
with open(filename, mode="w") as file:
    json.dump(data, file)
