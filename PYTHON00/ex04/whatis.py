import sys


# print("Tous les arguments :", sys.argv)
# print("Nom du script :", sys.argv[0])
# print("Premier argument :", sys.argv[1] if len(sys.argv) > 1 else None)


def all_thing_is_obj(nb: int):
    if nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

arg = sys.argv[1] if len(sys.argv) == 2 else None


if arg is not None:
    try:
        nb = int(arg)
        all_thing_is_obj(nb)
    except ValueError:
        print("AssertionError: argument is not an integer")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
else:
    print("AssertionError: missing argument")
