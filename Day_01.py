#-*- coding: utf-8 -*-
"""
Day 01 solutions for Advent of Code 2018 (https://www.adventofcode.com/2018)

--- Day 1: Chronal Calibration ---

--- Part One ---

"We've detected some temporal anomalies," one of Santa's Elves at the Temporal Anomaly Research and
Detection Instrument Station tells you. She sounded pretty worried when she called you down here.
"At 500-year intervals into the past, someone has been changing Santa's history!"

"The good news is that the changes won't propagate to our time stream for another 25 days, and we
have a device" - she attaches something to your wrist - "that will let you fix the changes with
no such propagation delay. It's configured to send you 500 years further into the past every
few days; that was the best we could do on such short notice."

"The bad news is that we are detecting roughly fifty anomalies throughout time; the device will
indicate fixed anomalies with stars. The other bad news is that we only have one device and
you're the best person for the job! Good lu--" She taps a button on the device and you suddenly
feel like you're falling. To save Christmas, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent
calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one
star. Good luck!

After feeling like you've been falling for a few minutes, you look at the device's tiny screen.
"Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain
destination lock." Below the message, the device shows a sequence of changes in frequency (your
puzzle input). A value like +6 means the current frequency increases by 6; a value like -3
means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a
frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.

In this example, the resulting frequency is 3.
Here are other example situations:
+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6

Starting with a frequency of zero, what is the resulting frequency after all of the changes in
frequency have been applied?

Your puzzle answer was 402.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

You notice that the device repeats the same frequency change list over and over. To calibrate the
device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

    Current frequency  0, change of +1; resulting frequency  1.
    Current frequency  1, change of -2; resulting frequency -1.
    Current frequency -1, change of +3; resulting frequency  2.
    Current frequency  2, change of +1; resulting frequency  3.
    (At this point, the device continues from the start of the list.)
    Current frequency  3, change of +1; resulting frequency  4.
    Current frequency  4, change of -2; resulting frequency  2, which has already been seen.

In this example, the first frequency reached twice is 2. Note that your device might need to repeat
its list of frequency changes many times before a duplicate frequency is found, and that duplicates
might be found while in the middle of processing the list.

Here are other examples:

    +1, -1 first reaches 0 twice.
    +3, +3, +4, -2, -4 first reaches 10 twice.
    -6, +3, +8, +5, -6 first reaches 5 twice.
    +7, +7, -2, -7, -4 first reaches 14 twice.

What is the first frequency your device reaches twice?

Your puzzle answer was 481.

You are one gold star closer to fixing the time stream.
"""

import os

SCRIPT_DIR = os.path.dirname(__file__)
# print SCRIPT_DIR
INPUT_DATA_PATH = os.path.join(SCRIPT_DIR, 'test_data', 'Day_01.txt')
# print INPUT_DATA_PATH

def get_total_frequency(input_data=None):
    """
    Calculates the total of input frequency variations

    Args:
        input_data (list, optional): Defaults to None. Series of positive and negative integers

    Returns:
        int: sum of all frequency variations
    """

    frequency_result = 0

    input_data = process_data(input_data)

    if input_data:
        frequency_result = sum(input_data)

    return frequency_result

def process_data(input_data=None):
    """
    Convenience method to read from a data set

    Args:
        input_data (list, optional): Defaults to None. Series of positive and negative integers

    Returns:
        list: Series of positive and negative integers
    """

    if input_data is None:
        with open(INPUT_DATA_PATH) as fp:
            input_data = [int(x) for x in fp.read().split('\n') if x]
    return input_data

def duplicate_frequencies(input_data=None, number_of_occurances=2, frequency_map=None):
    """
    Finds the number occurances the system encounters during summation

    Args:
        input_data (list, optional): Defaults to None. Series of positive and negative integers
        number_of_occurances (int, optional): Defaults to 2. Number of occurances to search for
        frequency_map (dict, optional): Defaults to None. Data to map summation results the number
                                                          of occurances of the summation

    Returns:
        int: Summation value that occured a specified number of times
    """

    frequency = 0
    repeated_frequency = None

    input_data = process_data(input_data)

    if frequency_map is None:
        frequency_map = {}

    while repeated_frequency is None:
        for _freq in input_data:

            frequency += int(_freq)

            if frequency and frequency in frequency_map:
                frequency_map[frequency] += 1

                if frequency_map[frequency] == number_of_occurances:
                    repeated_frequency = frequency
                    break
            else:
                frequency_map.setdefault(frequency, 1)

    return repeated_frequency

if __name__ == '__main__':
    print get_total_frequency()
    print duplicate_frequencies()
