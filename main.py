from morse import Morse

def main():
    morse = Morse()
    print("Example text: Мама мыла раму")
    print("Example morse code: --. .-- --..-- _._._.")
    print ("")
    string = input("Please insert string for morse code or decode:")
    print(f"{string}")
    morse.morse_string = string
    print(morse.morse_string)

if __name__ == "__main__":
    main()
