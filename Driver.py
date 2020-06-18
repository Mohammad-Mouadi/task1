
from task1.TidyNumberGenerator import *

try:
    file_name = input("Please enter file name(it has to be in project directory): \n")
    f = open(file_name, "r")

    # first line contains number of test cases, which will be in a separate line each after the first line
    number_of_test_cases = f.readline()
    ans = []  # list containing the output, first item is the output of the first test case and so on

    for i in range(int(number_of_test_cases)):  # iterate over the lines
        test_case = f.readline()  # Get a line that corresponds to a test case

        """ 
        convert the string to a list because strings are immutable objects and we
        need to modify it 
        """
        test_case_list = list(test_case)

        # remove new line if there is any
        if test_case_list[len(test_case_list) - 1] == '\n':
            test_case_list.pop(len(test_case_list) - 1)

        num = generate_greatest_tidy("".join(test_case_list))

        # convert the string to integer to remove leading zeros
        answer = str("Case #" + str(i + 1) + ": " + str(int(num)) + "\n")
        ans.append(answer)

    file_write = input("Enter file name you want to write on: \n")
    f = open(file_write, "w+")

    f.write("".join(ans))  # .join will convert an iterable, in this case a list to a string

except IOError:
    print("Error opening the file")
