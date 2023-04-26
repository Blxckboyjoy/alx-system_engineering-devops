import requests
import json

# Make a GET request to the API endpoint
response = requests.get("https://jsonplaceholder.typicode.com/todos")

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    sys.exit(1)

# Parse the JSON response
todos = response.json()

# Group tasks by user ID
tasks_by_user = {}
for todo in todos:
    if todo["userId"] not in tasks_by_user:
        tasks_by_user[todo["userId"]] = []
    tasks_by_user[todo["userId"]].append({"username": todo["title"], "task": todo["title"], "completed": todo["completed"]})

# Export data in JSON format
data = {}
for user_id, tasks in tasks_by_user.items():
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    employee_name = response.json()["name"]
    data[user_id] = [{"username": employee_name, "task": task["task"], "completed": task["completed"]} for task in tasks]

filename = "todo_all_employees.json"
with open(filename, mode="w") as file:
    json.dump(data, file)
