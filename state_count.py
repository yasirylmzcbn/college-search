import csv
def state_count(state):
    """
    Returns the number of times a college or university in state is found.

    You're going to want to use the STABBR field and can assume that it's
    case sensitive and will always be the 2 character abbreviation for a
    state
    """
    csv_file = csv.DictReader(open('university-data.csv', 'r', encoding="utf-8"))
    # Do something with the data...
    count = 0
    for st in csv_file:
        if st["STABBR"] == state:
            count += 1

    return count