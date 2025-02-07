import subprocess

with open("_output/jupyter.txt", "w") as f:
    result = subprocess.run(["which", "jupyter"], capture_output=True, text=True)
    f.write(result.stdout if result.stdout else "Jupyter is not installed\n")
