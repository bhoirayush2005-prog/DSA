def count_odd_numbers(n, array):
    count = 0

    for i in range(n):
        if array[i] % 2 != 0:
            count += 1

    return count