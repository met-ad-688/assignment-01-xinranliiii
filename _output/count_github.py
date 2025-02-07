import os

count = sum(1 for root, dirs, files in os.walk(".") for file in files if file.endswith(".py"))

with open("_output/github_python_count.txt", "w") as f:
    f.write(f"Python file count: {count}\n")

