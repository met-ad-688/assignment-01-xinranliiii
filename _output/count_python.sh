#!/bin/bash

count=$(grep -i "python" questions.csv question_tags.csv | wc -l)

echo "Total lines containing 'python': $count"