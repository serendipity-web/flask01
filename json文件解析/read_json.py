import json

with open('test.json', 'r') as file:
    data = json.load(file)

print(type(data))
