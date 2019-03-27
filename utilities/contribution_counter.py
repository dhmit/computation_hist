import csv
from pathlib import Path

from ..config.settings import DATA_DIR

def contribution_counter(metadata=None):
    """
    This function returns a list of people who have contributed metadata.
    It returns a list of tuples where the first element is the person and the
    last element is the number of contributions. The list is ordered with the
    person who has contributed the most appearing first.\

    No actual doctest because the result will change regularly
    > contribution_counter("metadata.csv")
    [('stephan', 79), ('assel', 12), ('mingfei', 11), ('samantha', 11)...]

    :return: list
    """
    if not metadata:
        file_name = METADATA_CSV

    number_contributions = {}

    not_a_member = ["shobhita", "kelsey", "charlotte", "assel",
                    "elsa", "kate", "howard",
                    "emily", "sophia", "isaac",
                    ""]
    with open(metadata) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person = row["metadata_added_by"].lower().strip()
            if person not in number_contributions.keys():
                number_contributions[person] = 1
            elif person:
                number_contributions[person] += 1
    for not_member in not_a_member:
        if not_member in number_contributions:
            del number_contributions[not_member]

    return sorted(number_contributions.items(), key=lambda kv: -kv[1])

if __name__ == "__main__":
    from pprint import pprint
    pprint(contribution_counter())
