import csv

def contribution_counter(metadata="metadata.csv"):
    """
    This function returns a list of people who have contributed metadata.
    It returns a list of tuples where the first element is the person and the
    last element is the number of contributions. The list is ordered with the
    person who has contributed the most appearing first.\

    >>> contribution_counter("dummy_metadata.csv")
    [('stephan', 79), ('assel', 12), ('mingfei', 11), ('samantha', 11), ('elsa', 11), ('carol', 10), ('kate', 5), ('myke', 3), ('dina', 1), ('howard', 1), ('elena', 1), ('felix', 1), ('emily', 1), ('ife', 1), ('sophia', 1), ('isaac', 1), ('keith', 1), ('charlotte', 1), ('kelsey', 1), ('shobhita', 1), ('maritza', 1), ('', 1)]

    :return: list
    """
    number_contributions = {}

    with open(metadata) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person = row["metadata_added_by"]
            if person not in number_contributions.keys():
                number_contributions[person] = 1
            else:
                number_contributions[person] += 1
    return sorted(number_contributions.items(), key=lambda kv: -kv[1])
