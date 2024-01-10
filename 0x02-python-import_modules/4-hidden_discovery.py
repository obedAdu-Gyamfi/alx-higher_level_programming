#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    mod = dir(hidden_4)

    for i in mod:
        if i[:2] != "__":
            print(i)
