def is_valid_integer(str_num):
    try:
        int(str_num)
        return True
    except ValueError:
        return False


def generate_greatest_tidy_number(str_number):
    int_number = 0
    if is_valid_integer(str_number):
        int_number = int(str_number)
    else:
        raise Exception("Invalid input")
    if int_number < 0:
        raise Exception("Negative input")

    list_of_digits = list(str(int_number))  # don't use str_number because it might have a leading '+' sign
    int_number_of_digits = len(list_of_digits)
    for index_for_digits in range(int_number_of_digits - 1):
        # we skipped the last digit because it will be checked in the previous iteration
        """
        Algorithm: start with the most significant digit, if the next digit is smaller we subtract 1 from the
        current digit if it is greater than the prior digit otherwise subtract 1 from the previous digit,
        and then, replace all of the remaining digits with nines
        """

        if list_of_digits[index_for_digits] > list_of_digits[index_for_digits + 1]:

            index_of_digit_to_be_incremented = index_for_digits

            # Next while loop will subtract 1 from the current digit or the previous digits
            while index_of_digit_to_be_incremented != 0 and \
                    list_of_digits[index_of_digit_to_be_incremented] == list_of_digits[index_of_digit_to_be_incremented - 1]:
                index_of_digit_to_be_incremented -= 1
            else:
                int_digit_to_be_decremented = int(list_of_digits[index_of_digit_to_be_incremented])
                int_decremented_digit = int_digit_to_be_decremented - 1
                list_of_digits[index_of_digit_to_be_incremented] = str(int_decremented_digit)

            # replace remaining digits with 9s
            for index_of_digit_to_be_replaced_by_nine in range(index_of_digit_to_be_incremented + 1, int_number_of_digits):
                list_of_digits[index_of_digit_to_be_replaced_by_nine] = '9'
            break

    # convert list to string
    str_number_from_list_of_digits = "".join(list_of_digits)

    int_tidy_number = int(str_number_from_list_of_digits)  # remove leading zeros

    return int_tidy_number
