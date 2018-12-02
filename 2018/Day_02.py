#-*- coding: utf-8 -*-
"""
--- Day 2: Inventory Management System ---

You stop falling through time, catch your breath, and check the screen on the device. "Destination
reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now,
to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that
so many people have chimneys, maybe he could sneak in that way?" Another voice responds,
"Actually, we've been working on a new kind of suit that would let him fit through tight spaces
like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans,
everything! Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored
together, so the box IDs should be similar. Too bad it would take forever to search the
warehouse for two similar box IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if
you were discovered - and use your fancy wrist device to quickly scan every box and produce a
list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number
that have an ID containing exactly two of any letter and then separately counting those with
exactly three of any letter. You can multiply those two counts together to get a rudimentary
checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice, and three of them
contain a letter which appears exactly three times. Multiplying these together produces a
checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?

Your puzzle answer was 5681.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype
fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings.
For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz

The IDs abcde and axcye are close, but they differ by two characters (the second and fourth).
However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those
must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by
removing the differing character from either ID, producing fgij.)

Your puzzle answer was uqyoeizfvmbistpkgnocjtwld.

You are one gold star closer to fixing the time stream.
"""

import os
import difflib
from collections import Counter

import utils

SCRIPT_DIR = os.path.dirname(__file__)
# print SCRIPT_DIR
INPUT_DATA_PATH = os.path.join(SCRIPT_DIR, 'test_data', 'Day_02.txt')
# print INPUT_DATA_PATH

COLLECTIONS_MAP = None
INSTANCE_MAP = None

def get_collection(data_item):
    global COLLECTIONS_MAP

    if COLLECTIONS_MAP is None:
        COLLECTIONS_MAP = {}

    if data_item not in COLLECTIONS_MAP:
        c = Counter(data_item)
        COLLECTIONS_MAP[data_item] = c

    return COLLECTIONS_MAP[data_item]

def count_instances(counter=None, instances=None):
    global INSTANCE_MAP

    if counter is None:
        return

    if INSTANCE_MAP is None:
        INSTANCE_MAP = {}
        for instance_num in instances:
            INSTANCE_MAP.setdefault(instance_num, {})
            INSTANCE_MAP[instance_num].setdefault('total', 0)
            INSTANCE_MAP[instance_num].setdefault('items', [])

    for _inst in set(counter.values()):
        if _inst in INSTANCE_MAP:
            INSTANCE_MAP[_inst]['total'] += 1
            INSTANCE_MAP[_inst]['items'].append(counter)


def get_box_ids_checksum(instances=[2,3], input_data=None):
    input_data = utils.process_data(INPUT_DATA_PATH, input_data)

    for data in input_data:
        collection = get_collection(data)
        if collection:
            count_instances(counter=collection, instances=instances)

    _checksum = 1
    for instance_num in INSTANCE_MAP.keys():
        print INSTANCE_MAP[instance_num]['total']
        _checksum *= INSTANCE_MAP[instance_num]['total']

    return _checksum

def get_correct_box_ids(input_data=None):
    input_data = utils.process_data(INPUT_DATA_PATH, input_data)

    matching_text = ''
    for item in input_data:
        for _item in input_data:
            if item == _item:
                continue
            else:
                seq = difflib.SequenceMatcher(None, item, _item)
                d = seq.ratio() * 100
                if d > 95.0:
                    cur_item = set(item)
                    _cur_item = set(_item)
                    diff = cur_item.difference(_cur_item)

                    matching_text = item.replace(''.join(list(diff)), '')
                    break

        if matching_text:
            break

    return matching_text

if __name__ == '__main__':
    print get_box_ids_checksum()
    print get_correct_box_ids()

