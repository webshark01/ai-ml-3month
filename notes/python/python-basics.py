# ============================================================
# PYTHON BASICS FOR AI/ML
# ============================================================


# ============================================================
# 1. WHILE LOOPS
# ============================================================

accuracy = 0.5

while accuracy < 0.95:
    accuracy = accuracy + 0.1
    print(f"Accuracy now: {accuracy:.2f}")

print("Training Complete")


print("-------------------")


# ============================================================
# 2. FOR LOOPS AND RANGE()
# ============================================================

# range(10) -> 0 to 9

for i in range(10):
    print(i)


# range(start, stop, step)
# Starts at 0, stops before 20, increases by 2

for i in range(0, 20, 2):
    print(i)


# Simulating training epochs

for epoch in range(1, 6):
    print(f"Epoch {epoch}/5 complete")


print("-------------------")


# ============================================================
# 3. FUNCTIONS - CALCULATING ERROR
# ============================================================

def calculate_error(predicted, actual):
    return abs(predicted - actual)


calculated_error = calculate_error(0.8, 0.75)

print(calculated_error)
print(round(calculated_error, 5))


# ============================================================
# 4. FUNCTION - NORMALIZATION
# ============================================================

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)


normalized = normalize(50, 0, 100)

print(normalized)


print("-------------------")


# ============================================================
# 5. DEFAULT PARAMETERS
# ============================================================

def split_score(score, passing=0.6):

    if score >= passing:
        print("Pass")
    else:
        print("Fail")


split_score(1)

# Override the default passing value
split_score(0.6, 0.8)


# ============================================================
# 6. MULTIPLE RETURN VALUES
# ============================================================

def get_stats(numbers):
    return sum(numbers) / len(numbers), max(numbers)


print(get_stats([4, 8, 15, 16, 23, 42]))


print("-------------------")


# ============================================================
# 7. LIST COMPREHENSIONS
# ============================================================

predictions = [0.9, 0.4, 0.8, 0.3, 0.75, 0.2, 0.95]


# Get predictions with confidence greater than 0.7

high_confidence = [
    prediction
    for prediction in predictions
    if prediction > 0.7
]


# General list comprehension pattern:
#
# [value_if_true if condition else value_if_false for item in list]


# Create labels based on prediction value

labels = [
    "positive" if prediction >= 0.5 else "negative"
    for prediction in predictions
]


print(high_confidence)
print(labels)


print("-------------------")


# ============================================================
# 8. IMPORTING MODULES
# ============================================================

# Import the entire math module

import math

print(math.sqrt(144))


# Import only pi from math

from math import pi

print(f"{pi:.4f}")
print(round(pi, 4))


# ============================================================
# 9. RANDOM VALUES
# ============================================================

import random


random_scores = [
    random.random()
    for _ in range(5)
]

print(random_scores)


print("-------------------")


# ============================================================
# 10. NUMPY - FIRST INTRODUCTION
# ============================================================

import numpy as np


data = np.array([5, 10, 15, 20, 25])

print(data)

print(np.mean(data))

print(np.std(data))


print("-------------------")


# ============================================================
# 11. FILE HANDLING and TRY/EXCEPT
# ============================================================

scores = []


with open("notes/python/data.txt", "r") as f:

    lines = f.readlines()


for line in lines:

    try:
        scores.append(float(line))

    except:
        print(f"Skipping invalid line: {line.strip()}")


print(scores)

print(sum(scores) / len(scores))


print("-------------------")


# ============================================================
# 12. BASIC CLASSES / OOP
# ============================================================

class Dataset:

    def __init__(self, name, num_samples):
        self.name = name
        self.num_samples = num_samples

    def info(self):
        print(f"{self.name}: {self.num_samples} samples")


# Create Dataset objects

d1 = Dataset("MNIST", 60000)
d2 = Dataset("CIFAR10", 50000)


# Call the info() method

d1.info()
d2.info()


print("-------------------")


# ============================================================
# 13. MINI PROJECT - STUDENT SCORE ANALYZER
# ============================================================

students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 45},
    {"name": "Zain", "score": 92},
    {"name": "Hina", "score": 60},
    {"name": "Omar", "score": 38},
]


# ------------------------------------------------------------
# Calculate average score
# ------------------------------------------------------------

def calculate_average(students):

    score_list = [
        student["score"]
        for student in students
    ]

    return sum(score_list) / len(score_list)


# ------------------------------------------------------------
# Get names of passing students
# ------------------------------------------------------------

def get_passing_students(students, passing_score=50):

    return [
        student["name"]
        for student in students
        if student["score"] >= passing_score
    ]


# ------------------------------------------------------------
# Convert score into a grade
# ------------------------------------------------------------

def grade_letter(score):

    if score >= 90:
        return "A"

    elif score >= 75:
        return "B"

    elif score >= 50:
        return "C"

    else:
        return "F"


# ------------------------------------------------------------
# Display each student's result
# ------------------------------------------------------------

for student in students:

    print(
        f"{student['name']}: "
        f"{student['score']} -> "
        f"Grade {grade_letter(student['score'])}"
    )


# ------------------------------------------------------------
# Final statistics
# ------------------------------------------------------------

class_average = calculate_average(students)

passing_students = get_passing_students(students)

passing_students_length = len(passing_students)

failed_students = len(students) - passing_students_length


print("Class Average:", round(class_average, 2))

print("Passing Students:", passing_students)

print("Failed Students:", failed_students)


print("-------------------")
