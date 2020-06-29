import sys


def hello(a, b):
    print("hello and that's your sum: ", a + b)


if __name__ == "__main__":
    print("\nNumber of arguments: ", len(sys.argv) - 1)
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except IndexError:
        print("Two parameters should be provided.")
    except ValueError:
        print("Parameters should be integers.")
    else:
        hello(a, b)

