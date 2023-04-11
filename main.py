from dictionary_morse import LANGUAGE
from morse import Morse, InputData


def main():
    lang = InputData()
    morse = Morse(lang.language)
    string = input("Please insert string for morse code or decode:")
    print(f"{string}")
    morse.morse_string = string
    print(morse.morse_string)

if __name__ == "__main__":
    main()
