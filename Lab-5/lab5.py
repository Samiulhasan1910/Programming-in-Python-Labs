# Lab 05: Functions and Lists

# Exercise 1: Campus Resource Tracker

resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    if len(resources) == 0:
        print("No resources found")
        return
    for r in resources:
        if r[3] < 0:
            print(r[0], r[1], r[2], "Invalid quantity")
        else:
            print(r[0], r[1], r[2], r[3])


def search_by_category(resources, category):
    found = False
    for r in resources:
        if r[2] == category:
            print(r[0], r[1], r[2], r[3])
            found = True
    if found == False:
        print("No resources in category", category)


def find_unavailable(resources):
    found = False
    for r in resources:
        if r[3] == 0:
            print(r[0], r[1], "is not available")
            found = True
    if found == False:
        print("All resources are available")


def search_by_id(resources, resource_id):
    for r in resources:
        if r[0] == resource_id:
            print(r[0], r[1], r[2], r[3])
            return
    print("Resource ID", resource_id, "not found")


print("All resources:")
display_resources(resources)

print("\nElectronics:")
search_by_category(resources, "Electronics")

print("\nUnavailable resources:")
find_unavailable(resources)

# Testing and debugging
print("\nTest 1: Unknown resource ID")
search_by_id(resources, 999)

print("\nTest 2: Negative quantity")
display_resources([[106, "Speaker", "Audio", -2]])

print("\nTest 3: Resource with zero units")
find_unavailable(resources)

print("\nTest 4: Empty resource list")
display_resources([])


# Exercise 2: Student Marks Investigator

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


def calculate_average(marks):
    return sum(marks) / len(marks)


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    for s in students:
        marks = s[2]

        if len(marks) == 0:
            print(s[0], s[1], "No marks found")
            continue

        valid = True
        for m in marks:
            if m < 0 or m > 100:
                valid = False

        if valid == False:
            print(s[0], s[1], "Invalid mark")
            continue

        avg = calculate_average(marks)
        print(s[0], s[1], round(avg, 2), classify_performance(avg))


print("\nStudent report:")
display_report(students)

# Testing and debugging
print("\nTest 1: Equal marks in all assessments")
display_report([[206, "Karim", [75, 75, 75]]])

print("\nTest 2: Tied averages")
display_report([[207, "Rina", [70, 80, 90]], [208, "Sakib", [90, 80, 70]]])

print("\nTest 3: Invalid mark")
display_report([[209, "Joy", [85, 120, 90]]])

print("\nTest 4: No marks")
display_report([[210, "Mitu", []]])
