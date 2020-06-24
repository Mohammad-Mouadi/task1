class BaseConversion:

    """
    convert_source_number_to_target_number: takes 3 arguments:

    1. list_of_source_number_digits: This is a list containing the decimal value of digits
        For example: if the source number is "FF" and the digits of source number numbering system are "0123456789abcdf"
        which are in an ascending order, this means that f has the decimal value 15, which is the index of 'f'.
        As a result, "FF" should be represented as a list like this [15,15], another example:
         "F5AB70" should be [15,5,10,11,7,0]

    2. int_source_base: the base of the source numbering system a.k.a. number of digits in that system

    3. int_target_base_ the base of the target numbering system a.k.a. number of digits in that system

    Returns: a list containing the decimal value of the digits composing the target number. For example,
    if the target number is "Foo" and the target digits are "oFA", then "Foo" should be returned as [1,0,0]
    """
    @staticmethod
    def convert_source_number_to_target_number(list_of_source_number_digits: list, int_source_base: int, int_target_base: int) -> list:

        int_number_in_decimal = BaseConversion.convert_to_decimal(list_of_source_number_digits, int_source_base)
        list_of_target_number_digits = BaseConversion.convert_from_decimal(int_number_in_decimal, int_target_base)

        return list_of_target_number_digits

    """
    convert_to_decimal: takes 2 arguments: 
    
    1. list_of_source_number_digits: This is a list containing the decimal value of digits
        For example: if the source number is "FF" and the digits of source number numbering system are "0123456789abcdf"
        which are in an ascending order, this means that f has the decimal value 15, which is the index of 'f'.
        As a result, "FF" should be represented as a list like this [15,15], another example:
         "F5AB70" should be [15,5,10,11,7,0]
    
    2. int_source_base: the base of the source numbering system a.k.a. number of digits in that system
    
    Returns: Decimal value of source number after conversion
    """
    @staticmethod
    def convert_to_decimal(list_of_source_number_digits: list, int_source_base: int) -> int:
        int_number_of_digits = len(list_of_source_number_digits)
        int_number_in_decimal = 0

        for index_of_digit, digit in enumerate(list_of_source_number_digits):
            int_exponent = int_number_of_digits - index_of_digit - 1  # we start with the most significant digit
            int_number_in_decimal += digit * (int_source_base ** int_exponent)

        return int_number_in_decimal

    """
    convert_from_decimal: Takes 2 arguments: 
    
    1. int_number_in_decimal: The name says it all
    
    2. int_target_base_ the base of the target numbering system a.k.a. number of digits in that system
    
    Returns: A list having the decimal value of each digit of target number corresponding to the target base
    """
    @staticmethod
    def convert_from_decimal(int_number_in_decimal: int, int_target_base: int) -> list:
        list_of_digits_in_target_base = []

        while int_number_in_decimal > 0:
            int_digit_in_target_base = int_number_in_decimal % int_target_base
            list_of_digits_in_target_base.insert(0, int_digit_in_target_base)
            int_number_in_decimal = int_number_in_decimal // int_target_base

        return list_of_digits_in_target_base
