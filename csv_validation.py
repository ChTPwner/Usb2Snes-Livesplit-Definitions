import csv
import os
import sys

with open('default_file.csv', mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        game = row['game']
        filepath = row['filepath']
        if not os.path.exists(filepath):
            sys.exit(f"Error: File for game '{game}' not found at path '{filepath}'.")