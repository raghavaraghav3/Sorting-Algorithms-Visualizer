def swap(array, i, j):
    """
    Swaps the elements of the array at the given indices.
    """

    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def oddevenSort(array, *args):
    """
    Sorts the given array using the Odd-Even Sort Algorithm.

    Odd-Even Sort Algorithm is a variation of Bubble Sort that sorts
    pairs of adjacent elements with odd or even indices in alternating
    passes. On each pass, it compares the elements in the pair and swaps
    them if they are not in the correct order. The process repeats until
    no more swaps are needed, indicating that the array is sorted.

    Args:
        array: The array to be sorted.

    Yields:
        The current state of the array, along with the indices of the
        elements being compared and swapped (-1 if not applicable).
    """
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(array) - 1, 2):
            yield array, i, i + 1, -1, -1
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                sorted = False

        for i in range(0, len(array) - 1, 2):
            yield array, i, i + 1, -1, -1
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                sorted = False
