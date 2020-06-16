
def greatest_tidy_number(number):
    try:
        positive_check = int(number)
        if positive_check < 0:
            return "Error: Negative number"

        number = list(number)
        length = len(number)
        for j in range(length - 1):  # we skipped the last element because it will be checked in the previous iteration
            """
            Algorithm: start with the most significant digit, if the next digit is smaller we subtract 1 from the
            current digit if it is greater than the prior digit otherwise subtract 1 from the previous digit,
            and then, replace all of the remaining digits with nines
            """
            if number[j] > number[j + 1]:

                # tmp variable will point to the digit we should decrement by 1
                tmp = j

                # Next while loop will subtract 1 from the current digit or the previous digits
                while tmp != 0 and number[tmp] == number[tmp - 1]:
                    tmp -= 1
                else:
                    number[tmp] = str((int(number[tmp]) - 1))

                for k in range(tmp + 1, length):  # replace remaining digits with 9s
                    number[k] = 9
                break

        list_to_string = ""  # list_to_string is to convert the list to a string

        # convert list to string
        for j in range(len(number)):
            list_to_string += str(number[j])

        number = int(list_to_string)
        return number
    except ValueError:
        return "Invalid number"

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


        num = greatest_tidy_number("".join(test_case_list))

        # convert the string to integer to remove leading zeros
        answer = str("Case #" + str(i + 1) + ": " + str(int(num)) + "\n")
        ans.append(answer)

    file_write = input("Enter file name you want to write on: \n")
    f = open(file_write, "w+")

    f.write("".join(ans))  # .join will convert an iterable, in this case a list to a string

except IOError:
    print("Error opening the file")



