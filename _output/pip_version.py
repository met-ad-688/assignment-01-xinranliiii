import subprocess

with open("_output/pip3.txt", "w") as f:
    result = subprocess.run(["pip3", "--version"], capture_output=True, text=True)
    f.write(result.stdout)
