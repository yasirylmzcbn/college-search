import csv


def highest_in_state(state):
    mostExpName = ""
    mostExpCost = 0
    csv_file = csv.DictReader(open('university-data.csv', 'r', encoding="utf-8"))
    count = 0
    listt = []
    for school in csv_file:
        if school["STABBR"] == state:
            try:
                int(school["TUITIONFEE_IN"])
            except:
                continue
            if mostExpCost < int(school["TUITIONFEE_IN"]):
                mostExpName = school["INSTNM"]
                mostExpCost = int(school["TUITIONFEE_IN"])

    # for i in listt:
    #     x = school["TUITIONFEE_IN"]
    #     if x == '-':
    #         continue
    #     else:
    #         x = int(x)
    #     if mostExpCost < int(school["TUITIONFEE_IN"]):
    #         mostExpCost = int(school["TUITIONFEE_IN"])
    #         mostExpName = school["INSTNM"]
    return mostExpCost, mostExpName