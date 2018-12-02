import numpy

board = []

# https://stackoverflow.com/questions/36834505/creating-a-spiral-array-in-python


def spiral_ccw(input_array):

    # creates an array
    input_array = numpy.array(input_array)

    # creates empty list
    out = []

    # while this array has elements
    while input_array.size:

        out.append(input_array[0][::-1])  # first row reversed

        # cut off first row and rotate clockwise
        input_array = input_array[1:][::-1].T

    # .concatenate joins a sequence of arrays along an existing axis
    return numpy.concatenate(out)


def base_spiral(num_rows, num_cols):
    return spiral_ccw(
        numpy.arange(num_rows * num_cols).reshape(num_rows, num_cols))[::-1]


def to_spiral(input_array):

    # creates an array
    input_array = numpy.array(input_array)

    # creates an array of equal size as input
    B = numpy.empty_like(input_array)

    # .flat flattens and combines array elements to a single array
    B.flat[base_spiral(*input_array.shape)] = input_array.flat

    return B


def find_element(input_array, target):
    result = numpy.where(input_array == target)
    # print result
    # print type(result)

    # for x in result:
    #     print x
    #     print type(x)

    location = (result[0][0], result[1][0])
    print location
    return location


def move_index(input_array, index_location):
    print index_location

    x_index = index_location[0]
    y_index = index_location[1]

    index = 0
    counter = 0

    while index != 1:
        adjecent_index_values = []

        # test left
        if (
                0 <= x_index - 1 < len(input_array) and
                0 <= y_index < len(input_array)
        ):
            adjecent_index_values.append(input_array[x_index - 1, y_index])

        # test right
        if (
                0 <= x_index + 1 < len(input_array) and
                0 <= y_index < len(input_array)
        ):
            adjecent_index_values.append(input_array[x_index + 1, y_index])

        # test up
        if (
                0 <= x_index < len(input_array) and
                0 <= y_index - 1 < len(input_array)
        ):
            adjecent_index_values.append(input_array[x_index, y_index - 1])

        # test down
        if (
                0 <= x_index < len(input_array) and
                0 <= y_index + 1 < len(input_array)
        ):
            adjecent_index_values.append(input_array[x_index, y_index + 1])

        print adjecent_index_values
        adjecent_index_values.sort()
        print adjecent_index_values

        next_index = adjecent_index_values[0]

        new_index = find_element(input_array, next_index)
        x_index = new_index[0]
        y_index = new_index[1]

        counter = counter + 1

    return counter


def make_search_grid(list, target_value):

    size = 0
    while size * size <= target_value:
        size = size + 1

    print size

    if size == 0 or size == 1:
        return 0

    elif size > 1:
        square = size + (size - 1)

        B = numpy.arange(1, (square * square + 1)).reshape(square, square)
        print(B)

        A = to_spiral(B)

        # Flips 2D Array
        B = numpy.flipud(A)

        # Get Location of target value
        start_index = find_element(B, target_value)

        # Traverse 2D array to the center
        result = move_index(B, start_index)
        return result


test = make_search_grid(board, 361527)
print test
