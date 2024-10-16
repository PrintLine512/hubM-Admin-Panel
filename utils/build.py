import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:

        if sys.argv[1] == "1":
            print("1")
        elif sys.argv[1] == "2":
            print("2")
    else:
        print("Аргумент не был передан.")