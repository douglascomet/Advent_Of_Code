'''
=============================================================================
!/usr/bin/env python
title           :Day_2_1.py
description     :Day 2: Corruption Checksum of Advent Of Code 2017
                https://adventofcode.com/2017/day/2
author          :Doug Halley
date            :2018-01-14
version         :2.0
usage           :
notes           :
python_version  :2.7.14
=============================================================================
'''

# test input provided
# rather than using spreadsheets as an external file
# I create each test case as a dictionary
# so each key was treated as a new row in a spreadsheet
test_1 = {
    1: '5, 1, 9, 5',
    2: '7, 5, 3',
    3: '2, 4, 6, 8'
}

# test puzzle provided
test_2 = {
    1:
        '121, 59, 141, 21, 120, 67, 58, 49, 22, 46, 56, 112, 53, 111, 104, \
        130',
    2:
        '1926, 1910, 760, 2055, 28, 2242, 146, 1485, 163, 976, 1842, 1982, \
        137, 1387, 162, 789',
    3:
        ' 4088, 258, 2060, 1014, 4420, 177, 4159, 194, 2794, 4673, 4092, 681, \
        174, 2924, 170, 3548',
    4:
        '191, 407, 253, 192, 207, 425, 580, 231, 197, 382, 404, 472, 164, \
        571, 500, 216',
    5:
        '4700, 1161, 168, 5398, 5227, 5119, 252, 2552, 4887, 5060, 1152, \
        3297, 847, 4525, 220, 262',
    6:
        '2417, 992, 1445, 184, 554, 2940, 209, 2574, 2262, 1911, 2923, 204, \
        2273, 2760, 506, 157',
    7:
        '644, 155, 638, 78, 385, 408, 152, 360, 588, 618, 313, 126, 172, 220, \
        217, 161',
    8:
        '227, 1047, 117, 500, 1445, 222, 29, 913, 190, 791, 230, 1281, 1385, \
        226, 856, 1380',
    9:
        '436, 46, 141, 545, 122, 86, 283, 124, 249, 511, 347, 502, 168, 468, \
        117, 94',
    10:
        '2949, 3286, 2492, 2145, 1615, 159, 663, 1158, 154, 939, 166, 2867, \
        141, 324, 2862, 641',
    11:
        '1394, 151, 90, 548, 767, 1572, 150, 913, 141, 1646, 154, 1351, 1506, \
        1510, 707, 400',
    12:
        '646, 178, 1228, 1229, 270, 167, 161, 1134, 193, 1312, 1428, 131, \
        1457, 719, 1288, 989',
    13:
        '1108, 1042, 93, 140, 822, 124, 1037, 1075, 125, 941, 1125, 298, 136, \
        94, 135, 711',
    14:
        '112, 2429, 1987, 2129, 2557, 1827, 477, 100, 78, 634, 352, 1637, \
        588, 77, 1624, 2500',
    15:
        '514, 218, 209, 185, 197, 137, 393, 555, 588, 569, 710, 537, 48, 309, \
        519, 138',
    16:
        '1567, 3246, 4194, 151, 3112, 903, 1575, 134, 150, 4184, 3718, 4077, \
        180, 4307, 4097, 1705'
}


def spreadsheet_parser(dict_input):
    '''Rather than using exernal excel files I treated each row as a
    dictionary entry. This function iterates through each dictionary entry
    which contains strings seperated by ', ' by spliting the string into a
    list of just the values and determing the highest and lowest value found
    within the list. Then the difference of the highest and lowest value for
    each row/dictionary entry are added to the total sum.

    Arguments:
        dict_input {dictionary} -- Dictionary of strings to simulate the use
                                    of a excel spreadsheet

    Returns:
        int -- Returns sum of each row/dictionary entry added together
    '''

    sum_difference = 0

    for dict_key, dict_value in dict_input.iteritems():
        print 'dict_key {0}'.format(dict_value)

        # split the psuedo spreadsheet dictionary by the seperator
        split_dict_value = dict_value.split(', ')

        high_num = 0
        low_num = 0
        for element in split_dict_value:

            # initilize high_num and low_num with the first value in the list
            if index == 0:
                high_num = int(element)
                low_num = int(element)
            elif int(element) >= high_num:
                high_num = int(element)
            elif int(element) < low_num:
                low_num = int(element)

            print 'high {0}'.format(high_num)
            print 'low {0}'.format(low_num)

        sum_difference = sum_difference + (high_num - low_num)

        print 'sum {0}'.format(sum_difference)

    return sum_difference


print spreadsheet_parser(test_1)
print spreadsheet_parser(test_2)
