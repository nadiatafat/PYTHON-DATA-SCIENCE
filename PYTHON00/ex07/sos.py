import sys


def morse_code(text):
    """
    Convert a given text string into its Morse code representation.

    Each letter (A-Z), digit (0-9), and space (' ') is converted to its
    corresponding Morse code symbol according to the international standard.
    A space in the input text is represented by '/' in Morse code output.
    """
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }

    text = text.upper()
    morse_list = []
    for char in text:
        if char not in MORSE_CODE:
            print(f"Invalid character: {char}")
            return None
        morse_list.append(MORSE_CODE[char])
    return ' '.join(morse_list)


def main():
    arg = sys.argv[1] if len(sys.argv) == 2 else None
    if arg is None:
        print("Usage: python sos.py <text>")
        return

    for c in arg:
        if not (c.isdigit() or c.isalpha() or c == " "):
            print("Wrong Arg: contains invalid characters")
            return

    morse = morse_code(arg)
    if morse:
        print(morse)


if __name__ == "__main__":
    main()
