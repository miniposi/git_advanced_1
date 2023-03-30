def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.
    Args:
        int_list: A list of integer.
    Returns:
        A list of even integers.
    """
    # TODO: Implement even_list
    for num in int_list:
        if num % 2 == 0:
            continue
        else:
            int_list.remove(num)

    return int_list