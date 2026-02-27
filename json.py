import json

data = {
    "name": "Azat",
    "age": 18,
    "is_student": True
}

json_string = json.dumps(data)
print(json_string)


data = {"a": 1, "b": 2}

print(json.dumps(data, separators=(',', ':')))


with open("data.json", "r") as f:
    data = json.load(f)

print(data)


data = {"course": "Python", "level": "Intermediate"}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)
