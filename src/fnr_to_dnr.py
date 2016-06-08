#!/usr/bin/python

import sys

weights1 = [3, 7, 6, 1, 8, 9, 4, 5, 2, 1, 0]
weights2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

def create_dnr(nums):
    cont_digit_1 = 0
    cont_digit_2 = 0
    for i in range(0, 9):
        cont_digit_1 = cont_digit_1 + weights1[i] * nums[i]
        cont_digit_2 = cont_digit_2 + weights2[i] * nums[i]

    res_1 = 0 if (cont_digit_1 % 11 == 0) else 11 - (cont_digit_1 % 11)
    nums.append(res_1)

    cont_digit_2 = cont_digit_2 + weights2[9] * nums[9]

    res_2 = 0 if (cont_digit_2 % 11 == 0) else 11 - (cont_digit_2 % 11)
    nums.append(res_2)

    return ''.join(str(e) for e in nums)


def loop_generate_dnr(fnr):
    print 'Creating D-number from input argument: ' + fnr
    nums = map(int, list(fnr))
    nums = nums[:9]
    nums[0] += 4

    dnr = ''
    while len(dnr) != 11:
        dnr = create_dnr(nums)

        if len(dnr) == 11 or (nums[7] == 0 and nums[8] == 0):
            break
        newnum = str(nums[7]) + str(nums[8])
        print newnum
        newnum = str(int(newnum) - 1)
        nums[7] = int(newnum[0]) if int(newnum) > 9 else 0
        nums[8] = int(newnum[1]) if int(newnum) > 9 else int(newnum)
    return dnr


def main():
    if len(sys.argv) < 2:
        print 'Usage: fnr_to_dnr <fnr>'
        sys.exit(0)

    fnr = sys.argv[1]
    fnr_len = len(fnr)
    if fnr_len < 9:
        print 'Length of input is', fnr_len, \
            ",must be at least 9 (Norwegian SSN-numbers are 11 digits, but the two last digits are not used in this case)."
        sys.exit(0)

    if fnr_len > 9:
        print 'Input fnr is too long (' + str(fnr_len) + '), truncating to:' + fnr[:9]

    if int(fnr[2:4]) not in range(1, 13):
        print 'Invalid month specified: ' + fnr[2:4]
        sys.exit(0)

    if int(fnr[:2]) == 0:
        print 'Invalid day specified: 00'
        sys.exit(0)

    month_len = [0, 31, 29, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][int(fnr[2:4])]
    if int(fnr[:2]) > month_len:
        print 'Day: ' + fnr[2:4] + 'specified, but specified month only has ' + month_len + 'days.'

    dnr = loop_generate_dnr(fnr)
    if dnr != '':
        print 'Valid dnr: ' + dnr
    else:
        print 'Could not create a valid dnr from the fnr.'
        print 'This can happen due to the way D-numbers are specified.'

if __name__ == "__main__":
    main()



