def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    for i in range(len(nums) - 2):
        res = sum(nums[i:i + 3])
        if res % 2 == 1:
            return True
    return False

    # lst = [sum(nums[i: i + 3]) for i in range(len(nums)) if len(nums[i:i + 3]) == 3]
    # return lst