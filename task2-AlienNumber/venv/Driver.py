from AlienNumbersConversion import AlienNumbersConversion

try:
    file_name_to_read = input("Please enter file name(it has to be in project directory): \n")
    pointer_to_file_to_read_from = open(file_name_to_read, "r")
except IOError("File name does not exist"):
    exit(-1)

# first line contains number of test cases, which will be in a separate line each after the first line
try:
    int_number_of_test_cases = int(pointer_to_file_to_read_from.readline())
    if int_number_of_test_cases < 0:
        raise ValueError
except ValueError("Invalid input"):
    exit(-1)

list_to_be_written_on_a_file = []

for index_of_line_number in range(int_number_of_test_cases):  # iterate over the lines
    str_test_case = pointer_to_file_to_read_from.readline()  # Get a line that corresponds to a test case

    """ 
    convert the string to a list because strings are immutable objects and we
    need to modify it 
    """

    # remove new line if there is any
    if str_test_case[len(str_test_case) - 1] == '\n':
        str_test_case = str_test_case[:len(str_test_case)-1]

    source_number, source_digits, target_digits = str_test_case.split(' ')
    target_number = AlienNumbersConversion.covert_alien_number_to_target_language(source_number, source_digits,
                                                                                  target_digits)

    test_case_result = str("Case #" + str(index_of_line_number + 1) + ": " + str(target_number) + "\n")
    list_to_be_written_on_a_file.append(test_case_result)

file_to_write_to = input("Enter file name you want to write on: \n")
pointer_to_file_to_write_to = open(file_to_write_to, "w+")

str_to_be_written_on_a_file = "".join(list_to_be_written_on_a_file)
pointer_to_file_to_write_to.write(str_to_be_written_on_a_file)