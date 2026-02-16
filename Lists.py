# Function to determine letter grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Student name
name = input("Enter student name: ")

# Five grades (no loops)
g1 = float(input("Enter a grade: "))
g2 = float(input("Enter a grade: "))
g3 = float(input("Enter a grade: "))
g4 = float(input("Enter a grade: "))
g5 = float(input("Enter a grade: "))

# list
grades = [g1, g2, g3, g4, g5]

# average
average = sum(grades) / len(grades)

# Print results
print()
print(name)
print()
print("Average:", average)
print()
print("Letter Grade:", get_letter_grade(average))
