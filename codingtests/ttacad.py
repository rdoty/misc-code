import math
import csv


def guts():
    # basic flow (pseudo code)
    # prompt user for data height, weight
    # load data for height, weight, preference
    # use input in algorithm to calculate guess
    #   One algorithm example:
    #   calculate distance data from user height, weight for all entries
    #   output guess
    # prompt user to confirm guess == preference
    # record data height, weight, preference, guess

    h = float(input('Enter height: '))
    w = float(input('Enter weight: '))

    # Perhaps we'd store the data in a DB with these fields?
    # 'distance','animal','height','weight','guess'
    with open('ahw.csv', 'r') as data_file:
        has_header = csv.Sniffer().has_header(data_file.read(1024))
        data_file.seek(0)  # Rewind
        reader = csv.reader(data_file)
        if has_header:  # Skip header row
            next(reader)
        csv_list = list(reader)

    for row in csv_list:
        row.insert(0, math.sqrt((h - float(row[1])) ** 2 + (w - float(row[2])) ** 2))
    csv_list.sort()
    closest_animals = csv_list[:5]  # The first five are the closest to the given h, w values
    closest_animals = [x[1] for x in closest_animals]
    print closest_animals

    the_guess = max(set(closest_animals), key=closest_animals.count)
    the_prompt = "Is {:s} your preference? y/N ".format(the_guess)
    correct_guess = raw_input(the_prompt)

    # add new entry to csv file
    if correct_guess == 'y':
        new_row = [the_guess, h, w]
    else:
        if the_guess == 'Cat':
            new_row = ['Dog', h, w]
        else:
            new_row = ['Cat', h, w]

    with open('ahw.csv', 'ab') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(new_row)


# Testing stub
if __name__ == "__main__":
    guts()
