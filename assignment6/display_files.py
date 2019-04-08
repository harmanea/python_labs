import sys


for arg in sys.argv[1:]:
    with open(arg) as f:
        for line in f:
            print(line.strip())
            response = input()

            if response == 'n':
                break
            if response == 'q':
                exit(0)
