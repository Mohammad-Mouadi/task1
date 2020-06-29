class AlienNumbersConverter:

    def __init__(self, str_test_case: str):
        self.__validate_input_type(str_test_case)
        self.__validate_input_format(str_test_case)
        self.str_source_num, self.str_source_digits, self.str_target_digits = str_test_case.split(' ')
        self.int_source_base = len(self.str_source_digits)
        self.int_target_base = len(self.str_target_digits)

    def __validate_input_type(self, str_test_case: str):
        if not isinstance(str_test_case, str):
            raise TypeError("Invalid type")

    def __validate_input_format(self, str_test_case: str):
        list_strings = str_test_case.split(' ')
        if len(list_strings) != 3:
            raise Exception("Invalid input format")

        for char in list_strings[0]:
            if not char in list_strings[1]:
                raise Exception("Invalid input format: Source number has unknown digits")

        if self.__has_dublicates(list_strings[1]) or self.__has_dublicates(list_strings[2]):
            raise Exception("Invalid input format: dublicate digits")

    def __has_dublicates(self, str_test_case: str):
        if len(str_test_case) == len(set(str_test_case)):
            return False
        return True

    # NOTE: what is better approach and why:
    # make covert to decimal return a value int, or create an instance variable called number_in_decimal

    def __convert_to_decimal(self) -> int:
        source_num_digits_list = list(self.str_source_num)

        for index, digit in enumerate(source_num_digits_list):
            source_num_digits_list[index] = self.str_source_digits.find(digit)

        int_number_of_digits = len(self.str_source_num)
        int_number_in_decimal = 0

        for index, digit in enumerate(source_num_digits_list):
            int_exponent = int_number_of_digits - index - 1  # we start with the most significant digit
            int_number_in_decimal += digit * (self.int_source_base ** int_exponent)
        return int_number_in_decimal  #

    def __convert_from_decimal(self, int_number: int) -> str:
        list_of_digits = []

        while int_number > 0:
            int_digit_in_target_base = int_number % self.int_target_base
            list_of_digits.insert(0, str(int_digit_in_target_base))
            int_number = int_number // self.int_target_base

        return "".join(list_of_digits)

    def __str__(self):
        print("Source number: {}, Source digits: {}, Target digits: {}".format(self.str_source_num,
                                                                               self.str_source_digits,
                                                                               self.str_target_digits))

    def convert(self) -> str:
        """
        Algorithm: This is just a conversion between bases because the digits of the alien language is in an ascending
        order As a result, we can use an array to store each digit of the alien language. Array length is the base of
        the language and the index of each digit represents the digit's actual value in that base.
        """
        int_num_in_decimal = self.__convert_to_decimal()

        str_num_in_target_base = self.__convert_from_decimal(int_num_in_decimal)

        list_of_num_digits_in_target_base = list(str_num_in_target_base)

        for index, digit in enumerate(list_of_num_digits_in_target_base):
            list_of_num_digits_in_target_base[index] = self.str_target_digits[int(digit)]

        return "".join(list_of_num_digits_in_target_base)
