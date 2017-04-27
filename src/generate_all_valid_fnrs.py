#!/usr/bin/python

import sys
import random
import argparse

print 'Usage: ./generate_all_valid_fnrs.py <birth_date: ddmmyy> <opt indiv: two digits> <opt sex: m/f>'

if len(sys.argv) < 2:
    sys.exit(1)

birth_date = sys.argv[1]

if len(birth_date) != 6:
    print 'Invalid date (ddmmyy) specified: ' + birth_date
    sys.exit(0)

random.seed()

ij = sys.argv[2] if (len(sys.argv) > 2) else None

if len(sys.argv) > 3:
    s = sys.argv[3]
    if s == "f":
        sex = [0, 2, 4, 6, 8]
    elif s == "m":
        sex = [1, 3, 5, 7, 9]
    elif int(s) in range(0, 10):
        sex = [int(s)]
    else:
        print 'Invalid argument for specification of sex: ' + s
        sys.exit(0)
else:
    sex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

printed = 0
if ij is None:
    for i in range(5):
        for j in range(10):
            for k in sex:
                e = birth_date + str(i) + str(j) + str(k)
                k1 = 11-((3*int(e[0]) + 7*int(e[1]) + 6*int(e[2]) + 1*int(e[3]) + 8*int(e[4]) + 9*int(e[5]) +
                          4*int(e[6]) + 5*int(e[7]) + 2*int(e[8])) % 11)
                k2 = 11-((5*int(e[0]) + 4*int(e[1]) + 3*int(e[2]) + 2*int(e[3]) + 7*int(e[4]) + 6*int(e[5]) +
                          5*int(e[6]) + 4*int(e[7]) + 3*int(e[8]) + 2*k1) % 11)
                if k1 == 10 or k2 == 10:
                    continue
                if k1 == 11:
                    k1 = 0
                if k2 == 11:
                    k2 = 0
                e += str(k1) + str(k2)
                printed += 1
                print(str(e))
else:
    for k in sex:
        e = birth_date + str(ij) + str(k)
        k1 = 11-((3*int(e[0]) + 7*int(e[1]) + 6*int(e[2]) + 1*int(e[3]) + 8*int(e[4]) + 9*int(e[5]) + 4*int(e[6]) + 5*int(e[7]) + 2*int(e[8]))%11)
        k2 = 11-((5*int(e[0]) + 4*int(e[1]) + 3*int(e[2]) + 2*int(e[3]) + 7*int(e[4]) + 6*int(e[5]) + 5*int(e[6]) + 4*int(e[7]) + 3*int(e[8]) + 2*k1)%11)
        if k1 == 10 or k2 == 10:
            continue
        if k1 == 11:
            k1 = 0
        if k2 == 11:
            k2 = 0
        e += str(k1) + str(k2)
        printed += 1
        print str(e)

if printed == 0:
    print 'Invalid parameters, no fnrs passed the control-check. Try different optional number arguments.'
