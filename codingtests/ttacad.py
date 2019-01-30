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


def get_guess(the_input):
    data_list = get_data()
    num_points_to_compare = 5
    for row in data_list:  # calculate distances
        row.insert(0, math.sqrt((the_input[0] - float(row[1])) ** 2 + (the_input[1] - float(row[2])) ** 2))
    data_list.sort()  # find closest values
    closest_data = data_list[:num_points_to_compare]
    is_guess = False if closest_data[0][0] == 0.0 else True  # we already have the value in the database
    closest_animals = [x[1] for x in closest_data]  # Get the animal preferences
    return [max(set(closest_animals), key=closest_animals.count), is_guess]  # Get most common value


def get_input():
    h = float(input('Enter height: '))
    w = float(input('Enter weight: '))
    return [h, w]


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

    h_w_input = get_input()
    the_result = get_guess(h_w_input)

    if the_result[1]:  # If this is a guess - h/w not already in data
        the_confirmation = "Is {:s} your preference? y/N ".format(the_result[0])
        correct_guess = True if raw_input(the_confirmation) == 'y' else False

        # add new entry to csv file
        if correct_guess:
            new_row = [the_result[0], h_w_input[0], h_w_input[1]]
        else:
            new_row = ['Dog', h_w_input[0], h_w_input[1]] if the_result[0] == 'Cat'\
                else ['Cat', h_w_input[0], h_w_input[1]]

        with open('ahw.csv', 'ab') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(new_row)
    else:
        print "Found preference for Height: {:f}, Weight: {:f}. Preference: {:s}"\
            .format(h_w_input[0], h_w_input[1], the_result[0])


# Testing stub
if __name__ == "__main__":
    guts()
