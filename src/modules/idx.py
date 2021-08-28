def idx(i):
    """
    convert index (starts from 1) to Python index (starts from 0)
    param:
    i (int) = index

    return: int
    """
    if i > 0:
        return i - 1
    else:
        raise ValueError("the i key index reached 0")