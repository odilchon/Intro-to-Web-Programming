#ex 1
my_list = [10, 20, 30, 40 ,50]
my_list.append(60)
my_list.insert(1, 15)
my_list.remove(30)
my_list.reverse()
my_list.sort()
print(my_list)

#task 2
print(my_list[0], my_list[1], my_list[2])
print(my_list[4], my_list[5])
print(my_list[:-1])

#task 3
student= {"name": "alice", "age": 22, "grade": "A+", "subject": "math"}
student.pop("age")
print(student)
print("\n")

#task 4
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference = set1.difference(set2)
print(union_set)
print(intersection_set)
print(difference)
print("\n")

#task 5
colors = ("red", "blue", "green", "red", "yellow")
print(colors.count("red"))
print(colors.index("green"))
print("\n")

#task 6
company = {
    "employees":[
            {"name": "jone", "position": "chef", "salary": 16667},
            {"name": "sara", "position": "decider", "salary": 98765}
    ]
}
print(company.get("employees"))