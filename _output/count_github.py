import os

count = 0
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            count += 1

print(f"Python file count: {count}")

