def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [      O(1)      ]

    This is constant runtime because the comparison is done by indexing.
    Does runtime change if comparison is done by using ==?

    """

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [    O(n)        ]

    This is linear runtime because it is searching in a list.

    """

    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [    O(n)        ]

    I think this is O(n) because lookup in a set is O(1) - for "the if -x in s" line.
    For loop is O(n) and since the assignment of s is outside of the loop so the operation
    shall remain O(n).

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s:
        if -x in s:
            result.append([-x, x])

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [     O(n^2)     ]

    This is quadratic runtime because it is a typical nested for loops.
    It is looping numbers twice for every sum operation.

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y:
                result.append((x, y))
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [       O(n^3)   ]

    I think this is polynomial runtime because there are three loops in this function.
    There is a hidden lookup "(y,x) not in result" and this multiply by the nested for loops
    which makes its runtime to O(n^3). * Not quite sure if the "and" operator and "==" makes any
    difference here, but if it does count then the runtime might go up to O(n^4)?


    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y and (y, x) not in result:
                result.append((x, y))
    return result
