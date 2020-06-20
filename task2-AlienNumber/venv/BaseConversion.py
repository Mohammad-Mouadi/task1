class BaseConversion:

    @staticmethod
    def convert(list_of_source_number_digits: list, int_source_base: int, int_target_base: int) -> list:

        int_number_in_decimal = BaseConversion.convert_to_decimal(list_of_source_number_digits, int_source_base)
        list_of_target_number_digits = BaseConversion.convert_from_decimal(int_number_in_decimal, int_target_base)

        return list_of_target_number_digits

    @staticmethod
    def convert_to_decimal(list_of_source_number_digits: list, source_base: int) -> int:
        int_number_of_digits = len(list_of_source_number_digits)
        int_number_in_decimal = 0

        for index_of_digit in range(int_number_of_digits):
            int_number_in_decimal += list_of_source_number_digits[(index_of_digit + 1) * -1] * \
                                     (source_base ** index_of_digit)
        return int_number_in_decimal

    @staticmethod
    def convert_from_decimal(int_number_in_decimal: int, target_base: int) -> list:
        list_of_digits_in_target_base = []

        while int_number_in_decimal > 0:
            int_digit_in_target_base = int_number_in_decimal % target_base
            list_of_digits_in_target_base.insert(0, int_digit_in_target_base)
            int_number_in_decimal = int_number_in_decimal // target_base

        return list_of_digits_in_target_base
