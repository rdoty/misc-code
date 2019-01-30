import math
import csv


def get_data():
    # Perhaps we'd store the data in a DB with these fields?
    # 'distance','animal','height','weight','guess'
    with open('ahw.csv', 'r') as data_file:
        has_header = csv.Sniffer().has_header(data_file.read(1024))
        data_file.seek(0)  # Rewind
        reader = csv.reader(data_file)
        if has_header:  # Skip header row
            next(reader)
        ret_val = list(reader)

    return ret_val


def get_guess(h, w):
    data_list = get_data()
    num_points_to_compare = 5
    for row in data_list:  # calculate distances
        row.insert(0, math.sqrt((h - float(row[1])) ** 2 + (w - float(row[2])) ** 2))
    data_list.sort()  # find closest values
    closest_animals = data_list[:num_points_to_compare]
    closest_animals = [x[1] for x in closest_animals]  # Get the animal preferences
    return max(set(closest_animals), key=closest_animals.count)  # Get most common value


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

    the_guess = get_guess(h, w)

    the_prompt = "Is {:s} your preference? y/N ".format(the_guess)
    correct_guess = True if raw_input(the_prompt) == 'y' else False

    # add new entry to csv file
    if correct_guess:
        new_row = [the_guess, h, w]
    else:
        new_row = ['Dog', h, w] if the_guess == 'Cat' else ['Cat', h, w]

    with open('ahw.csv', 'ab') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(new_row)


# Testing stub
if __name__ == "__main__":
    guts()
