#!/usr/bin/env python3
import sys

def main():
    pos = 50
    cntz = 0

    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        dir_char = line[0].upper()
        try:
            dist = int(line[1:].strip())
        except ValueError:
            continue

        if dir_char == 'L':
            pos = (pos - dist) % 100
        elif dir_char == 'R':
            pos = (pos + dist) % 100
        else:
            continue

        if pos == 0:
            cntz += 1

    print(cntz)

if __name__ == "__main__":
    main()
