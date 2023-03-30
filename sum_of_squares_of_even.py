# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list of integers.
    Args:
    even_int_list: A list of even integers.
    Returns:
    The sum of the squares of all even numbers in the list.
    """
    # TODO: Implement sum_of_squares_of_even
    sum = 0
    for num in even_int_list:
        sum = sum + num * num

    return sum