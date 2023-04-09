#Morse coding and encoding realisation
import re
from dictionary_morse import MORSE_DICT, LANGUAGE


class InsufficientAmount(Exception):
    '''Custom exception'''
    pass

class Morse:
    '''Morse preparation. Encode and Decode data'''

    def __init__(self, language='ru'):

        self.__decoded = ""
        self.__coded = []
        self.__language = LANGUAGE.index(language)


    @property
    def morse_string(self):
        return (self.__coded, self.__decoded)


    @morse_string.setter
    def morse_string(self, string):
        result = self.check_data(string)

        match result:
            case "morse":
                self.__decoded = self.decode()
            case "text":
                self.__decoded = string
                self.__coded = self.encode()
            case _:
                raise InsufficientAmount(result)

        return (self.__coded, self.__decoded)


    def check_data(self, string):

        is_morse_pattern = "^[-.\s]+$"

        if re.match(is_morse_pattern, string):
            self.__coded = string.split(" ")
            unsufficient_symbols = [each_code for each_code in self.__coded if not MORSE_DICT.get(each_code)]
            print(f"Morse decode {unsufficient_symbols}")
            if not unsufficient_symbols:
                return "morse"

        else:
            all_possible_symbols =  [symbol[self.__language] for symbol in MORSE_DICT.values()]
            unsufficient_symbols = [symbol.upper() for symbol in string if symbol.upper() not in all_possible_symbols]
            print(f"Morse encode {unsufficient_symbols}")
            if not unsufficient_symbols :
                return "text"


        return unsufficient_symbols


    def encode(self):

        self.__coded.clear()
        unique_symbols = set(self.__decoded.upper())
        dict_from_unique_symbols = dict.fromkeys(unique_symbols,"*")

        for key, each_element_dict in MORSE_DICT.items():
            dict_from_unique_symbols[each_element_dict[0]] = key

        for element in self.__decoded.upper():
            self.__coded.append(dict_from_unique_symbols[element])

        return self.__coded


    def decode(self):

        decoded = ''.join([MORSE_DICT.get(element)[0].lower() for element in self.__coded])

        return decoded



def main():
    morse = Morse()

    morse.morse_string = "мама10!"
    print(morse.morse_string)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
