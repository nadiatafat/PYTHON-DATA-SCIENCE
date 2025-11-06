import sys
import string


def count_element(text: str):
    """
    Count upper, lower letters, ponctuation marks, spaces and digit in a string
    """
    total_chars = len(text)
    upper_letters = sum(1 for c in text if c.isupper())
    lower_letters = sum(1 for c in text if c.islower())
    punctuation_marks = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())
    print(f"The text contains {total_chars} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuation_marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    if len(sys.argv) == 2:
        arg = sys.argv[1]
    elif len(sys.argv) == 1:
        arg = input("What is the text to count?")
    else:
        arg = None

    if arg is not None:
        try:
            count_element(arg)
        except ValueError:
            print("AssertionError")
    else:
        print("AssertionError")


if __name__ == "__main__":
    main()
