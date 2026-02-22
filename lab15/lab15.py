#Lab 1
text_file = "notes.txt"
lines = """Python file handling example.
This file was created for testing purposes.
Reading and writing works correctly.
"""

with open(text_file, "w", encoding="utf-8") as f:
    f.write(lines)

print("File created:", text_file)

with open(text_file, "r", encoding="utf-8") as f:
    data_from_file = f.read()

print("File content:")
print(data_from_file)

#Lab 2
import csv

csv_file = "people_data.csv"

rows = [
    ["Name", "Age", "City"],
    ["Anna", "23", "Berlin"],
    ["David", "31", "London"],
    ["Sara", "27", "Paris"]
]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("CSV written:", csv_file)

print("Reading CSV rows:")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#Lab 3
append_file = "notes.txt"
extra_line = "This line was added later.\n"

with open(append_file, "a", encoding="utf-8") as f:
    f.write(extra_line)

print("Data appended to:", append_file)

with open(append_file, "r", encoding="utf-8") as f:
    updated_text = f.read()

print("Updated file content:")
print(updated_text)