def main():
    get_name()


def get_name():
    name = input("Please enter your name")
    while len(name) <= 0:
        print("Please enter a name")
    print_name(name)


def print_name(name):
    for i in range(0, len(name), 2):
        print(name[i], end='')


main()