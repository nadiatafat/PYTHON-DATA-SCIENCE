from ft_filter import ft_filter
import sys


def main():
    if len(sys.argv) == 3:
        text = sys.argv[1]
        try:
            nb = int(sys.argv[2])
        except ValueError:
            print("AssertionError: second argument should be a number")
            text = None
            nb = -1
    else:
        print("AssertionError: 2 arguments needed")
        text = None
        nb = -1
    if nb >= 0 and text is not None:
        words = text.split()
        # ft_filter(lambda x:len(x) > nb, words)
        print(ft_filter(lambda x: len(x) >= nb, words))


if __name__ == "__main__":
    main()
