class BaseConversion:

    @staticmethod
    def convert( list_of_number_in_source_base: list, source_base: int, target_base:int) -> list:
        int_number_in_decimal= BaseConversion.convert_to_decimal(list_of_number_in_source_base,source_base)
        list_number_in_target_base=BaseConversion.convert_from_decimal(int_number_in_decimal,target_base)
        return (list_number_in_target_base)
       
    @staticmethod
    def convert_to_decimal( list_of_number_digits_in_source_base:list, source_base: int) -> int:
        number_of_digits = len(list_of_number_digits_in_source_base)
        int_number_in_decimal = 0
        
        for index_of_digit_in_number_in_source_base,digit_in_number_in_source_base in enumerate(list_of_number_digits_in_source_base):
            int_number_in_decimal += list_of_number_digits_in_source_base[number_of_digits - index_of_digit_in_number_in_source_base - 1] \
                                     * source_base ** index_of_digit_in_number_in_source_base
            
        return int_number_in_decimal
    
    @staticmethod
    def convert_from_decimal(int_number_in_decimal: int,target_base:int) -> list:
        list_of_digits_in_target_base =[]
        
        while int_number_in_decimal>0:
            int_digit_in_target_base = int_number_in_decimal%target_base
            list_of_digits_in_target_base.insert(0,int_digit_in_target_base)
            int_number_in_decimal = int_number_in_decimal//target_base
        
        return list_of_digits_in_target_base
        