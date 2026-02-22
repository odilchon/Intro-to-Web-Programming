import re

text_a = "Hello world, welcome here"
text_b = "This string does not start correctly"

regex = r"Hello"

print("Check with match on text_a:")
m1 = re.match(regex, text_a)
if m1:
    print("Found:", m1.group())
else:
    print("Nothing found")

print("Check with match on text_b:")
m2 = re.match(regex, text_b)
if m2:
    print("Found:", m2.group())
else:
    print("Nothing found")

print("Check with search on text_b:")
s1 = re.search(regex, text_b)
if s1:
    print("Found:", s1.group())
else:
    print("Nothing found")

phones_text = "You can call 555-1234, 555-5678 or 555-9999 anytime."
phone_pattern = r"\d{3}-\d{4}"
found_phones = re.findall(phone_pattern, phones_text)
print("Phones:", found_phones)

numbers_text = "There are 3 apples, 15 oranges, and 256 bananas."
digit_pattern = r"\d+"
changed = re.sub(digit_pattern, "NUMBER", numbers_text)
print("After replace:", changed)

mail_text = "Write to support@example.com or contact@example.org for help."
mail_pattern = r"\b\w+@\w+\.\w+\b"
mail_list = re.findall(mail_pattern, mail_text)
print("Emails:", mail_list)

vowel_text = "An apple a day keeps the doctor away. Even elephants enjoy eating."
vowel_pattern = r"\b[aeiou]\w*\b"
words = re.findall(vowel_pattern, vowel_text, re.IGNORECASE)
print("Words starting with vowel:", words)