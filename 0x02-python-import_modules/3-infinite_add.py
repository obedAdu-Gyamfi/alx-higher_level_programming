#!/usr/bin/python3
import sys
if __name__ == "__main__":

    def sum_arg():
        infSum = 0
        for line in sys.argv[1:]:
            infSum += int(line)
        print(f"{infSum}")

    sum_arg()
