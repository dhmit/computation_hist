import copy
import csv
import re
from collections import Counter, defaultdict

from IPython import embed
from nameparser import HumanName

from config.settings import METADATA_CSV


class Person:
    """
    Person stores the information for one person

    """

    def __init__(self, last='', first='', middle='', aliases=[], name_raw='', count=0):

        if name_raw:
            last, first, middle = self.parse_name(name_raw)

        self.last = last
        self.first = first
        self.middle = middle
        # list of other names of this person, e.g. ['Verzuh, F. M.', 'Verzuh Frank M.']
        self.aliases = aliases
        self.count = count

    def __repr__(self):
        return f'{self.last} | {self.first} | {self.middle} '

    def __str__(self):

        first = self.first
        if len(first) == 1:
            first += '.'
        middle = self.middle
        if len(middle) == 1:
            middle += '.'

        return f'{self.last}, {first} {middle}'

    def copy(self):
        return Person(last=self.last, first=self.first, middle=self.middle,
                      aliases=copy.deepcopy(self.aliases), count=self.count)

    def __hash__(self):
        return hash(f'{self.last} {self.first} {self.middle}')

    def parse_name(self, name_raw):
        """
        Parses a raw_name, e.g. "Corbato, F.J." into first, middle, and last name

        >>> p=Person(name_raw='Corbato, F.J.')
        >>> p.last, p.first, p.middle
        ('Corbató', 'F', 'J')

        :param name_raw:
        :return:
        """

        # fix names like "Verzuh M., F.", where the middle name comes after the last name
        # -> it should be Verzuh, F. M.
        match = re.match('([A-Z][a-z]+) ([A-Z])\., ([A-Z][a-z]*)\.*', name_raw)
        if match:
            name_raw = f'{match.groups()[0]}, {match.groups()[2]}. {match.groups()[1]}.'

        name = HumanName(name_raw)

        # If first and middle initials have periods but not spaces -> separate, e.g. "R.K. Teague"
        if re.match('[a-zA-Z]\.[a-zA-Z]\.', name.first):
            name.middle = name.first[2]
            name.first = name.first[0]

        # Capitalize after splitting joined initials, otherwise R.K. becomes R.k. (i.e. middle
        # inital is interpreted as lower case)
        name.capitalize(force=True)

        name.last = name.last
        name.first = name.first.strip('.')
        name.middle = name.middle.strip('.')

        last_name_replacements = [
            ('Corbato', 'Corbató'),
            ('Corbatò', 'Corbató'),
            ('Verguh', 'Verzuh')
        ]
        for replacement in last_name_replacements:
            name.last = name.last.replace(replacement[0], replacement[1])

        return name.last, name.first, name.middle


class PeopleDatabase:
    """
    PeopleDatabase holds information about a set of people. Its primary purpose is to store this
    data to merge duplicate names.
    Lifted from a very similar class from S.R.'s work with tobacco documents

    """

    def __init__(self):
        self.people = set()

    def print_sorted(self):
        """
        Prints all names sorted alphabetically including counts and aliases

        :return:
        """

        for person in sorted(self.people, key=lambda x: x.last):
            print('{:25s}. {:4d}. Aliases: {}'.format(str(person), person.count, person.aliases))

    def get_aliases_to_full_name_dict(self):
        """
        Returns a dictionary of aliases to full names, i.e. names as they appear in the csv to
        authoritative full names.

        >>> people_db = PeopleDatabase()
        >>> people_db.extract_names_from_metadata_sheet()
        >>> aliases_dict = people_db.get_aliases_to_full_name_dict()
        >>> aliases_dict['Corbatò, F. J.']
        'Corbató, Fernando J.'

        :return:
        """
        aliases_to_full_name = {}

        for person in self.people:
            for alias in person.aliases:
                aliases_to_full_name[alias] = str(person)
        return aliases_to_full_name


    def extract_names_from_metadata_sheet(self):
        """
        Extracts all names from the metadata sheet and adds them to its people set

        :return:
        """

        # parse all of the names (not orgs) and add them to a counter
        names_counter = Counter()
        with open(METADATA_CSV) as file:
            csv_file = csv.DictReader(file)

            for line in csv_file:
                for element in ['author', 'recipients', 'cced']:
                    for person_or_org in [p.strip() for p in line[element].split(';')]:
                        # if at least a comma -> most likely a person
                        if len(person_or_org.split(',')) > 1:
                            names_counter[person_or_org] += 1

        # for each element in the counter, add them to the people set.
        for name in names_counter:
            self.people.add(Person(name_raw=name, count=names_counter[name], aliases=[name]))
        self.merge_all_duplicates()

    def merge_all_duplicates(self):
        """
        Tries to identify all duplicates in the dataset and merge them

        :return:
        """

        # create a set of all last names in the dataset and iterate over them.
        last_names = set()
        for person in self.people:
            last_names.add(person.last)

        # run merge operation by running over each last name individually
        for last_name in last_names:

            while True:
                # ugly implementation detail: we modify the people set with every merge -> this
                # dict needs to be regenerated after every merge
                last_names_dict = defaultdict(list)
                for person in self.people:
                    last_names_dict[person.last].append(person)

                people_with_last_name_list = last_names_dict[last_name]

                finished = self.merge_duplicates_of_last_name(people_with_last_name_list)
                if finished:
                    break


    def merge_duplicates_of_last_name(self, people_with_last_name_list):
        """
        Tries to merge the duplicates in a list of people with the same last name
        Returns true if the task is finished (everything that could be merged was merged
        Returns false if more merges could be done.

        :param people_with_last_name_list: list(Person)
        :return: bool
        """

        # if only one name -> already finished
        if len(people_with_last_name_list) == 1:
            return True

        # sort list by count (higher counts are less likely misspellings).
        people_with_last_name_list.sort(key=lambda x: x.count, reverse=True)

        # Compare each person with each other person
        for person1 in people_with_last_name_list:
            for person2 in people_with_last_name_list:

                if person1 == person2:
                    continue

                # if no first and middle name -> continue
                if person1.first == '' and person1.middle == '':
                    continue
                if person2.first == '' and person2.middle == '':
                    continue

                # if first and middle names match exactly -> merge
                if person1.first == person2.first and person1.middle == person2.middle:
                    self.merge_two_persons(person1, person2)
                    return False

                # if both have full first names and they don't match -> skip
                if len(person1.first) > 2 and len(person2.first) > 2 and \
                        person1.first != person2.first:
                    continue

                # if both have full middle names and they don't match -> skip
                if len(person1.middle) > 2 and len(person2.middle) > 2 and \
                        person1.middle != person2.middle:
                    continue

                # if initial of the first name is not the same -> skip
                if person1.first and person2.first and person1.first[0] != person2.first[0]:
                    continue

                # if both have at least first and middle initials
                if person1.first and person1.middle and person2.first and person2.middle:
                    # if first or last initials don't match -> skip
                    if person1.first[0] != person2.first[0] or person1.middle[0] != person2.middle[0]:
                        continue

                    # if first and middle initials match -> merge
                    if person1.first[0] == person2.first[0] and person1.middle[0] == person2.middle[0]:
                        self.merge_two_persons(person1, person2)
                        return False  # we're not finished -> return False

                # if both have the same first name and only one has initials -> merge
                if person1.first and person2.first and \
                        len(person1.first) > 2 and len(person2.first) > 2 and \
                        (person1.middle == '' or person2.middle == ''):
                    self.merge_two_persons(person1, person2)
                    return False # not finished

                # if four people or fewer left with the last name and at least their initials match
                # -> merge (the number 4 is a guesstimate.
                if len(people_with_last_name_list) <= 4 and person1.first and person2.first and \
                        person1.first[0] == person2.first[0]:
                    self.merge_two_persons(person1, person2)
                    return False # not finished

                else:
                    continue

        # if no merges after comparing every person with every other person -> finished
        return True

    def merge_two_persons(self, person1, person2):
        """
        Merges two people and their aliases into one

        :param person1:
        :param person2:
        :return:
        """

        new_p = person1.copy()

        # we know that the last name matches.
        # next, select the longer first and middle names
        # goal: by merging multiple names, we should get full first and middle names.
        for attr in ['first', 'middle']:
            if len(getattr(person2, attr)) > len(getattr(person1, attr)):
                setattr(new_p, attr, getattr(person2, attr))

        new_p.aliases = person1.aliases + person2.aliases
        new_p.count = person1.count + person2.count

        self.people.remove(person1)
        self.people.remove(person2)
        self.people.add(new_p)


if __name__ == '__main__':

    people_db = PeopleDatabase()
    people_db.extract_names_from_metadata_sheet()
    people_db.print_sorted()
