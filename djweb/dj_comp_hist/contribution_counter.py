import csv

number_contributions = {}

with open("metadata.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        person = row["metadata_added_by"]
        if person not in number_contributions.keys():
            number_contributions[person] = 1
        else:
            number_contributions[person] += 1
print(sorted(number_contributions.items(), key=lambda kv: -kv[1]))
