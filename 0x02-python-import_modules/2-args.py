#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    k = len(argv)
    print("{:d} {:s}{:s}".format(k - 1, "argument" if k <= 2 else "arguments",
                                 "." if k == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
