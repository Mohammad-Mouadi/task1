from BaseConversion import *


class AlienNumbersConversion:

    @staticmethod
    def covert_alien_number_to_target_language(str_alien_number: str, str_alien_digits: str, str_source_digits: str) -> str:
        """
        Algorithm: This is just a conversion between bases because the digits of the alien language is in an ascending order
        As a result, we can use an array to store each digit of the alien language. Array length is the base of the language
        and the index of each digit represents the digit's actual value in that base.
        """

        alien_digits_list = list(str_alien_digits)
       # alien_digits_dict = {}

        target_digits_list = list(str_source_digits)
        str_alien_number = list(str_alien_number)



        # the index is also the value of the alien digit in the language base
        for index_of_digit_in_language_base in range(len(alien_digits_list)):
            for index_of_alien_digit, alien_digit in enumerate(str_alien_number):
                if alien_digit == alien_digits_list[index_of_digit_in_language_base]:
                    str_alien_number[index_of_alien_digit] = int(index_of_digit_in_language_base)

        list_number_in_source_language = BaseConversion.convert(str_alien_number, len(str_alien_digits),
                                                                len(str_source_digits))

        for i in len(list_number_in_source_language):
            list_number_in_source_language = target_digits_list[list_number_in_source_language[i]]

        str_number_in_source_language = "".join(list_number_in_source_language)

        return str_number_in_source_language
