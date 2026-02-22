import json

#lab 1
person_data = {
    "name": "Daniel",
    "age": 22,
    "subjects": ["Physics", "Chemistry", "Biology"]
}

json_result = json.dumps(person_data, indent=4)
print("JSON output:")
print(json_result)
print()

#lab 2
json_text = """
{
    "name": "Daniel",
    "age": 22,
    "subjects": ["Physics", "Chemistry", "Biology"]
}
"""

python_object = json.loads(json_text)
print("Converted back to Python object:")
print(python_object)
print()

#lab 3
file_name = "data_student.json"

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(person_data, f, indent=4)

print("Data saved to file:", file_name)

with open(file_name, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("Data loaded from file:")
print(loaded_data)