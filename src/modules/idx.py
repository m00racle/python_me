def idx(i):
    """
    convert index (starts from 1) to Python index (starts from 0)
    param:
    i (int) = index

    return: int
    """
    if type(i) != type(int()): raise ValueError("the input is not an integer")
    # TODO review we need to check this data type check the test also for the corresponding tests
    if i < 1:
        raise ValueError("the i key index reached 0")
    else:
        return i - 1