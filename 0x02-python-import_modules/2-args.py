#!/usr/bin/python3
import sys
if __name__ == "__main__":

    def arg_len():
        alist = []
        for line in sys.argv[1:]:
            alist.append(line)
        if len(alist) == 1:
            print(f"{len(alist)} argument:")
        else:
            print(f"{len(alist)} arguments:")
        i = 0
        for i in range(len(alist)):
            print(f"{i+1}: {alist[i]}")
    arg_len()
