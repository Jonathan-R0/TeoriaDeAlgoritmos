import sys
from random import choice, randint

if __name__ == "__main__":
    lines = int(sys.argv[1])
    with open(sys.argv[2], "w") as file:
        for i in range(lines):
            first = randint(0, 167)
            second = randint(0, 167)
            while second == first:
                second = randint(0, 167)
            file.write(f"User-{i},{first},{second}\n")
