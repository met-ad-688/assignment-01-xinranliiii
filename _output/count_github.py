import pandas as pd

files = [
    "/home/ubuntu/github-classroom/met-ad-688/assignment-01-xinranliiii/question_tags.csv",
    "/home/ubuntu/github-classroom/met-ad-688/assignment-01-xinranliiii/questions.csv"
]

count = 0
chunk_size = 100000

for file in files:
    print(f"Processing {file}...")
    for chunk in pd.read_csv(file, encoding='utf-8', on_bad_lines='skip', chunksize=chunk_size, low_memory=True):
        count += chunk.astype(str).apply(lambda col: col.str.contains("GitHub", case=False, na=False)).any(axis=1).sum()

print(f"Total lines containing 'GitHub': {count}")