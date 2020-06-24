from BaseConversion import *


class AlienNumbersConversion:
    """
    convert_alien_number_to_target_language: takes alien number, digits of alien number in an ascending order and
    digits of target language and returns string of the number in target language
    """

    @staticmethod
    def convert_alien_number_to_target_language(str_alien_number: str, str_alien_digits: str,
                                                str_target_digits: str) -> str:
        """
        Algorithm: This is just a conversion between bases because the digits of the alien language is in an ascending
        order As a result, we can use an array to store each digit of the alien language. Array length is the base of
        the language and the index of each digit represents the digit's actual value in that base.
        """

        alien_digits_list = list(str_alien_digits)
        alien_digits_dict = {}

        for index_of_alien_digit, alien_digit in enumerate(alien_digits_list):
            # the index is to be used as the decimal value of digit
            alien_digits_dict[alien_digit] = index_of_alien_digit

        alien_number_digits_list = list(str_alien_number)

        for index_of_alien_digit, alien_digit in enumerate(alien_number_digits_list):
            alien_number_digits_list[index_of_alien_digit] = alien_digits_dict[alien_digit]

        int_source_base = len(str_alien_digits)
        int_target_base = len(str_target_digits)

        list_of_number_digits_in_target_language = \
            BaseConversion.convert_source_number_to_target_number(alien_number_digits_list, int_source_base,
                                                                  int_target_base)

        target_digits_list = list(str_target_digits)

        for index_of_target_digit, target_digit in enumerate(list_of_number_digits_in_target_language):
            list_of_number_digits_in_target_language[index_of_target_digit] = target_digits_list[target_digit]

        str_number_in_target_language = "".join(list_of_number_digits_in_target_language)

        return str_number_in_target_language
