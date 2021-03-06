FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for element in data:
        new_element = element.rstrip()
        info = list(new_element.split(","))
        print("{} is taught by {} and has {} students".format(info[0], info[1], info[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    input_data = list(input_file)
    input_file.close()
    return input_data


main()
