# ============================================================
# PYTHON BASICS FOR AI/ML
# ============================================================


# ============================================================
# 1. PRINTING OUTPUT
# ============================================================

print("I am starting my AI/ML journey")
print("Python is the language of AI")


# ============================================================
# 2. VARIABLES
# ============================================================

# Python variables don't require let, const, or var

model_accuracy = 0.87
dataset_name = "iris"

print("Model trained on", dataset_name, "dataset with accuracy:", model_accuracy)


# ============================================================
# 3. FLOOR DIVISION AND MODULUS
# ============================================================

total_samples = 1000
batch_size = 32

# // gives the number of complete divisions
num_batches = total_samples // batch_size

# % gives the remainder left after division
leftover_samples = total_samples % batch_size

print("Full batches:", num_batches, "Leftover samples:", leftover_samples)

# After making as many complete groups of 32 as possible
# from 1000, how many samples are left?
#
# Modulus (%) returns the remainder left after division.


# ============================================================
# 4. F-STRINGS
# ============================================================

model_name = "ResNet50"
epoch = 5
loss = 0.023

print(f"{model_name} - Epoch {epoch} - Loss: {loss}")


# ============================================================
# 5. BASIC STRING OPERATIONS
# ============================================================

# len() gives the length of a string
print(len(model_name))

# .upper() converts a string to uppercase
print(model_name.upper())


# ============================================================
# 6. COMPARISON OPERATORS AND BOOLEANS
# ============================================================

accuracy = 0.85
min_required = 0.8

passed = accuracy >= min_required

print(passed)

# Boolean values can be True or False
has_overfitting = False

# not reverses a Boolean value
print(not has_overfitting)


# ============================================================
# 7. IF / ELIF / ELSE
# ============================================================

temperature = 0.7

if temperature < 0.3:
    print("Very predictable output")
elif temperature < 0.8:
    print("Balanced output")
else:
    print("Very random output")


print("-------------------")


# ============================================================
# 8. LISTS
# ============================================================

# A list is an ordered collection of values,
# similar to a JavaScript array.

errors = [0.12, 0.9, 0.15, 0.07, 0.11]

print(len(errors))

# Calculate average
print(sum(errors) / len(errors))

print(max(errors))
print(min(errors))


print("-------------------")


# ============================================================
# 9. LIST INDEXING AND SLICING
# ============================================================

scores = [0.85, 0.91, 0.76, 0.88, 0.95]

# Index 1 up to (but not including) index 3
print(scores[1:3])

# From the beginning up to (but not including) index 2
print(scores[:2])

# From index 2 to the end
print(scores[2:])

# Last 2 items
print(scores[-2:])


# More indexing and slicing examples

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(data[:3])
print(data[-3:])
print(data[1:9])
print(data[4])


print("-------------------")


# ============================================================
# 10. TUPLES
# ============================================================

# A tuple is similar to a list, but it cannot be changed
# after it is created (immutable).
#
# Tuples use () instead of [].

image_shape = (64, 64, 3)

print(f"Height: {image_shape[0]}, Width: {image_shape[1]}")

# This would cause an error because tuples are immutable:
# image_shape[0] = 128


print("-------------------")


# ============================================================
# 11. DICTIONARIES
# ============================================================

# A dictionary stores data as key-value pairs.
# Similar to a JavaScript object.

student = {
    "name": "Ali",
    "score": 88,
    "passed": True
}

# Access a value using its key
print(student["name"])

# Update a value
student["score"] = 92

# Add a new key-value pair
student["grade"] = "A"

print(student)


print("-------------------")


# ============================================================
# 12. SETS
# ============================================================

# A set is a collection with two key properties:
# 1. No duplicate values
# 2. No normal indexing/order


labels = ["cat", "dog", "cat", "cat", "bird", "dog"]

# Convert list to set to remove duplicates
unique_labels = set(labels)

print(unique_labels)

# Number of unique labels
print(len(unique_labels))

# Check whether a value exists in the set
print("fish" in unique_labels)


print("-------------------")


# ============================================================
# 13. FOR LOOPS
# ============================================================

scores = [0.8, 0.9, 0.7]

for score in scores:

    if score >= 0.8:
        print(f"{score} - Pass")
    else:
        print(f"{score} - Fail")


# ============================================================
# 14. ENUMERATE()
# ============================================================

# enumerate() gives you both:
# index and value

for i, score in enumerate(scores):
    print(f"Run {i}: {score}")


# ============================================================
# 15. PROCESSING DATA WITH LOOPS
# ============================================================

errors = [0.12, 0.05, 0.20, 0.03, 0.15]

for error in errors:

    if error > 0.1:
        print(f"High error: {error}")
    else:
        print(f"Low error: {error}")


# enumerate() gives index + value

for index, error in enumerate(errors):
    print(f"Run {index}: error = {error}")


print("-------------------")
accuracy = 0.5
while accuracy < 0.95: 
    accuracy = accuracy + 0.1 
    print(f"Accuracy now: {accuracy:.2f}")
print("Training Complete")

print("-------------------")

print("-------------------")

print("-------------------")

print("-------------------")
